---
title: 游乐宝/娱乐管家网络调试文档，适用范围：油菜盒子（低配版AP方案）（本地服务器）
category: 设备与机台
tags: 
source: KMS
updated: 2023-03-24
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81485aecc24018712c0fa8c2053.html
section: 网络调试安装
toc_path: 现场实施知识库 / 网络调试安装
author: 梁建宁
kms_id: 00000885
---

# 一、作业说明

本教程用于本地服务器使用油菜盒子的场地使用，并使用以下型号设备：

主路由器：TL-R476G

隔离路由器：TP-LINK TL-R479GPE-AC

卡头数量少于等于100个

# 二、作业准备

调试电脑*1台

网线*1根（用于调试使用）

AP已提前挂顶，AP线路连接到机柜中

外网已经通路

标签纸

# 三、注意事项

1.监控网络不要与系统网络共用主路由

# 四、作业标准

1.机柜整洁

2.线路清晰

3.网络平均延迟低于40ms

# 五、设置步骤

## 步骤一：网络接线

### 1.网络接线，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9ec52036&type=med)

## 步骤二：主路由设置

### 1.把电脑的网线接到主路由器（型号：TL-R476G）LAN口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9ecf2037&type=med)

### 2.打开浏览器，并在浏览器中输入tplogin.cn按回车键。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9ed62038&type=med)

### 3.在出现的界面设置路由器的 用户名：admin管理密码：****（已脱敏，请向运维索取） 点击确定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9ee62039&type=med)

### 4.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9ef6203a&type=med)

### 5.跳过快速配置界面

### 6.选择【基本设置】-【WAN设置】-将【接口设置】中的连接方式改为【动态IP】-点击【保存】，如下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9eff203b&type=med)

### 7.选择【LAN设置】-【接口设置】-将【模式设置】改为“手动”-将【IP地址】设置为“192.168.10.1”-将【子网掩码】设置为“255.255.255.0”-然后点【设置】，按下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f0b203c&type=med)

### 8.此时可能会出现需要重新进入路由器设置界面，需要等待几分钟等调试电脑重新获取地址即可，如出现无法登录，请将网线拔掉再重新接上等待重新获取IP地址。

### 9.重新使用192.168.10.1，登录到主路由器设置界面，选择【基本设置】-【LAN设置】-【DHCP服务】，开始地址设置为192.168.10.50，结束地址：192.168.10.200，网关设置为192.168.10.1，首选DNS设置为119.29.29.29，如下图所示

说明：DHCP分配网段设置后，油菜花其他需要固定IP的设备，则使用范围外的网段，如柜台碎票机，当需要设置柜台碎票机时，可设置IP地址为192.168.10.201，避免因为固定IP和DHCP中的IP地址冲突。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191783ac8f76de4&type=med)

### 10.选择【AP管理】-【AP设置】-将【AP管理功能】取消掉，如下图所示

说明：此路由用于管理服务器、收银电脑、办公电脑以及现场的自助设备，所以AP管理不需要开启。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f16203d&type=med)

## 步骤三：隔离路由设置

### 1.拔掉调试电脑网线，将调试电脑网线接入到第二个路由器（隔离路由器，型号：TP-LINK TL-R479GPE-AC）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f24203e&type=med)

### 2.打开浏览器，并在浏览器中输入tplogin.cn按回车键。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f2d203f&type=med)

### 3.在出现的界面设置路由器的 用户名：admin管理密码：****（已脱敏，请向运维索取） 点击确定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f352040&type=med)

### 4.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f3d2041&type=med)

### 5.跳过快速配置界面

### 6.选择【基本设置】-【WAN设置】-将【接口设置】中的连接方式改为【动态IP】-点击【保存】，如下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f472042&type=med)

### 7.选择【LAN设置】-【接口设置】-将【模式设置】改为“手动”-将【IP地址】设置为“10.0.0.1”-将【子网掩码】设置为“255.255.0.0”-然后点【设置】，按下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f512043&type=med)

### 8.此时可能会出现需要重新进入路由器设置界面，需要等待几分钟等调试电脑重新获取地址即可，如出现无法登录，请将网线拔掉再重新接上等待重新获取IP地址。

### 9.进入【LAN设置】，找到【DHCP服务】，将DHCP服务开打，开始地址为“10.0.10.2”；结束地址为“10.0.10.254”，网关地址为：“10.0.0.1”，首选DNS服务器：114.114.114.114，备用DNS服务器：223.5.5.5，然后点保存设置。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f5e2044&type=med)

### 10.选择【AP管理】-【AP设置】-将【AP管理功能】勾选上，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f692045&type=med)

### 11.选择【AP管理】-【无线网络设置】-将【多频合一】关闭掉

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f922046&type=med)

### 12.登录油菜花后台系统

游乐宝路径为：【后台】-【设备】-【基础设置】-【卡头wifi通讯设置】-【通用配置卡】-【重新设置网络通讯】-选择【内场】并填入门店本地IP地址-【下一步】-【生成自动连接wifi】-并复制对应的wifi名称和密码

娱乐管家路径为：【后台】-【终端】-【卡头wifi通讯设置】-【通用配置卡】-【重新设置网络通讯】-选择【内场】并填入门店服务器IP地址-【下一步】-【生成自动连接wifi】-并复制对应的wifi名称和密码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9f9c2047&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f8564ad005c1f&type=med)

### 13.继续回到路由器设置界面，选择第一个无线网络设置，如下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9fa52048&type=med)

### 14.如下图所示设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9fae2049&type=med)

### 15.点【AP管理】-【射频调优】-【信道调优】选择启用-【2.4G信道集合】改成1.5.9.13,-最后点【设置】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712bf9fba204a&type=med)

### 16.设置完毕后，油菜盒子会自动连上该网络，并且电源、联网和强度灯均为绿色灯，待机为红色灯闪烁。

<
