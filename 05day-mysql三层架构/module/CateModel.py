#!/usr/bin/env python
# coding:utf-8

from utility.SqlDbHelp import SqlDbHelp

class CateModel(object):
    
    def __init__(self):
        self.sqldbhelper = SqlDbHelp()
    
    
    def editCate(self,sql,params):
        return self.sqldbhelper.updateData(sql, params)
    
    