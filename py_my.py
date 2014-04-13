# encoding: utf-8
'''
analyze_lrc -- Python script for generating lrc file
'''

import MySQLdb
import pdb

db = MySQLdb.connect(host="192.168.7.100", user="root", passwd='123456', db='voa')

cur = db.cursor()

cur.execute('select * from lrcs')

avg_line = []
for row in cur.fetchall():
    avg_line.append(row[3] / row[5])
    pass

su = 0.0
for i in avg_line:
    su += i

print (su / len(avg_line))