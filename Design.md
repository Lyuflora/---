

| 成员姓名： |            Group 6            |
| ---------- | :--------------------------------------------------------: |
| 专业：     |                        数字媒体技术                        |

















# Design

## 一、整体界面设计及界面展示

​		整体界面设计偏古风设计，使用小组成员专门设计的logo和海报。

![img](http://m.qpic.cn/psb?/de06b7ca-68f9-4534-a891-7c70327ebeaa/49nX8SCtLEC1u4tw9Bw34rJkoe2SgX16fkP9v6QnH1s!/b/dIQAAAAAAAAA&bo=OASQDQAAAAADhwM!&rf=viewer_4)

​																							主页面

![img](http://m.qpic.cn/psb?/de06b7ca-68f9-4534-a891-7c70327ebeaa/NVKFJpY8j5SOwGFrIpI1Bwn7hvU*F72*Itbi7uQEcGM!/b/dL4AAAAAAAAA&bo=OAQGBQAAAAADZ30!&rf=viewer_4)

​																							目录页

![img](http://m.qpic.cn/psb?/de06b7ca-68f9-4534-a891-7c70327ebeaa/gdkR8II*fHeWZx9AKLMy.oTYsvDP9A6nD0eMm9hM2QM!/b/dLgAAAAAAAAA&bo=OAR4BQAAAAADVzM!&rf=viewer_4)

​																							书籍目录页

![img](http://m.qpic.cn/psb?/de06b7ca-68f9-4534-a891-7c70327ebeaa/NSXZUiDXBjCzx56yiZ8jgnaezGefqwAgG1Ms8ebqCtI!/b/dFQBAAAAAAAA&bo=OARtBgAAAAADVyU!&rf=viewer_4)																						妖怪分布图

![img](http://m.qpic.cn/psb?/de06b7ca-68f9-4534-a891-7c70327ebeaa/qtNtBls39VIhRjAdnPaCbdGeSuChT2XrK3JPQbHbrv4!/b/dFEBAAAAAAAA&bo=OAShBAAAAAADV.s!&rf=viewer_4)

​																						创建新怪物



![img](http://m.qpic.cn/psb?/de06b7ca-68f9-4534-a891-7c70327ebeaa/Gjz3Cofbng.B9mOY21wSqyln9lB.ebNJ8bRjUnDXX4A!/b/dFIBAAAAAAAA&bo=OAQtCAAAAAADd0s!&rf=viewer_4)																						妖怪个人页

![img](http://m.qpic.cn/psb?/de06b7ca-68f9-4534-a891-7c70327ebeaa/8sUKQhJouz.OqMSgdtK5h5hFE7BsaIi9ViCznx8UTBI!/b/dL8AAAAAAAAA&bo=NQU4BAAAAAADV34!&rf=viewer_4)

​																							联系页

## 二、整体设计

### 1.部署图

本项目的部署图如下：<br>

<img src="https://ftp.bmp.ovh/imgs/2019/11/870229cf078c312c.png" width = "1500" div align=center />

### 2.前端

前端部分主要完成了index.html、catalog.html、catalog_{{bookname}}.html、map.html、notfound.html、monster_ip={{number}}.html几个页面。

![img](https://m.qpic.cn/psb?/de06b7ca-68f9-4534-a891-7c70327ebeaa/.O55M01mcYjApCREW1bkkTYxfIw5gsYez12z4f6BvH0!/b/dL4AAAAAAAAA&bo=FgNmAQAAAAARB0I!&rf=viewer_4)

#### **index.html**

Index.html是首页，主要实现了**封面图轮播，妖怪推荐**等功能。

封面图轮播(topimage.js)是把封面的三张图片存在一个unordered list中，设置一个计时器timer，通过设定一定的间隔时间轮换图片，轮换图片时调用changeImg，通过将所有的图片的style属性中的display改正none，要呈现的图片的样式设置为block就可以实现轮播效果。同时通onmouseover和onmouseout可以控制鼠标悬浮在图片上时让图片停止轮播。

具体代码如下：

```javascript
var timer = null,
    index = 0,
    pics = document.getElementsByClassName("banner-slide"),
    ulis = document.getElementById("nav-main"),
    lis = ulis.getElementsByTagName("li");
 
 
//封装一个代替getElementById()的方法
function byId(id){
    return typeof(id) === "string"?document.getElementById(id):id;
}
 
function slideImg() {
    var main = byId("mainimage");
    var banner = byId("banner-main");
    main.onmouseover = function(){
        stopAutoPlay();
    }
    main.onmouseout = function(){
        startAutoPlay();
    }
    main.onmouseout();
 
    //点击导航栏切换图片
    pics[0].id = "imageshown";
    for(var i=0;i<pics.length;i++){
        lis[i].id = i;
          //给每个li项绑定点击事件
        lis[i].onclick = function(){
          //获取当前li项的index值
            index = this.id;
            changeImg();
        }
    }
}
//开始播放轮播图
function startAutoPlay(){
    timer = setInterval(function(){
        index++;
        if(index>=3){
            index = 0;
        }
        changeImg();
    },2300);
}
//暂停播放
function stopAutoPlay(){
    if (timer) {
        clearInterval(timer);
    }
}
//改变轮播图
function changeImg(){
  
    for(var i=0;i<pics.length;i++){
        pics[i].style.display = "none";
        lis[i].className = "";
    }
    pics[index].style.display = "block";
    pics[index].id = "imageshown";
    lis[index].className = "changeColor";
}
slideImg();
```



#### catalog.html

catalog.html是总目录页，将几本书通过卡片形式呈现出来，通过点击可以链接到子目录页。

 

#### catalog_{{bookname}}.html

catalog_{{bookname}}.html是子目录页，用于**展示所有该书中的妖怪**。由于妖怪数量过多，所以选择通过**循环形式呈现**，具体代码如下：

```html
{% for i in range(0,page_num-1) %}
<div class="content wow fadeIn" data-wow-delay=".1s" data-wow-duration="1s">
    {% for j in range(0, 40) %}
    <div class="lg-1-4 md-1-3 sm-1-2">
        <div class="wrap-col">
            <div class="product">
                <div class="product-content">
                    <div class="row">
                        <h2 class="product-title"><a href="#">{{cjson['《中国百鬼录》']['怪物名称'][40*i+j]}}</a></h2>
                        <div class="categories">
                            <a href="#" rel="tag">{{cjson['《中国百鬼录》']['活动地点'][40*i+j]}}</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% endfor %}
<div class="content wow fadeIn" data-wow-delay=".1s" data-wow-duration="1s">
    {% for j in range(page_num*40-40, number) %}
    <div class="lg-1-4 md-1-3 sm-1-2">
        <div class="wrap-col">
            <div class="product">
                <div class="product-content">
                    <div class="row">
                        <h2 class="product-title"><a href="#">{{cjson['《中国百鬼录》']['怪物名称'][j]}}</a></h2>
                        <div class="categories">
                            <a href="#" rel="tag">{{cjson['《中国百鬼录》']['活动地点'][j]}}</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
	{% endfor %}
</div>
```

而该目录下的分页效果主要通过嵌入式的javascript代码实现，首先将妖怪的名片分成一块一块的，通过点击上一页和下一页控制js中的**nowPage**决定显示哪一页，**其他的style.display设为none，而nowPage所在的一块设置为block**。

具体代码如下：

```javascript
//封装函数、图片显示的部分、传入获取到的div，和被点击的序号
function toggle(eles, active) {
    for(var i = eles.length; i--;) {
        eles[i].style.display = "none"; //先让所有div隐藏
    }
    eles[active].style.display = "block";//再让被点击的序号对应的div 显示
    location.href="#";
}
//获取按键和div
var aItem = document.getElementsByClassName("content wow fadeIn");
var prev = document.getElementsByClassName("prev");
var next =  document.getElementsByClassName("next");
var nowPage = 0; //定义当前页，默认值为0；
var pagenum = aItem.length;
toggle(aItem,0);

//下一页
next[0].onclick = function () {
    if(nowPage<pagenum-1)
    {
        nowPage++;
        toggle(aItem,nowPage);
    }
}

//上一页
prev[0].onclick=function(){
    if(nowPage>0)
    {
        nowPage--;
        toggle(aItem,nowPage);
    }
}
```



#### map.html

map.html的不同地区妖怪是从json里面调出来循环呈现的，散点图的实现在关键技术部分会详细呈现。

 

#### notfound.html

notfound.html主要是针对首页搜索不到的情形，主要是通过**embed标签**将lusongsongzhuamao.swf的**flash**互动文件调用，从而可以进行阻止猫跳出去的游戏。

具体代码如下：

```html
<embed align=center height="400" type="application/x-shockwave-flash" 
						width="600" src="../static/images/lusongsongzhuamao.swf"
						allowscriptaccess="sameDomain" flashvars="width=600&amp;height=400" 
						scale="noborder" quality="high" wmode="transparent" style="position:relative; left: 25%;"></embed>
```



#### monster_ip={{number}}.html

monster_ip={{number}}.html界面是妖怪信息的具体呈现，显示了妖怪的名称，别名，分布地点，长相，技能，白话介绍，文言文引用的几个部分的信息。最后还设置了一个表单供游客进行评论，评论将会**通过表单模式post到后端去**，从而存储在数据库中，供页面渲染时调用。

评论上传具体代码如下:

```html
<div class="zerogrid" id="comment_submit">
    <div class="comments-are">
        <div id="comment">
            <h3>Leave a Comment</h3>
            <span>Your comments will be published in website. Required fields are marked </span>
            <form name="form1" id="comment_form" method="post" action="">
                <label>
                    <textarea name="message" id="message"></textarea>
                </label>
                <center><input class="button button-skin " type="submit" name="SubmitComment" value="Submit"></center>
            </form>
        </div>
    </div>
</div>

```



### 3.后端

#### 利用`Flask`框架实现前后端的连接及数据交互

通过`Flask`框架，连接到主页面（`index.html`），书籍目录页（`catalog.html`），具体书籍所包含妖怪的目录页（`catalog_zgbgl.html`, `catalog_lzzy`, `catalog_ssj.html`, `catalog_shj.html`, `catalog_qt.html`），地图页（`map1.html`,`map2.html`），单独的怪物网页（`single.html`），此处根据怪物id获取怪物的具体信息，动态路由到怪物信息的具体界面，添加怪物界面（`addpage.html`）和”联系我们“界面（`contact.html`）。

其中后端通过`json`文件向前端具体书籍所包含的妖怪目录页提供每本书中所有妖怪的所有信息，向地图页提供固定地点的名称和经纬度以及活动地点在此地的怪物的数量、id及名称；通过数据库记录单独的怪物信息，并捕捉添加怪物信息界面的新增信息，实时更新数据库中的怪物信息，并将新增怪物归类为“其他”类怪物，添加到类别“其他”所对应的`json`文件中。

通过上述的操作，实现了前后端的连接和数据交互。

#### 后端数据存储的格式

##### a.地点的`json`文件

其中`position_id`，`position_name`为字符串类型；`monster_number`为整数类型；`monster_id`，`monster_name`为列表（list）类型。

```json
{
    position: {
        "position_id": position_id, 
        "position_name": position_name, 
        "monster_number": monster_number,
        "monster_id": monster_id_list, 
        "monster_name": monster_name_list
    }
}
```

##### b.具体书籍的`json`文件

其中，`id`，`怪物名称`，`别名`，`活动地点`，`白话故事`，`古文引用`，`技能`，`外貌`，`图片数量`均为列表（list）类型，`imgsrc`为字典（dictionary）类型，其中根据怪物的id作为索引，用列表存储不同怪物的所有图片地址。

```
{
    book_name: {
        "id": id_list, 
        "怪物名称": name_list, 
        "别名": name2_list,
        "活动地点": position_list, 
        "白话故事": story_list,
        "古文引用": story2_list,
        "技能": skill_list,
        "外貌":appearance_list,
        "imgsrc": {
        	monster_id: imgsrc_list
        },
        "图片数量": img_number_list
    }
}
```



### 4.数据库

本系统采用sqlite关系数据库管理系统，在后台实现网站内容的管理，包括妖怪条目的文字、图片，以及用户的留言评论。sqlite作为嵌入式数据库可以为网页服务存储数据，而且有轻量级、允许多线程访问的优势。

在本项目的数据库模块中，我们的设想是：

- 使每个妖怪名下有单独的词条，并附有用户对其的评论；
- 用户可搜索妖怪名称，浏览指定书籍中的妖怪名单。

根据以上构思，在数据库的实现中，首先调用sqlite的API创建数据库和数据表，根据制定的妖怪词条格式，设计数据库的schema，再对记录实现增、删、改、查的管理。本数据库主要的数据表是记录妖怪词条的数据表`monster_dict`，对每一个妖怪词条自动分配id，并且从前期调研阶段整合的资料中读取数据；针对用户体验，我们增加了用户评论数据表`monster_comment`，从前端返回的评论将存储在数据表中。

本系统数据库的E-R图如下：

<img src="https://ftp.bmp.ovh/imgs/2019/11/a7ef5464c10a2a86.png" width = "1000" div align=center />

#### 数据表的实现

妖怪记录的数据表如下（截取部分列）：
<img src="https://ftp.bmp.ovh/imgs/2019/11/29a0bc888f10042c.png" width = "1500" div align=center />

用户评论的数据表如下：

<img src="https://ftp.bmp.ovh/imgs/2019/11/5ddf50ab633c8bdd.png" width = "500" div align=center />

妖怪数据表的实现如下：

```
create table monster_dict(
      id INT UNSIGNED PRIMARY KEY,
      name VARCHAR(20) NOT NULL,
      secname VARCHAR(40), 
      place text, 
      story text, 
      acientchinese text, 
      skill text, 
      appearance text, 
      image_dir text,
      image_num INT 
);
```

评论数据表的实现如下：

```
CREATE TABLE monster_comment(
	comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
	monster_id INT NOT NULL,
	comment_content  NVARCHAR(400),
	CreatedTime TimeStamp NOT NULL DEFAULT (datetime('now','localtime')),
	FOREIGN KEY(monster_id) REFERENCES monster_dict(id)
);
```

