# encoding: utf-8
import re
import requests
from bs4 import BeautifulSoup
import scrapy
from scrapy.http import Request
from jobs.items import JobsItem
import urllib2
import uuid
import time
import random
class jobsSpider(scrapy.Spider):
    name = '58jobs'
    allowed_domains = ["58.com"]
    
    # start_urls = "http://maoyan.com/films?offset="


    def start_requests(self):
        start = 1
        i = 1
        while i<150:
            ua = random.choice(range(150))
            url = ("http://cd.58.com/tech/pn%s/" % str(ua))
            i=i+1
            yield Request(url, self.parse)
        print "数据获取完毕"
    def parse(self, response):
        try:
            headers = {}
            headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"
            
            time.sleep(5)
            item = JobsItem()
            works = BeautifulSoup(response.text, 'lxml').find("div", class_="infolist").find_all("dl")
            for work in works:
                time.sleep(1)
                job_url = work.find('dt').find('a')
                url = job_url['href']
                request = urllib2.Request(url=url, headers=headers)
                response = urllib2.urlopen(request)
                job_html = response.read().decode('utf-8')
                html = BeautifulSoup(job_html, 'lxml')
                
                
                item['id'] = uuid.uuid4()
                item['title'] = html.find('div', class_='item_con pos_info').find('span', class_='pos_name').get_text()
                
                item['salary'] = html.find('div', class_='pos_base_info').find('span', class_='pos_salary').get_text()
               
                item['company'] = html.find('div', class_='subitem_con company_baseInfo').find('p', class_='comp_baseInfo_title').find('a', class_='baseInfo_link').get_text()
                # item['company'] = "asd"
                item['scale'] = html.find('div', class_='subitem_con company_baseInfo').find('p',class_='comp_baseInfo_scale').get_text()
               
                
                item['address'] = html.find('div', class_='subitem_con work_adress').find('p',class_='detail_adress').get_text()
                item['city'] = u"成都" 

                yield item
        except Exception, e:
            print e.message

            
