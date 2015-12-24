#!/usr/bin/env python
# coding:utf-8

import MySQLdb
from config.config import db_dict
import sys
 
 
class SqlDbHelp(object):
     
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(**db_dict)
        except Exception,e:
            print e
            sys.exit('连接异常')
        
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        self.conn.query('set names utf8')
    
    # 执行SQL语句    
    def query(self,sql,params=None):
        if params is None:
            try:
                return self.cursor.execute(sql)
            except Exception,e:
                print e
                sys.exit('语法错误')
        else:
            try:
                return self.cursor.execute(sql,params)
            except Exception,e:
                print e
                sys.exit('语法错误')
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    # 查询单行语句
    def getOne(self,sql,params):
        self.query(sql,params)
        return self.cursor.fetchone()
    
    # 查询多行语句
    def findAll(self,sql,params=None):
        self.query(sql,params)
        return self.cursor.fetchall()
    
    # 添加数据
    def addData(self,sql,params):
        self.query(sql, params)
        lastid = self.cursor.lastrowid
        self.conn.commit()
        return lastid
    
    # 修改数据
    def updateData(self,sql,params):
        result = self.query(sql, params)
        if result == 1:
            self.conn.commit()
            return True
        else:
            return False
    
    # 删除数据
    def deleteData(self,sql,params):
        result = self.query(sql, params)
        if result == 1:
            self.conn.commit()
            return True
        else:
            return False    
        
    
    
#mysql = SqlDbHelp();

#sql = "select * from cate where id=%s"
#params = (1,)
#print mysql.getOne(sql, params)

#sql = "select * from cate"
#params = None
#print mysql.findAll(sql, params)
    
#sql = "insert into cate (cname,ename,pid,status) values (%s,%s,%s,%s)"
#params = ('测试111','azhnag',0,1)
#print mysql.addData(sql, params)
    

#sql = "update cate set cname=%s where id=%s"
#params = ('测试中',16)
#print mysql.updateData(sql, params)    
    
    
#sql = "delete from cate where id=%s"
#params = (15,)
#print mysql.deleteData(sql, params)   
    
    
    
    
    
    
    
    
    
    
    
    