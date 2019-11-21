import os
import xlrd
import json


# 怪物json
workbook = xlrd.open_workbook('information.xlsx')
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
# keys=[]
# for i in range(cols):
#     keys.append(sheet.cell(0,i).value)
#
# for i in range(1,rows):
#     d=dict()
#     for j in range(cols):
#         d[keys[j]] = sheet.cell(i,j).value
#     str_json = json.dumps(d,ensure_ascii=False)
#     path = "MonsterINFO/"+str(int(d['编号']))+".json"
#     # if not os.path.exists(path):
#     #     os.mkdir(path)
#     with open(path,"w") as f:
#         json.dump(str_json, f)

# zzh的地点

#找到zzh所给地点里面的所有非空地点list并将其转为唯一的set
workbook1 = xlrd.open_workbook('mountain.xlsx')
sheet1 = workbook1.sheet_by_index(0)
rows1 = sheet1.nrows
cols1 = sheet1.ncols
pl = []
for k in range(rows1):
    if(sheet1.cell(k,3).value != ''):
        pl.append(sheet1.cell(k,3).value)
seq = set(pl)

#找我们的地点在zzh地点里的集合和在文件中所在的位置
pl_in = []
pl_id = []
for k in range(1,rows):
    if(sheet.cell(k,3).value in seq):
        pl_in.append(sheet.cell(k,3).value)
        pl_id.append(k)

#我们的地点的无重复set，再转为list
seq1 = set(pl_in)
l = list(seq1)
dic = dict.fromkeys(l)

# 以地点名为索引建立的dict，给每一个地点对应一个dict
dict_name = ('position_id', 'position_name','monster_number', 'monster_id', 'monster_name')
for i in range(len(l)):
    dic[l[i]] = dict.fromkeys(dict_name) #给每个地点以上面的dict_name对应一个dict

    # 给地点的dict设置position_id
    j = i + 1
    str_id = repr(j)
    str_id = '{0:0>3}'.format(str_id)
    dic[l[i]]['position_id'] = str_id

    # 给地点的dict设置position_name
    dic[l[i]]['position_name'] = l[i]

    # 给地点的dict设置monster_id的list
    list = []
    dic[l[i]]['monster_id'] = list

    # 给地点的dict设置monster_name的list
    list1 = []
    dic[l[i]]['monster_name'] = list1

for i in range(len(pl_id)):
    # 给monster_id的list增砖添瓦
    monster_id = int(sheet.cell(pl_id[i],0).value)
    monster_id_str = str(monster_id)
    monster_id_str = '{0:0>3}'.format(monster_id_str)
    dic[sheet.cell(pl_id[i],3).value]['monster_id'].append(monster_id_str)

    # 给monster_name的list增砖添瓦
    dic[sheet.cell(pl_id[i],3).value]['monster_name'].append(sheet.cell(pl_id[i],1).value)

for i in range(len(dic)):
    dic[l[i]]['monster_number'] = len(dic[l[i]]['monster_id'])

path = "MonsterINFO/zzh_position.json"

with open(path,"w") as f:
    json.dump(dic, f)
print(dic)









#hmq的地点

# # 首先得到hmq所找的非空的地点列表，并把列表转为set（无重复），再把这个set转为list，并以这个list为索引创建dict
# mq_position = []
# for i in range(481,601):
#     if(sheet.cell(i,3).value != ''):
#         mq_position.append(sheet.cell(i,3).value)
# mq_seq = set(mq_position)
# mq_plist = list(mq_seq)
# dic = dict.fromkeys(mq_plist)
#
# # 以地点名为索引建立的dict，给每一个地点对应一个dict
# dict_name = ('position_id', 'position_name', "monster_number",'monster_id', 'monster_name')
# for i in range(len(mq_plist)):
#     dic[mq_plist[i]] = dict.fromkeys(dict_name) #给每个地点以上面的dict_name对应一个dict
#     #给地点的dict设置position_id
#     j = i + 1
#     str_id = repr(j)
#     str_id = '{0:0>3}'.format(str_id)
#     dic[mq_plist[i]]['position_id'] = str_id
#
#     # 给地点的dict设置position_name
#     dic[mq_plist[i]]['position_name'] = mq_plist[i]
#     # 给地点的dict设置monster_id的list
#     list = []
#     dic[mq_plist[i]]['monster_id'] = list
#     # 给地点的dict设置monster_name的list
#     list1 = []
#     dic[mq_plist[i]]['monster_name'] = list1
#
# for i in range(481,601):
#     if(sheet.cell(i,3).value != ''):
#         #给monster_id的list增砖添瓦
#         monster_id = int(sheet.cell(i,0).value)
#         monster_id_str = str(monster_id)
#         monster_id_str = '{0:0>3}'.format(monster_id_str)
#         dic[sheet.cell(i,3).value]['monster_id'].append(monster_id_str)
#         #给monster_name的list增砖添瓦
#         dic[sheet.cell(i,3).value]['monster_name'].append(sheet.cell(i,1).value)
#
# for i in range(len(dic)):
#     dic[mq_plist[i]]['monster_number'] = len(dic[mq_plist[i]]['monster_id'])
#
# path = "MonsterINFO/hmq_position.json"
#
# with open(path,"w") as f:
#     json.dump(dic, f)
#
# print(dic)






















# seq = ('q','w','e')
# dict = dict.fromkeys(seq)
# # print("新字典为 : %s" % str(dict))
# print(dict)
# d = {}
# list = []
# list.append('haha1')
# list.append('haha2')
# d['haha']=list
# d['hehe'] = 'hehe'
# dict[seq[0]] = d
# print(dict)
# print(d['haha'][0])
# dict = dict.fromkeys(seq[0],1)
# print("新字典为 : %s" % str(dict))