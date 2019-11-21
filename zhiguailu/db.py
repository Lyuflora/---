import sqlite3
import os

def selectIDbyName(name=''):
    connect = sqlite3.connect('./static/db/monster.db')
    cur = connect.cursor()
    cur.execute('SELECT id FROM monster_dict WHERE name LIKE \'%'+name+'%\'')
    print('SELECT id FROM monster_dict WHERE name LIKE \'%'+name+'%\'')
    res = cur.fetchall()
    connect.commit()
    connect.close()
    if res:
        return res[0][0]
    else:
        return "Can't find!"

def getMonsterNum():
    connect = sqlite3.connect('./static/db/monster.db')
    cur = connect.cursor()
    cur.execute('SELECT max(id) FROM monster_dict')
    res = cur.fetchall()
    connect.commit()
    connect.close()
    if res:
        return res[0][0]
    else:
        return "Can't find!"

def addNewMonster(dict):
    connect = sqlite3.connect('./static/db/monster.db')
    cur = connect.cursor()
    sql = 'insert into monster_dict values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cur.execute(sql, (dict['id'], dict['怪物名称'], dict['别名'], dict['活动地点'], dict['白话故事'],
                      dict['古文引用'], dict['技能'], dict['外貌'], dict['imgsrc'], dict['图片数量']))
    connect.commit()
    connect.close()

def getINFObyID(id):
    connect = sqlite3.connect('./static/db/monster.db')
    cur = connect.cursor()
    cur.execute('SELECT * FROM monster_dict WHERE id='+str(id))
    tuple = cur.fetchall()
    connect.commit()
    connect.close()
    if tuple[0]:
        info = dict()
        info['id'] = tuple[0][0]
        info['怪物名称'] = tuple[0][1]
        info['别名'] = tuple[0][2]
        info['活动地点'] = tuple[0][3]
        info['白话故事'] = tuple[0][4]
        info['古文引用'] = tuple[0][5]
        info['技能'] = tuple[0][6]
        info['外貌'] = tuple[0][7]
        info['图片数量'] = tuple[0][9]
        list = []
        info['imgsrc'] = list
        img_list = os.listdir(tuple[0][8])
        for j in range(info['图片数量']):
            info['imgsrc'].append(tuple[0][8] + img_list[j])
        return info
    else:
        return "Can't find!"

# 增加单条评论 （妖怪id, 评论内容）
def insertComment(tuple):
    connect = sqlite3.connect('./static/db/monster.db')
    cursor = connect.cursor()
    n = 0
    sql = "INSERT INTO monster_comment (MONSTER_ID, COMMENT_CONTENT) VALUES "

    sql = sql + "{}"
    sql = sql.format(tuple)

    cursor.execute(sql)
    connect.commit()
    connect.close()


# 筛选妖怪Y的评论 （妖怪id）
def showCommentY(mid):
    connect = sqlite3.connect('./static/db/monster.db')
    cursor = connect.cursor()
    sql = "SELECT * from monster_comment WHERE monster_id = {monster_id}".format(monster_id=mid)
    cursor.execute(sql)
    connect.commit()
    comment = dict()
    comment['num'] = 0
    comment['context'] = list()
    for row in cursor:
        # print("COMMENT_ID = ", row[0])
        # print("COMMENT_CONTENT = ", row[2], "\n")
        comment['context'].append(row[2])
        comment['num'] = comment['num']+1
    connect.close()
    return comment
