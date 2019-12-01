# Key Techniques

本篇将简要介绍项目的几个亮点及关键技术实现。

## 1. 分布地图

#### 功能简介

除部分出处不可考的怪物外，大部分怪物信息都记载着出没地点。为直观地反应怪物的地理分布情况，在网页上展示志怪分布地图，统计显示各地的怪物分布情况，并可响应用户的交互指令跳转至详细信息。

#### 技术依赖

百度地图API；echarts.js

#### 实现思路

地图的实现主要是通过使用**echarts.js的散点图**来实现。

首先调用百度地图的api，通过注册用户的密钥调用百度地图，初始化在map-containter中。

然后定义**信息数组和位置数组**，将地区名字，地区的妖怪数量以及地区标签的路由记录进信息数组**data**，再将地区的名字以及地区的精度和纬度记录进位置数组**geoCoordMap**，并且将两个数组合并在一起。

在**option**中可以设置地图的呈现方式。在title中填入图表名称和子标题，在tooltip提示栏中设置提示信息，在bmap中把地图改成自己想要呈现的样式，在series里修改三点的呈现形式，包括颜色，大小等。

最后在散点被选中时调用**mychart.on("click", function(e))**，使用function(e)中的location.href = e.data.url连接到相应的信息位置。

#### 关键代码

##### 地图数据处理

```javascript
	    var dom = document.getElementById("map-container");
		var myChart = echarts.init(dom);
		var app = {};
		option = null;
		var data = [
			{name: '安徽', value: 4, url:'#position025'},
			...,
			{name: '重庆', value: 2, url:'#position030'},
		];
		var geoCoordMap = {
			'安徽':[117.27,31.86],
			...,
			'重庆':[106.54,29.59],
		};
		var convertData = function (data) {
			var res = [];
			for (var i = 0; i < data.length; i++) {
				var geoCoord = geoCoordMap[data[i].name];
				if (geoCoord) {
					res.push({
						name: data[i].name,
						value: geoCoord.concat(data[i].value),
						url: data[i].url
					});
				}
			}
			return res;
		};
```

##### 地图样式定义

```javascript
option = {
			title: {
				text: '志怪分布图',
				subtext: '妖怪数量各省市分布',
				sublink: './index.html',
				left: 'center'
			},
			tooltip : {
				trigger: 'item',
				formatter: function (param) {
					 return param.name + '  ' + param.value[2];
				},
			},
			bmap: {
				center: [104.114129, 33.550339],
				zoom: 5,
				roam: true,//允许缩放
				mapStyle: {
					styleJson: ...,
				}
			},
			series : [ ...,
			]
		};;
```

##### 响应用户指令，跳转至详细信息

```javascript
if (option && typeof option === "object") {
			myChart.setOption(option, true);
			myChart.on("click",function(e){
				console.log(e);
				//window.open(e.data.url);
				location.href=e.data.url;
			});
		}
```

## 2. 信息检索

#### 功能简介

为方便用户查询怪物信息，在首页植入搜索功能。用户可通过输入怪物姓名跳转至详情页面，若无相应怪物存在则跳转至404小游戏界面。

#### 技术依赖

python-request, sqlite3

#### 实现思路

信息检索涉及到前端向后端传送数据以及后端的响应，我们利用HTML表单来完成数据交互。用户在前端页面的文本框中输入想要搜索的怪物名称，点击提交按钮后，这一信息被封装在POST请求中发往服务端。后端解析请求，提取出怪物名称，在数据库中查询得到对应的怪物ID编号，并将页面重定向到该怪物的详情页面。

![form](form.png)

在数据库中查询时，执行select语句如下

```sql
SELECT id FROM monster_dict WHERE name LIKE \'%'+name+'%\
```

#### 关键代码

##### 前端表单信息

```html
<form action="" class="selectparent" method="post" enctype="multipart/form-data">
    <input id="select1" type="text" name="monster_name" value="西王母">
    <input id="select2" type="submit" value="搜索">
</form>
```

##### 后端解析表单

