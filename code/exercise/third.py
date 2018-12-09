
"""
描述： 王婷同学的学习资料
时间：2018-12-8
作者：Acmen
"""

import pandas as pd
import numpy as np
import pymysql

def QueryData():
	db= pymysql.connect(host="localhost",user="Acmen", password="Acmen",db="aimmetest",port=3306)
	cur = db.cursor()
	sql = "select * from t_loan_sum"
	try:
		cur.execute(sql)
		results = cur.fetchall()
		print(results)
		for row in results :
			uid = row[0]
			month = row[1]
			loan_num = row[2]
			print(uid, month, loan_num)
	except Exception as e:
		raise e

	db.close()

# QueryData()
db= pymysql.connect(host="localhost",user="Acmen", password="Acmen",db="aimmetest",port=3306)
cur = db.cursor()

def InsetToLoan_sum(uid, month, loan_sum):
	sql = "insert into t_loan_sum(uid, month, loan_sum) values(" + str(uid) + ",'" + str(month) + "'," + str(loan_sum) + ")"
	try:
		cur.execute(sql)
	except Exception as e:
		raise e



def TestPandas():
	csv = pd.read_csv('t_loan_sum.csv',header=0)
	df = pd.DataFrame(csv)
	index = 0
	for iex, row in df.iterrows():
		index += 1
		if(index >= 5):
			break

		InsetToLoan_sum(row['uid'], row['month'], row['loan_sum'])

	db.close()
# 1. 从csv读出来数据
# 2. 把数据整理
# 3. 把数据存储在mysql中

TestPandas()