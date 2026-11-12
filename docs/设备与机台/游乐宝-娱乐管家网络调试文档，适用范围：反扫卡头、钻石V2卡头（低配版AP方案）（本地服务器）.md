---
title: 游乐宝/娱乐管家网络调试文档，适用范围：反扫卡头、钻石V2卡头（低配版AP方案）（本地服务器）
category: 设备与机台
tags: 
source: KMS
updated: 2023-03-24
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81485aecc24018712bbc9401fdc.html
section: 网络调试安装
toc_path: 现场实施知识库 / 网络调试安装
author: 梁建宁
kms_id: 00000425
---

# 一、作业说明

本教程用于本地服务器使用反扫卡头、钻石V2卡头的场地使用使用的以下型号设备

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

### 1.网络接线，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba94d41fbd&type=med)

### 2.把电脑的网线接到主路由器（型号：TL-R476G）LAN口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba94de1fbe&type=med)

### 3.打开浏览器，并在浏览器中输入tplogin.cn按回车键。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba94e61fbf&type=med)

### 4.在出现的界面设置路由器的 用户名：admin管理密码：****（已脱敏，请向运维索取） 点击确定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba94f31fc0&type=med)

### 5.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba94fc1fc1&type=med)

### 6.跳过快速配置界面

### 7.选择【基本设置】-【WAN设置】-将【接口设置】中的连接方式改为【动态IP】-点击【保存】，如下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95051fc2&type=med)

### 8.选择【LAN设置】-【接口设置】-将【模式设置】改为“手动”-将【IP地址】设置为“192.168.10.1”-将【子网掩码】设置为“255.255.255.0”-然后点【设置】，按下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba950e1fc3&type=med)

### 9.此时可能会出现需要重新进入路由器设置界面，需要等待几分钟等调试电脑重新获取地址即可，如出现无法登录，请将网线拔掉再重新接上等待重新获取IP地址。

### 10.重新使用192.168.10.1，登录到主路由器设置界面，选择【基本设置】-【LAN设置】-【DHCP服务】，开始地址设置为192.168.10.50，结束地址：192.168.10.200，网关设置为192.168.10.1，首选DNS设置为119.29.29.29，如下图所示

说明：DHCP分配网段设置后，油菜花其他需要固定IP的设备，则使用范围外的网段，如柜台碎票机，当需要设置柜台碎票机时，可设置IP地址为192.168.10.201，避免因为固定IP和DHCP中的IP地址冲突。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191781df9c96cd2&type=max)

### 11.选择【AP管理】-【AP设置】-将【AP管理功能】取消掉，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba951d1fc4&type=med)

### 12.拔掉调试电脑网线，将调试电脑网线接入到第二个路由器（隔离路由器，型号：TP-LINK TL-R479GPE-AC）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95251fc5&type=med)

### 13.在浏览器中输入tplogin.cn按回车键。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba952e1fc6&type=med)

### 14.在出现的界面设置路由器的用户名：admin管理密码：****（已脱敏，请向运维索取） 点击确定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95361fc7&type=med)

### 15.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba953e1fc8&type=med)

### 16.跳过快速配置界面

### 17.选择【基本设置】-【WAN设置】-将【接口设置】中的连接方式改为【动态IP】-点击【保存】，如下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95481fc9&type=med)

### 18.选择【LAN设置】-【接口设置】-将【模式设置】改为“手动”-将【IP地址】设置为“10.0.0.1”-将【子网掩码】设置为“255.255.0.0”-然后点【设置】，按下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95501fca&type=med)

### 19.此时可能会出现需要重新进入路由器设置界面，需要等待几分钟等调试电脑重新获取地址即可，如出现无法登录，请将网线拔掉再重新接上等待重新获取IP地址。

### 20.进入【LAN设置】，找到【DHCP服务】，将DHCP服务开打，开始地址为“10.0.10.2”；结束地址为“10.0.10.254”，网关地址为：“10.0.0.1”，首选DNS服务器：119.29.29.29，备用DNS服务器：223.5.5.5，然后点保存设置。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001914a88aa3e6cff&type=med)

### 21.选择【AP管理】-【AP设置】-将【AP管理功能】勾选上，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95631fcc&type=med)

### 22.选择【AP管理】-【无线网络设置】-将【多频合一】关闭掉

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba956b1fcd&type=med)

### 23.继续选择第一个无线网络设置，如下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95741fce&type=med)

### 24.如下图所示设置

无线名称设置为YocartoonNet0，也可以设置自定义无线名称，无线名称不支持中文或者符号。

AP设备，选择自动绑定所有AP

加密方式选择 WPA-PSK/WPA2-PSK

无线密码：设置为****（已脱敏，请向运维索取），其中****设置为门店编码前4位

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001914a8b57c06d28&type=max)

### 25.点【AP管理】-【射频调优】-【信道调优】选择启用-【2.4G信道集合】改成1.5.9.13,-最后点【设置】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95851fd0&type=med)

### 26.设置完毕后，在卡头写配置卡的界面，设置对应的WIFI名称和密码，网段类型选择子网地址，并填入对应的服务器地址即可写配置卡。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001914a8c00b56d2b&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc24018712ba95971fd2&type=med)

<
