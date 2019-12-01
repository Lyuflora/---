# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from datetime import timedelta
import readjson, json,random,string, db
import os
import sqlite3

app = Flask(__name__)
app.config.update(JSON_AS_ASCII = True)
# # 设置静态文件缓存过期时间
# app.send_file_max_age_default = timedelta(seconds=1)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        input_name = request.form.get('monster_name')
        monster_id = db.selectIDbyName(input_name)
        if monster_id=="Can't find!":
            return render_template('notfound.html')
        return redirect("/monster_id="+str(monster_id).zfill(3))
        # return redirect("/api/monster/"+str(monster_id).zfill(3))
    return render_template('index.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/catalog_zgbgl')
def catalog_zgbgl():
    cjson = readjson.openjson("new_zgbgl.json")
    list = cjson["《中国百鬼录》"]['id']
    number = len(list)
    page_num = int((number-1)/40)+1
    return render_template('catalog_zgbgl.html', cjson=cjson, number=number, page_num=page_num)

@app.route('/catalog_lzzy')
def catalog_lzzy():
    cjson = readjson.openjson("lzzy.json")
    list = cjson["《聊斋志异》"]['id']
    number = len(list)
    page_num = int((number-1)/40)+1
    return render_template('catalog_lzzy.html', cjson=cjson, number=number, page_num=page_num)


@app.route('/catalog_ssj')
def catalog_ssj():
    cjson = readjson.openjson("ssj.json")
    list = cjson["《搜神记》"]['id']
    number = len(list)
    page_num = int((number-1)/40)+1
    return render_template('catalog_ssj.html', cjson=cjson, number=number, page_num=page_num)


@app.route('/catalog_qt')
def catalog_qt():
    cjson = readjson.openjson("new_qt.json")
    list = cjson["其他"]['id']
    number = len(list)
    page_num = int((number-1)/40)+1
    return render_template('catalog_qt.html', cjson=cjson, number=number, page_num=page_num)

@app.route('/catalog_shj')
def catalog_shj():
    cjson = readjson.openjson("new_shj.json")
    list = cjson["《山海经》"]['id']
    number = len(list)
    page_num = int((number-1)/40)+1
    return render_template('catalog_shj.html', cjson=cjson, number=number, page_num=page_num)


@app.route('/map1')
def map1():
    mjson = readjson.openjson("hmq_position.json")
    print(mjson)
    return render_template('map1.html', mjson=mjson)

@app.route('/map2')
def map2():
    mjson = readjson.openjson("zzh_position.json")
    return render_template('map2.html', mjson=mjson)

@app.route('/monster_id=<id>', methods=['POST','GET'])
def single(id):
    info = db.getINFObyID(id)
    if request.method=='POST':
        message = request.form.get('message')
        db.insertComment((id, message))
    comments = db.showCommentY(id)
    return render_template('single.html', mjson=info, comments = comments)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/addpage', methods=['POST','GET'])
def addnew():
    if request.method == 'POST':
        d = dict()
        d['id'] = db.getMonsterNum() + 1
        print(d['id'], type(d['id']))
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
            img.save('./static/image/'+str(d['id'])+'/1.png')
            d['imgsrc'] = './static/image/'+str(d['id'])+'/'
        db.addNewMonster(d)


        temp = readjson.openjson('new_qt.json')
        qt_json = temp['其他']
        print(type(qt_json['id'][0]))
        qt_json['id'].append(str(d['id']))
        qt_json['怪物名称'].append(d['怪物名称'])
        qt_json['别名'].append(d['别名'])
        qt_json['活动地点'].append(d['活动地点'])
        qt_json['白话故事'].append(d['白话故事'])
        qt_json['古文引用'].append(d['古文引用'])
        qt_json['技能'].append(d['技能'])
        qt_json['外貌'].append(d['外貌'])
        qt_json['图片数量'].append(d['图片数量'])
        qt_json['imgsrc'][str(d['id'])] = []
        qt_json['imgsrc'][str(d['id'])].append('./static/image/' + str(d['id']) + '/1.png')
        temp['其他'] = qt_json
        with open('./static/json/new_qt.json', 'w') as file:
            json.dump(temp, file)
        # file.close()

        return redirect('/monster_id='+str(d['id']).zfill(3))

    return render_template('addpage.html')

if __name__ == '__main__':
    app.run(port='8888', debug=True)