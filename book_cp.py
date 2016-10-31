#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Filename: book_cp.py
#--------------------
#Function description:
#
#--------------------
#Date:2016-10-31
#--------------------

import os
import logging
import filecmp
import shutil
import sys

#日志设置，用于纠错
LOG_FILENAME = 'logging_book_cp.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s',
                    datefmt='%a,%Y %b %d %H:%M:%S',
                    filemode='w',
                    )
                    
def autoBackup(scrDir, dstDir):
    if ((not os.path.isdir(scrDir)) or (not os.path.isdir(dstDir)) or (os.path.abspath(scrDir)!=scrDir) or (os.path.abspath(dstDir)!=dstDir)):
        usage
    for item in os.listdir(scrDir):
        scritem = os.path.join(scrDir,item)
        dstitem = scritem.replace(scrDir,dstDir)
        if os.path.isdir(scritem):
            #创建新增的文件夹，保证目标文件夹的结构和原始文件夹一致
            if not os.path.exists(dstitem):
                os.makedirs(dstitem)
                print 'make directory:'+dstitem
            autoBackup()
        elif os.path.isfile(scritem):
            #只复制新增或修改过的文件
            if ((not os.path.exists(dstitem)) or (not filecmp.cmp(scritem, dstitem, shallow=False))):
                shutil.copyfile(scritem, dstitem)
                print 'file:'+scritem+'==>'+dstitem

def usage():
    print 'scrDir and dstDir must be existing absolute path of certain directory'
    print 'For example:{0} c:\\olddir c:\\newdir'.format(sys.argv[0])
    sys.exit(0)
    
if __name__=='__main__':
    if len(sys.argv)!=3
        usage
    scrDir, dstDir = sys.argv[1], sys.argv[2]
    autoBackup(scrDir, dstDir)
