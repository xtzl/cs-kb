---
title: 游乐宝/娱乐管家网络调试文档，适用范围：反扫卡头、钻石V2卡头（中配版AP方案）（本地服务器）
category: 设备与机台
tags: 
source: KMS
updated: 2023-02-24
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81485aecc240186829586484e99.html
section: 网络调试安装
toc_path: 现场实施知识库 / 网络调试安装
author: 梁建宁
kms_id: 00000428
---

# 一、作业说明

本教程用于本地服务器使用反扫卡头、钻石卡头的场地使用使用，

适用于：

主路由为TL-R476G；

隔离路由为TL-ER3210G型号的指导教程。

卡头数量大于100且小于200个

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

## 步骤一：网络设备接线

### 1.网络接线，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829547e94e7e&type=med)

## 步骤二：配置主路由器

### 1.把电脑的网线接到主路由器（型号：TL-R476G）LAN口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829547f54e7f&type=med)

### 2.打开浏览器，并在浏览器中输入tplogin.cn按回车键。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829547fd4e80&type=med)

### 3.在出现的界面设置路由器的 用户名：admin管理密码：****（已脱敏，请向运维索取） 点击确定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548064e81&type=med)

### 4.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc2401868295480f4e82&type=med)

### 5.跳过快速配置界面

### 6.选择【基本设置】-【WAN设置】-将【接口设置】中的连接方式改为【动态IP】-点击【保存】，如下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548194e83&type=med)

### 7.选择【LAN设置】-【接口设置】-将【模式设置】改为“手动”-将【IP地址】设置为“192.168.10.1”-将【子网掩码】设置为“255.255.255.0”-然后点【设置】，按下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548244e84&type=med)

### 8.此时可能会出现需要重新进入路由器设置界面，需要等待几分钟等调试电脑重新获取地址即可，如出现无法登录，请将网线拔掉再重新接上等待重新获取IP地址。

### 9.重新使用192.168.10.1，登录到主路由器设置界面，选择【基本设置】-【LAN设置】-【DHCP服务】，开始地址设置为192.168.10.50，结束地址：192.168.10.200，网关设置为192.168.10.1，首选DNS设置为119.29.29.29，如下图所示

说明：DHCP分配网段设置后，油菜花其他需要固定IP的设备，则使用范围外的网段，如柜台碎票机，当需要设置柜台碎票机时，可设置IP地址为192.168.10.201，避免因为固定IP和DHCP中的IP地址冲突。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019178c71273700c&type=med)

### 10.选择【AP管理】-【AP设置】-将【AP管理功能】取消掉，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc2401868295482d4e85&type=med)

## 步骤三：配置隔离路由器

### 1.拔掉调试电脑网线，将调试电脑网线接入到第二个路由器（隔离路由器，型号：TL-ER3210G）

### 2.在浏览器中输入tplogin.cn按回车键。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548374e86&type=med)

### 3.在出现的界面设置路由器的用户名：admin管理密码：****（已脱敏，请向运维索取） 点击确定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548404e87&type=med)

### 4.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc2401868295484a4e88&type=med)

### 5.跳过快速设置

### 6.选择【基本设置】-【WAN设置】-连接方式选择“自动获取IP”-点【设置】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548534e89&type=med)

### 7.选择【基础设置】-【LAN设置】-IP地址设置为10.0.0.1，子网掩码设置为255.255.0.0，然后点【设置】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc2401868295485e4e8a&type=med)

### 8.选择【DHCP服务】，点击 ![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548674e8b&type=med) ，对DHCP进行设置，设置如下图所示

开始地址：10.0.10.2；结束地址：10.0.10.250；地址租期：120；网关地址：10.0.0.1；首选DNS：119.29.29.29；备选DNS服务器：223.5.5.5

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548764e8c&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001914a8decf66d4d&type=max)

### 9.选择【AP管理】-【AP设置】-【功能设置】中的启用AP管理功能打开，如下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548884e8e&type=med)

### 10.继续设置【无线服务设置】-新增/编辑已有的无线名称，点 ![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548904e8f&type=med) ，设置无线名称和密码

无线名称设置为YocartoonNet0，也可以设置自定义无线名称，无线名称不支持中文或者符号。

加密方式选择 WPA-PSK/WPA2-PSK

无线密码：设置为****（已脱敏，请向运维索取），其中****设置为门店编码前4位

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548984e90&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001914a8ebef76d54&type=max)

### 11.设置此无线名称对应的射频，点击 ![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548ab4e92&type=med) ，对射频进行设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548b34e93&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548bb4e94&type=med)

### 12.设置完毕后，在卡头写配置卡的界面，设置对应的WIFI名称和密码，网段类型选择子网地址，并填入对应的服务器地址即可写配置卡。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001914a8fef8d6d55&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186829548ce4e96&type=med)

<
