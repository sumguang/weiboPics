# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:54:59 2018

@author: andy
"""

from selenium import webdriver
import time
import urllib
import random

def auto_down(url,filename):
    try:
        urllib.request.urlretrieve(url,filename)
    except urllib.ContentTooShortError:
        print('Network conditions is not good.Reloading.')
        auto_down(url,filename)


def browser_proxy():
    chromeOptions = webdriver.ChromeOptions()

    # 设置代理
    chromeOptions.add_argument("--proxy-server=http://127.0.0.1:8087")
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    browser = webdriver.Chrome(chrome_options = chromeOptions)
    return browser


class CrawelPic:
    def __init__(self,username,password):
        #self.browser= webdriver.Chrome()
        self.browser=browser_proxy()
        self.num=1
        self.username=username
        self.password=password
        
    def login(self,url):
        self.browser.get(url)
    
        time.sleep(2)
    
        user=self.browser.find_element_by_id("loginName")
        pwd=self.browser.find_element_by_id("loginPassword")
        user.send_keys(self.username)
        
        pwd.send_keys(self.password)


        submit_btn=self.browser.find_element_by_id("loginAction")
        submit_btn.click()
    
        print("Pleare input Codes")
    
        time.sleep(10)
    
    #获取页面内的所有图片链接
    def getPicUrlsFromPage(self,initurl):
        self.browser.get(initurl)
        
        #经查看图片元素，发现图片链接在类名ctt内。该函数找到ctt名类的所有
        comments=self.browser.find_elements_by_class_name("ctt")
        picUrls=[]
        #获取图片链接
        for x in comments:
            pic_temp=x.text.split(" ")[-1]
            if("http" in pic_temp):
                picUrls.append(pic_temp)
    
        #下一页地址
        nextPageUrl=""
        try:
            nextPage=self.browser.find_element_by_xpath("//a[text()='下页']")
            nextPageUrl=nextPage.get_property('href')
        except :
                print("There is no pages moer!")

           
        return picUrls,nextPageUrl





    def getPic(self,url):
        #打开图片短地址
        self.browser.get(url)
        try:
            #获取图片的真正地址
            img=self.browser.find_element_by_xpath("//img").get_property('src')
            print("We are downloading "+img)
            #print("Download the" +num +" pics")
            print(self.num)
            #下载该图片，并为它命名
            auto_down(img, '%s.jpg' %self.num)
            self.num=self.num+1
            time.sleep(random.randint(3,6))
        
        except:
        
            print("there is a error, need to re-login")
            time.sleep(15)
            return 1
        return 0
    




    def getPics(self,urls):
    
        for url in urls:
        
            if(self.getPic(url)):
                time.sleep(60)
                self.getPic(url)
        return 0
        
        
            
    
    
if __name__ == "__main__":
    yao=CrawelPic("微博用户名","密码")
    
    url="https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt="
    yao.login(url)
    
    
    
    #initUrl="https://weibo.cn/comment/H0Q0BivZE?uid=5998187176&rl=0#cmtfrm"
    #热门图片
    initUrl="https://weibo.cn/comment/hot/H0Q0BivZE?rl=1"
   
    yao.num=1
    while(True):
        
        time.sleep(random.randint(10,20))
    
        x,y=yao.getPicUrlsFromPage(initUrl)
    
    
        print("This page has pics:")
        print(x)
        yao.getPics(x)
   
    
        if(y):
            print("next page is:" +y)
            initUrl=y
        else:
            break
    
            





    
    
