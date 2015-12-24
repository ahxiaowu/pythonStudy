#!/usr/bin/env python
# coding:utf-8


from module.CateModel import CateModel

def main():
    
    cateModel = CateModel()
        
    sql = "update cate set cname=%s where id=%s"
    params = ('测试中12132132',16)
    print cateModel.editCate(sql,params)
    
        
    
    
    





if __name__ == '__main__':
    main()