# weiboPics
抓取新浪微博某条信息的所有图片评论


最近微博很火的知名时尚博主colouration，举办了多个比赛，如大长腿、美臀、锁骨、小蛮腰等比赛。各妹子纷纷参加，看得我眼花缭乱。可是由于尺度问题，大长腿、美臀、锁骨等比赛的图片被博主删除了。看到有小蛮腰比赛，本人就试着下载下来，于是编程来实现吧。

一、主要问题及思路：
1、模拟登录新浪微博
登录新浪微博不太容易，如果自己写模拟登录的代码，需要花一番功夫。还好有selenium，本人本着偷懒的原则，果断选择，简单轻松地实现登录。
selenium是一个用于Web应用程序测试的工具，能直接运行在浏览器中,就像真正的用户在操作一样。
安装介绍见Python爬虫环境常用库安装 - 天涯笨熊的博客 - CSDN博客；使用介绍见selenium用法详解 - 天涯笨熊的博客 - CSDN博客。

2、找到待抓取的微博，不断抓取其评论图片。
过程：（1）获取评论第一页内的图片链接，并下载
          （2）找到下一页地址
          （3）获取该页内的图片链接，并下载，转到（2）。
          
          
详细介绍请看https://zhuanlan.zhihu.com/p/48463531