```python
    if request.method == 'POST':
        input_name = request.form.get('monster_name')
        monster_id = db.selectIDbyName(input_name)
        if monster_id=="Can't find!":
            return render_template('notfound.html')
        return redirect("/monster_id="+str(monster_id).zfill(3))
```

##### 数据库查询

```python
def selectIDbyName(name=''):
    connect = sqlite3.connect('./static/db/monster.db')
    cur = connect.cursor()
    cur.execute('SELECT id FROM monster_dict WHERE name LIKE \'%'+name+'%\'')
    res = cur.fetchall()
    connect.commit()
    connect.close()
    if res:
        return res[0][0]
    else:
        return "Can't find!"
```

## 3. 怪物添加

#### 功能简介

为方便志怪录内容的更新，设计添加新怪物界面，用户可通过输入怪物基本信息，提交后数据库将被更新。新怪物默认被添加至“其他”分类下。

#### 技术依赖

python-request, sqlite3

#### 实现思路

与搜索功能类似，前端通过HTML表单将数据发送给后端。后端在数据库中增加怪物信息，并将页面重定向至新怪物的详情界面。

#### 关键代码

##### 后端更新怪物信息

```python
@app.route('/addpage', methods=['POST','GET'])
def addnew():
    if request.method == 'POST':
        d = dict()
        d['id'] = db.getMonsterNum() + 1
        d['别名'] = request.form.get('another_name')
        d['古文引用'] = request.form.get('guwen')
        d['怪物名称'] = request.form.get('monster_name')
        d['外貌'] = request.form.get('appearance')
        d['白话故事'] = request.form.get('baihua')
        d['技能'] = request.form.get('skill')
        d['活动地点'] = request.form.get('places')
        img = request.files['file']
        if img:
            d['图片数量'] = 1
            os.mkdir('./static/image/'+str(d['id']))
            img.save('./static/image/'+str(d['id'])+'/1.jpg')
            d['imgsrc'] = './static/image/'+str(d['id'])+'/'
        db.addNewMonster(d)
        return redirect('/monster_id='+str(d['id']).zfill(3))
    return render_template('addpage.html')
```

## 4. 评论

#### 功能简介

为进一步完善网站的用户交互体验，在每个怪物的详情页下有评论功能。用户可自由发表对该怪物的评论。所有评论都会展示在该怪物的详细信息下面。

#### 技术依赖

python-request, sqlite3, python-jinjia

#### 实现思路

在数据库中为评论信息单独建一张表，存有评论楼层、评论时间、怪物编号、评论内容等信息。

为了显示评论，后端在数据库中根据怪物ID检索出所有的评论信息并返回给前端。前端HTML代码中嵌入jinjia模板，循环处理每一条评论并展示在页面中。

为了添加评论，每次解析HTML表单得到新的评论信息后，都将其加入数据库，更新评论表。

#### 关键代码
##### 前端展示评论

```html
<div id="comment">
    <h3>Comments</h3>
    {% for i in range(comments['num']) %}
    <p style="margin-left: 35px;margin-right: 35px;border-bottom: 0.3px solid #dcdcdc;padding-bottom: 20px;margin-top: 10px;margin-bottom: 10px;padding-top: 20px;">
        <strong>{{i+1}}楼   </strong> 
        {{ comments['context'][i] }}</p>
    {% endfor %}
</div>
```

##### 数据库检索评论

```python
sql = "SELECT * from monster_comment WHERE monster_id = {monster_id}".format(monster_id=mid)
```

##### 后端更新评论

```python
if request.method=='POST':
    message = request.form.get('message')
    db.insertComment((id, message))
comments = db.showCommentY(id)
```

## 5. 数字水印

#### 功能简介

为了在项目中运用数字版权管理及媒资管理相关知识，我们给所有的怪物图片统一格式，并添加数字水印。

#### 技术依赖

opencv-python

#### 实现思路

利用课堂前置知识，我们设计一张黑白水印图，为“志怪录”文字LOGO。将水印图的每一个像素值压缩后植入原图像素的二进制数末尾，完成数字水印的添加。

![logo](watermark.png)



#### 关键代码

因为已在前置作业中展示过相关代码，此处囿于篇幅不再赘述。