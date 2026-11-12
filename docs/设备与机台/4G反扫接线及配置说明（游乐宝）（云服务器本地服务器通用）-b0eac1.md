---
title: 4G反扫接线及配置说明（游乐宝）（云服务器本地服务器通用）
category: 设备与机台
tags: 
source: KMS
updated: 2024-05-17
url: https://kms.gzych.vip/webdoc/view/Pub2c93a8148c3e04c2018f851b91d358ec.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准 / 卡头类（刷卡终端）
author: 梁建宁
kms_id: 00001720
---

# 一、作业说明

新到场地的盒子要与场地系统连接，就要安装接线与配置，下列为4G盒子的安装说明，4G盒子本身同时支持游乐宝/娱乐管家系统以及芸苔系统，本说明针对游乐宝系统来调试。

# 二、外观说明

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b860758cc&type=med)

# 三、作业准备

### 工具准备

1.扎带（若干）

2.3M双面胶

*注意：工具准备清单目录请参考：链接

### 系统准备

1.游乐宝系统版本升级为8.1.6842以上版本

2.本地部署需要开通云互联功能，此卡头只支持域名连接

3.扫码游戏，需要开通盈客宝小程序（微聆不支持4G盒子扫码游戏功能）

# 四、注意事项

1.卡头安装前，必须机台处于断电情况；

2.安装后，需要及时清理残渣。

3.4G盒子较为依靠4G网络信号，天线部分需要尽可能外置在机器外部

# 五、安装标准

1.4G盒子内置在机台里面，并且通过扎带或者双面胶固定在机台内部

2.4G盒子的天线，尽量外置摆放，并且保持垂直，部分特殊机台无法外置情况下，也要保证4G盒子天线垂直并且不与机台内壁接触。

3.接线后，线路需要整理梳理好，用扎带固定，且要求不能影响机台正常功能，包括不影响调试机台、回收硬币，打开检修口等操作。

# 六、调试作业

## 线材认识

1.投币器接盒子投币输入端线

2.机台投币信号接盒子投币输出端线

3.礼品信号线

4.协议线（非标配）

5.天线

6.反扫模块灯光线和扫码线

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b871358cd&type=med)

## 接线说明

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b871e58ce&type=med)

### 1.从机台中引出投币信号线，接入到盒子端投币输出。（如果接协议线则不需要）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b87fd58cf&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b883c58d0&type=med)

### 2.盒子线材中标记为【投币器】的一段接入到投币器，另一端标记为【投币输出盒子端】接入到盒子中的投币输入（如果接协议线则不需要）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b884658d1&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b885058d2&type=med)

### 3、礼品线接入

将礼品线接入到盒子礼品口，另外一段对接礼品线

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b885a58d3&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b886358d4&type=med)

注意：如果接线测试后发现礼品信号采集失败，可能需要手工改线，部分机台礼品信号线和地线是反的。

### 4、天线接入

将天线一段接入到盒子中，另外一端外置到机台外部

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b886e58d5&type=med)

### 5.反扫模块接入

反扫模块中的灯光线接入到盒子灯光为止

反扫模块中的

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b887958d6&type=med)

## 调试说明

### 1.机台通电，等待盒子端联网，联网成功工正常为3绿常亮1红闪烁（电源、联网和强度为绿色灯，待机为红色闪烁）

### 2.登录后台，依次进入路径：后台→设备→基础设置→卡头WiFi通讯设置→重新设置通讯网络

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b888358d7&type=med)

### 3.配置现场网络基础信息，如下图所示配置

选择外场→输入服务器域名地址→下一步→无线名称和密码忽略不需要修改→直接点完成→点服务器地址同步到游智云

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b899a58d8&type=med)

注意：此处必须填写域名地址，如门店使用的是本地服务器，需要联系销售助理开通域名地址功能才能使用。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b89aa58d9&type=med)

注意：这里的无线名称和密码忽略不用修改

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8a8e58da&type=med)

注意：这里务必点同步，否则有可能引起异常。

### 4.再次扫配置码进入配置界面（注意，虽然这里提示请勿使用微信扫一扫，但是新版已经支持微信扫一扫使用）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8a9a58db&type=med)

### 5.项目创建

打开手机微信端，用扫一扫，打开手机浏览器，扫描通用配置卡二维码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8aa658dc&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8b8a58dd&type=med)

进入配置界面，点击【新增】，创建该模拟机机台项目类型

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8b9558de&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8c7a58df&type=med)

点击项目分类栏，在弹窗点击刚创建的模拟机-机台类型

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8d9058e0&type=med)

补充填写该项目信息，完善项目资料，录入完成后点击保存，创建完成。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8d9c58e1&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8ea658e2&type=med)

### 6.卡头关联绑定项目

点击添加端口，在跳转界面输入 卡 头显示的编号，点击提交

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b8eb258e3&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b900058e4&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b900b58e5&type=med)

# 七、测试要求

####

#### 投币信号匹配测试

将会员卡放到卡头手上读取，卡头能显示卡内余额，并在1秒内扣除余额，机台上对应的币数，机台自带码表正常增加扣币数量则代表投币信号正常无异常；

#### 礼品信号匹配测试

将礼品扔到出礼品口，模拟出礼品过程，机器显示中奖，油菜花后台记录出礼品数，则完成礼品测试过程；

#### 投币信号高低电平匹配测试

机台断电，等30秒后上电，机台上电后，机台和卡头无报错误代码，则代表参数设置正常；

#### 网络信号通讯测试

连续刷卡5次，每次读取速度不高于1秒，同一张卡刷卡保护和后台设置间隔一致，则代表网络正常；

#### 反扫功能测试

通过会员二维码给反扫卡头读取，卡头能正常扣除币值，机台能正常启动，反扫模块工作正常。

# 八、常见问题：

1.如果需要解绑重连，可长按盒子端解绑按钮5~10秒进行解绑

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b90e058e6&type=med)

2.如果盒子出现异常，可长按盒子设置键5~10秒，然后断电再上电进行重置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b90ea58e7&type=med)

3.连接完毕后，出现重启后多上币，或者机台报卡币，可尝试调试盒子上的常开常闭设置，一般以机台中投币器的NO/NC进行设置，原来是NO则对应就是常开信号，反之常闭。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b90f458e8&type=med)

4.如果机台投币后机器不启动，请检查机器信号线电压，并在下图中位置调整信号线电压。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b90fd58e9&type=med)

5.打开盒子后，LED显示板会现场错误代码，含义如下：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f851b910758ea&type=med)

H4 连接测试游智云

H5 注册游智云

H6 检测更新

H7 获取绑定信息

H8 等待绑定

<
