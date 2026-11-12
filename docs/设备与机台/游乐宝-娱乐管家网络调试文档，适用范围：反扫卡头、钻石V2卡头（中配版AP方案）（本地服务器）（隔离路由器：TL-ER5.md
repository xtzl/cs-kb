---
title: 游乐宝/娱乐管家网络调试文档，适用范围：反扫卡头、钻石V2卡头（中配版AP方案）（本地服务器）（隔离路由器：TL-ER5120T）
category: 设备与机台
tags: 
source: KMS
updated: 2025-05-20
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a1963f44000196ecf869c8352f.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准 / 卡头类（刷卡终端）
author: 梁建宁
kms_id: 00002009
---

# 一、作业说明

本教程用于本地服务器使用反扫卡头、钻石卡头的场地使用使用，

适用于：

主路由为TL-R476G；

隔离路由为TL-ER5120T

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

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf868c93512&type=med)

## 步骤二：配置主路由器

### 1.把电脑的网线接到主路由器（型号：TL-R476G）LAN口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf868db3513&type=med)

### 2.打开浏览器，并在浏览器中输入tplogin.cn按回车键。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf868e83514&type=med)

### 3.在出现的界面设置路由器的 用户名：admin管理密码：****（已脱敏，请向运维索取） 点击确定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf868f23515&type=med)

### 4.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf868fb3516&type=med)

### 5.跳过快速配置界面

### 6.选择【基本设置】-【WAN设置】-将【接口设置】中的连接方式改为【动态IP】-点击【保存】，如下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869033517&type=med)

### 7.选择【LAN设置】-【接口设置】-将【模式设置】改为“手动”-将【IP地址】设置为“192.168.10.1”-将【子网掩码】设置为“255.255.255.0”-然后点【设置】，按下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf8690f3518&type=med)

### 8.此时可能会出现需要重新进入路由器设置界面，需要等待几分钟等调试电脑重新获取地址即可，如出现无法登录，请将网线拔掉再重新接上等待重新获取IP地址。

### 9.重新使用192.168.10.1，登录到主路由器设置界面，选择【基本设置】-【LAN设置】-【DHCP服务】，开始地址设置为192.168.10.50，结束地址：192.168.10.200，网关设置为192.168.10.1，首选DNS设置为119.29.29.29，如下图所示

说明：DHCP分配网段设置后，油菜花其他需要固定IP的设备，则使用范围外的网段，如柜台碎票机，当需要设置柜台碎票机时，可设置IP地址为192.168.10.201，避免因为固定IP和DHCP中的IP地址冲突。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869223519&type=med)

### 10.选择【AP管理】-【AP设置】-将【AP管理功能】取消掉，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf8692e351a&type=med)

## 步骤三：配置隔离路由器

### 1.拔掉调试电脑网线，将调试电脑网线接入到第二个路由器第四个接口（隔离路由器，型号：TL-ER5120T）

注意：初次设置，必须接入此接口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf86939351b&type=med)

### 2.将自己电脑IP地址固定为192.168.1.2，子网掩码为255.255.255.0，网关留空，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf86940351c&type=med)

### 3.在浏览器中输入【192.168.1.1】按回车键。进入设置界面，并设置用户名和登录密码。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf86949351d&type=med)

### 4.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf86950351e&type=med)

### 5.选择快速配置，并选择下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf86958351f&type=med)

### 6.选择【单WAN口】，并选择下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf8695f3520&type=med)

### 7.选择【动态IP（自动获取）】并点击下一步。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869683521&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869703522&type=med)

### 8.按照下图设置对应的LAN口配置，完成后点击下一步，确认配置后，点击完成

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869783523&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869803524&type=med)

### 10.继续设置【无线服务设置】-新增/编辑已有的无线名称，点 ![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869853525&type=med) ，设置无线名称和密码

无线名称设置为YocartoonNet0，也可以设置自定义无线名称，无线名称不支持中文或者符号。

加密方式选择 WPA-PSK/WPA2-PSK

无线密码：设置为****（已脱敏，请向运维索取），其中****设置为门店编码前4位

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf8698c3526&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869943527&type=med)

### 11.设置此无线名称对应的射频，点击 ![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf8699c3528&type=med) ，对射频进行设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869a53529&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869ac352a&type=med)

### 12.设置完毕后，在卡头写配置卡的界面，设置对应的WIFI名称和密码，网段类型选择子网地址，并填入对应的服务器地址即可写配置卡。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869b5352b&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869bc352c&type=med)

# 常见问题

1.点击快速配置时，提示绑定TP-LINK商云平台界面，无法继续下一步该怎么办？

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ecf869c5352d&type=med)

答：显示此界面，证明此路由已经做过端口设置，无法使用快速配置，解决方法是直接重置路由器再进行配置。

<
