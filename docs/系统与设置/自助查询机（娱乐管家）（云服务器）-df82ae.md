---
title: 自助查询机（娱乐管家）（云服务器）
category: 系统与设置
tags: 
source: KMS
updated: 2024-08-23
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81490676e7001917dda2e007e91.html
section: 现场实施知识库
toc_path: 现场实施知识库
author: 梁建宁
kms_id: 00001842
---

# 一、文档说明

顾客可在设备上，查询项目的游玩时间，并支持超时补费，补费后在免费时间内，可以刷闸机离场。需要配合闸机共同使用，一般查询机放置在游玩项目内部，方便顾客随时随地可以通过查询机查询游玩时长和扣费情况。

仅支持娱乐管家系统，不支持游乐宝系统。

# 二、产品外观

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917d43d6d27d28&type=max)

# 三、功能支持
1.支持查询消费情况，可显示入场时间、游玩时长、计费规则和超时时长、超时费用等信息；
2.支持微信支付宝直接付超时时长费用；

3.支持设置付款后多长时间出闸不额外收费；

# 四、工具准备

1.冲击钻*1、14mm冲击钻钻头*1

2.铁锤*1

3.12mm扳手*1

4.2mm一字螺丝*1

5.记号笔*1

6.十字螺丝刀4mm*1

7.六角螺丝刀*1套

# 五、配件说明

人脸识别面板*1

立式验票桩柱子*1

12mm膨胀螺丝*4（一个主机配4个膨胀螺丝）

电源适配器*1

58mm打印纸*1

# 六、前期准备

1.安装位置需要预留220V电源

2.安装刷卡位置需要预留网线

# 七、安装要求：

1. 自助查询机安装到地面不摇晃；

2. 安装后功能能正常使用（刷卡功能正常、扫码功能正常、屏幕显示正常、打印功能正常）

# 八、注意事项

1.安装前需要确保电源是断电状态

2.安装时需要佩戴手套，以免因五金件锋利导致弄伤手

3.固定自助查询机底部前，需要提前与现场确定底部是否有电源线管或者供暖水管，以免打膨胀螺丝时将管路打穿。

# 九、安装步骤

## 自助查询机安装

### 1.硬件安装

1.将自助查询机底部使用膨胀螺丝固定

2.将网线接入到网线接口

3.插入电源线，并进行通电

### 2.接入系统

2.1建立查询机账号

路径：后台→设置→用户管理

点击【+新增用户】，输入新增的账号、姓名、密码，并给予收银权限和勾选收银员权限，点击【确定】完成设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917e54bd2d0039&type=max)

2.2新增查询机终端

路径：后台→终端→收银终端

点击【新增】，并填写终端名称，选择终端类型为【POS机】，点击【确定】完成新增。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917e569694003d&type=max)

2.3绑定终端

自助查询机通电并通网后，服务器地址输入栏-输入相关地址，如域名地址为http://y********.yun.youcaihua.net:88/admin，则在服务器地址一栏填写y********.yun.youcaihua.net:88即可。点击测试连接

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917e2b56197f9e&type=max)

通过测试连接后，输入管理员账号和密码进行授权绑定终端

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917e5b1cfd0051&type=max)

2.4 选择刚刚新增的收银终端，并输入刚刚新增的收银账号及密码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917e5ca0820056&type=max)

2.5 点击登录，完成配置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917e63e43a005e&type=med)

### 3.使用说明

游客过闸开始计时计费后，则可以通过会员卡、会员二维码、票码来读取计费信息，如读取会员信息后，同时存在多张计时票，支持左右滑动查看多张计时票的计费情况

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917e63e443005f&type=med)

2.读取信息成功后，可出示微信支付宝付款款进行付款结算

3.设置结算后不再计费时间，补费后在免费时间内可免费离场

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001917e63a2d0005d&type=max)

# 十、测试流程

1.测试二维码扫码器是否能正确读取票码和会员二维码

2.测试读卡模块是否可以正确读取会员卡信息

3.测试付费后是否可以正确的打印消费小票

<
