# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
from jobs import settings
import sys

from jobs.items import JobsItem
MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
MYSQL_charset = settings.MYSQL_utf8
cnx = pymysql.connect(host=MYSQL_HOSTS, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, port=MYSQL_PORT,charset = MYSQL_charset)
cur = cnx.cursor()


class JobsPipeline(object):
    def process_item(self, item, spider):
        
        

        try:
            sql = "SELECT * FROM jobs WHERE title = '%s' and city = '%s' and company = '%s'" % (item['title'], item['city'],item['company'])

            cur.execute(sql)
            result = cur.fetchall()
            if len(result) > 0:
                print "already exist."
                pass
            else:
                id = str(item['id'])
                title = item['title']
                salary = item['salary']
               
                company = item['company']

                scale = item['scale']
             
                address = item['address']
                city = item['city']
                cur.execute(
                    'insert into jobs(id,city,title,salary,company,scale,address) values(%s,%s,%s,%s,%s,%s,%s)',
                    (id, city,title, salary, company, scale, address))

                print "insert one infomation"
                cnx.commit()
        
                return item
        except Exception, e:
                print e.message 
