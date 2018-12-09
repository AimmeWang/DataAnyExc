
"""
描述： 王婷同学的学习资料
时间：2018-12-9
作者：Acmen
"""

# 1. 从csv读出来数据
# 2. 把数据整理
# 3. 把数据存储在mysql中

import numpy as AEnp
import pandas as AEpd
import pymysql as AEsql

"""
数据库连接
"""
db = None
def ConnSql():
	global db
	if db == None:
		db= AEsql.connect(host="localhost",user="Acmen", password="Acmen",db="aimmetest",port=3306)
	cur = db.cursor()
	return cur

"""
数据库关闭
"""
def CloseSql():
	global db
	if db != None:
		db.close()
	db = None

"""
从csv里面读取
"""
def ReadFromCSV(filname, header):
	csv = AEpd.read_csv(filname,header = header)
	df = AEpd.DataFrame(csv)
	return df

"""
插入到数据中
"""
def InsertIntoLoan_sum(uid, month, loan_sum):
	sql = "insert into t_loan_sum(uid, month, loan_sum) values(" + str(uid) + ",'" + str(month) + "'," + str(loan_sum) +")"
	try: 
		cur = ConnSql()
		cur.execute(sql)
		db.commit()
	except:
		db.rollback()

def ConverLoan_sumToSql():
	df = ReadFromCSV('t_loan_sum.csv', header = 0)
	for idx, row in df.iterrows():
		uid = row["uid"]
		month = row["month"] + "-1"
		loan_sum = row["loan_sum"]
		InsertIntoLoan_sum(uid, month, loan_sum)

	CloseSql()


def InsertIntot_click(uid,click_time,pid,param):
	sql = "insert into t_click(uid,pid,param,click_time) values(" + str(uid) + "," + str(pid) + "," + str(param) + ",'" + str(click_time) + "')"
	print(sql)
	try:
		cur = ConnSql()
		cur.execute(sql)
		db.commit()
	except Exception as e:
		print(e)
		db.rollback()

def convert_click():
	df = ReadFromCSV('t_click.csv',header = 0)
	for idx, row in df.iterrows():
		uid =  row["uid"]
		click_time = row["click_time"]
		pid = row["pid"]
		param = row["param"]
		print(idx, uid, click_time)
		InsertIntot_click(uid,click_time,pid,param)
	
	CloseSql()
		
convert_click()
