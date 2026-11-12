---
title: 游乐宝/娱乐管家网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（高配版）（本地服务器）（隔离路由器：TL-ER5120T）
category: 设备与机台
tags: 
source: KMS
updated: 2025-05-20
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a1963f44000196ed1e7f433658.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准 / 卡头类（刷卡终端）
author: 梁建宁
kms_id: 00002010
---

# 一、作业说明

本教程用于本地服务器使用油菜盒子的场地使用，设备清单如下：

主路由：TP-LINK TL-ER5120T

隔离路由器：TP-LINK TL-ER5120T

AC控制器：TL-AC100

建议卡头数量大于200上且少于500个以下使用

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

1.网络接线，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e263635&type=med)

## 步骤二：主路由设置

### 1.将调试电脑网线接入到第二个路由器第四个接口（隔离路由器，型号：TL-ER5120T）

注意：初次设置，必须接入此接口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e2e3636&type=med)

### 2.将自己电脑IP地址固定为192.168.1.2，子网掩码为255.255.255.0，网关留空，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e363637&type=med)

### 3.在浏览器中输入【192.168.1.1】按回车键。进入设置界面，并设置用户名和登录密码。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e3d3638&type=med)

### 4.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e433639&type=med)

### 5.选择快速配置，并选择下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e4c363a&type=med)

### 6.选择【单WAN口】，并选择下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e54363b&type=med)

### 7.根据实际现场的WAN口接入情况，选择连接方式，并点击下一步。

情况说明：

情况一：上联网络（WAN口网线）是光猫，且需要输入账号密码的情况，则这里需要选择PPPOE连接（xDSL虚拟拨号），并按照提示输入对应的账号密码

情况二：上联网络（WAN口网线）是光猫路由器或者有其他路由器分出来的网线，直接接该网线则可以直接获取IP地址上网，这种情况则选择动态

情况三：上联网络（WAN口网线）是商场提供的专网，需要固定IP才能上网，此情况则需要使用静态IP，并固定商场提供的IP地址信息

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e5d363c&type=med)

### 8.按照下图设置对应的LAN口配置，完成后点击下一步，确认配置后，点击完成

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1acf31362a&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1b81ba362c&type=max)

## 步骤三：隔离路由器设置

### 1.拔掉调试电脑网线，将调试电脑网线接入到第二个路由器第四个接口（隔离路由器，型号：TL-ER5120T）

注意：初次设置，必须接入此接口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e68363d&type=med)

### 2.将自己电脑IP地址固定为192.168.1.2，子网掩码为255.255.255.0，网关留空，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e72363e&type=med)

### 3.在浏览器中输入【192.168.1.1】按回车键。进入设置界面，并设置用户名和登录密码。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e7b363f&type=med)

### 4.路由器跳转到管理界面后， 输入刚才设置的用户名和密码进入管理界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e843640&type=med)

### 5.选择快速配置，并选择下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e8d3641&type=med)

### 6.选择【单WAN口】，并选择下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e963642&type=med)

### 7.选择【动态IP（自动获取）】并点击下一步。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7e9e3643&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7ea73644&type=med)

### 8.按照下图设置对应的LAN口配置，完成后点击下一步，确认配置后，点击完成

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1d9a1b3632&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7eae3645&type=med)

## 步骤四：调试AC控制器

1.拔掉调试电脑网线，将调试电脑网线接入到AC控制器（AC控制器型号：AC-100）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7eb63646&type=med)

2.在电脑打开网页，并输入地址10.0.0.253，进入界面（如果无法进入，请尝试将电脑IP固定为192.168.1.100，固定IP的方法如下：https://jingyan.baidu.com/article/a17d5285fba7dac199c8f222.html IP固定完毕后，在网页输入192.168.1.253，进入界面）

3.第一次登录提示需要设置账号及密码，账号设置为：admin密码设置****（已脱敏，请向运维索取）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7ebf3647&type=med)

4.设置完毕后，用新的账号密码重新登录进去设置界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7ec73648&type=med)

5.先设置AC控制器的IP地址，选择【网络设置】-【接口设置】，设置ip地址，点【设置】

IP地址设置为10.0.0.253

子网掩码：255.255.0.0

网关10.0.0.1

DNS为119.29.29.29 和223.5.5.5

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7ed13649&type=med)

6.保存后，调试电脑会断开连接，此时需要把电脑固定IP重新设置为自动获取IP，等待片刻后可以通过10.0.0.253重新访问到设置界面

7.设置AP分配地址，进入【网络设置】-【IP地址分配】-选择【仅为AP分配】并按照下图设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7eda364a&type=med)

8.选择【无线管理】-【无线服务】，并修改第一个无线网络，点

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7ee2364b&type=med)

进入设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7eeb364c&type=med)

9.登录油菜花后台系统

游乐宝路径为：【后台】-【设备】-【基础设置】-【卡头wifi通讯设置】-【通用配置卡】-【重新设置网络通讯】-选择【内场】并填入门店本地IP地址-【下一步】-【生成自动连接wifi】-并复制对应的wifi名称和密码

娱乐管家路径为：【后台】-【终端】-【卡头wifi通讯设置】-【通用配置卡】-【重新设置网络通讯】-选择【内场】并填入门店服务器IP地址-【下一步】-【生成自动连接wifi】-并复制对应的wifi名称和密码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7ef4364d&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7efb364e&type=med)

10.修改SSID、安全选项和PSK密码，点【确定】，设置如下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7f05364f&type=med)

11.将其他无用的无线网络禁用掉，如下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7f0d3650&type=med)

12.点

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7f163651&type=med)

进入射频绑定界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7f1f3652&type=med)

13.勾选5G频段，然后点绑定（注意，如果此位置没有获取到AP列表，可重启整体网络之后再进去设置）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7f273653&type=med)

14.再次打开AC控制器，找到【射频设置】，选择【射频调优】，并设置频段宽带为20MHz，点击【设置】并点立即调优

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7f2f3654&type=med)

## 步骤五：检查卡头连接状态

1.设置完毕后，魔方卡头V9和钻石V9卡头会自动连上该网络，并提示联网成功，扫码绑定门店，此时网络设置已经完成

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7f373655&type=med)

# 常见问题

1.点击快速配置时，提示绑定TP-LINK商云平台界面，无法继续下一步该怎么办？

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000196ed1e7f403656&type=med)

答：显示此界面，证明此路由已经做过端口设置，无法使用快速配置，解决方法是直接重置路由器再进行配置。

<
