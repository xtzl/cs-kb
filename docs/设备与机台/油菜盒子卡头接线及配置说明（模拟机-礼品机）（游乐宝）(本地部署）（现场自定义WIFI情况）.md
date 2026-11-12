---
title: 油菜盒子卡头接线及配置说明（模拟机/礼品机）（游乐宝）(本地部署）（现场自定义WIFI情况）
category: 设备与机台
tags: 
source: KMS
updated: 2024-09-02
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81490676e700191b14556647666.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准 / 卡头类（刷卡终端）
author: 梁建宁
kms_id: 00001869
---

# 一、 作业说明

新到场地的盒子要与场地系统连接，就要安装接线与配置，下列为油菜盒子的安装说明

# 二、卡头外观

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1454e597652&type=med)

# 三、作业准备

### 工具准备

1.扎带（若干）

2.3M双面胶

*注意：工具准备清单目录请参考：链接

### 网络准备

第三方网络设备请参考此文档进行配置《第三方网络配置要求》

### 系统准备

游乐宝系统版本升级为8.1.6842以上版本

# 四、 注意事项

1.卡头安装前，必须机台处于断电情况；

# 五、固定标准

1.油菜盒子内置在机台里面，并且通过扎带或者双面胶固定在机台内部

2.油菜盒子的天线，尽量外置摆放，并且保持垂直，部分特殊机台无法外置情况下，也要保证油菜盒子天线垂直并且不与机台内壁接触。

3.接线后，线路需要整理梳理好，用扎带固定，且要求不能影响机台正常功能，包括不影响调试机台、回收硬币，打开检修口等操作。

# 六、接线标准

## 1.油菜盒子认识

油菜盒子的样式图，如图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1454e617653&type=med)

## 2.油菜盒子线材认识

线材样式图，如图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1454e6a7654&type=med)

线材说明：

黄色线--电源12V线；

黑色线--地线；

灰色线--投币输出线；

绿色线--投币输入线；

## 3.油菜盒子接线说明

a.按下图对机台线路进行接入，如图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1454e747655&type=med)

b.油菜盒子实际接线说明：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1454e7e7656&type=med)

说明：

假如该机台是接入协议线情况下，不需要再接入其他线材（天线除外），包括投币输入线、投币输出线和礼品线。

反之，如果该机台不支持接入协议，则需要接除协议线外其他线路。

# 七、后台配置说明

## 后台网络配置

### 1.获取场地WiFi信息

如果现场网络设备并非使用标准网络设备情况下，则需要提前了解现场无线网络是否符合使用要求。

要求如下：

①无线名称和密码必须不含有中文和符号

②给予卡头使用的无线网络为2.4G网络，且不能使用双频合一或2.4G和5G设置同一个WIFI名称密码

③无线网络DHCP服务功能需要开启，且自动分配的IP地址数量需要大于现场安装卡头数量，可修改LAN口配置参数中的【子网掩码】来增加地址范围

④DHCP服务中，dns首选需要固定成119.29.29.29，否则可能会影响扫码游戏

⑤无线网络中的WIFI加密方式为WPA-PSK/WPA2-PSK

### 2.配置通用配置卡二维码

路径如下：

后台→设备→基础设置→卡头WIFI通讯设置→通用配置卡

在通用配置卡界面，选择【内场】，并输入本地服务器地址，格式一般为192.168.**.**，端口为9999

若不知道如何查看本地ip地址，可参考以下文档进行查看：

win2012服务器电脑如何查看IP和端口-百度经验 (baidu.com)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1454f5f7657&type=med)

点下一步，输入现场已设置好给予V9卡头使用的无线名称和密码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b145507b7658&type=med)

点击完成后，点一下同步服务器地址到游智云，并将空白卡放置读卡器中，点击【网络参数写入配置卡】中，完成通用配置卡写入。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b14550847659&type=med)

注意：通用配置卡只需要写入一次即可，后续所有钻石V9卡头、存币机V10均可以使用该配置卡配置

###

### 3.将读卡模块接入到盒子端的【扫码】接口中，并将会员卡放置到读卡模块中，长按盒子的【设置键】5~10秒，等待盒子读取配置信息，等待盒子连接。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b145508c765a&type=med)

###

### 4.油菜盒子连接状态

油菜盒子连接成功，并常亮绿色【电源】【联网】【强度】三个灯，【待机】灯闪烁红灯，证明已经进入带配置模式。如果未显示该灯号，按解绑键5S后，等待待机灯快闪，即可进入配置模式。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b145516c765b&type=med)

## 项目创建、配置及调试

### 1.项目创建

手机连上卡头使用的无线网络，打开手机微信端，用扫一扫，打开手机浏览器，扫描通用配置卡二维码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1455175765c&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b145527d765d&type=med)

进入配置界面，点击【新增】，创建该模拟机/礼品机机台项目类型

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1455287765e&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b1455366765f&type=med)

点击项目分类栏，在弹窗点击刚创建的模拟机/礼品机-机台类型

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b145547f7660&type=med)

补充填写该项目信息，完善项目资料，录入完成后点击保存，创建完成。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b14554897661&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b145549d7662&type=med)

### 2.卡头关联绑定项目

点击添加端口，在跳转界面输入 卡 头显示的编号，点击提交

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b14555807663&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191b14555897664&type=med)

# 八、测试要求

#### 投币信号匹配测试

使用实物币投币，机台能正常启动，并且后台【项目消费查询】能查询到对应投币数据，连续测试10次，均为正常代表测试通过；

#### 礼品信号匹配测试

将礼品扔到出礼品口，模拟出礼品过程，机器显示中奖，油菜花后台记录【出礼品查询】，则完成礼品测试过程；

#### 投币信号高低电平匹配测试

机台断电，等30秒后上电，机台上电后，机台报错误，则代表参数设置正常；

#### 扫码游戏功能测试

通过微信扫码，选择已设置的扫码游戏方案，会员扣除储值数与机台上币数一致。

# 九、 常见问题

WIFI信号弱

答：将天线引出来

计数不准

答：可能性有几种

1.信号弱，盒子会保留累计数据，等待信号恢复一定强度后再一次性上传，此时系统记录的时间是上传时间并不是实际游玩时间

2.投币信号电平不对，调整盒子电平

3.礼品线线序错，可手动改线调整线序

<
