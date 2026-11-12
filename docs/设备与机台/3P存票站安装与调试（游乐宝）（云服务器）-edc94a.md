---
title: 3P存票站安装与调试（游乐宝）（云服务器）
category: 设备与机台
tags: 
source: KMS
updated: 2024-06-26
url: https://kms.gzych.vip/webdoc/view/Pub2c93a8148c3e04c2019053817c265499.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准 / 自助设备
author: 梁建宁
kms_id: 00001773
---

# 一、作业说明

本说明为3P存票站安装方法与调试说明。

# 二、产品外观

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053816e0c547e&type=med)

# 三、作业准备

1.提前在3P存票站安装位置预留网线和电源线；

3.检查柜台碎票机配件是否齐全，包括进票口五金件(柜台碎票机V8)、钥匙、备用刀组、清票刚尺、电源线。

2.准备读卡器*1，空白会员卡*1

3.准备网线一根。

4.准备一些彩票用于测试。

5.提前准备云服务器的域名地址以及机台端口，一般格式为：y********.yun.youcaihua.net:88/admin，机台端口可找油菜花实施组负责人获得。

# 四、注意事项

1.安装前一定要和客户确认3P存票站机放置位置。一般为靠墙位置。

2.由于部分金属件较为锋利，建议带上手套放置刮伤

3.安装配件，挪动时，必须确保碎票机在断电状态

4.安装后，需要检查保险开关是否处于正常状态，在存票状态电机转动情况下，打开面板，电机必须是停止转动的状态。如果保险功能失灵，请务必不能使用，并及时返修。

# 五、作业标准

1.网络连接正常，断电开机不出现掉线情况。

2.所有配件已经安装到位。

3.连续碎票10次不出现卡票情况。

4.连续碎票20张票，计数准确无误。

# 六、作业步骤

## 固定安装

3P存票站位置确认后，需要把滚轮上的地脚扭下来，使存票站稳固放置在地面

## 系统后台配置

### 后台创建碎票机项目

1.登录游乐宝后台，新建一个碎票机项目：

路径：【设置】-【设备管理】-【营业设备】-【新增】-【碎票机】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053816e15547f&type=med)

2.填写碎票机的设备名称，点击【保存】。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053816eee5480&type=med)

3.找到刚创建成功的碎票机项目，点击右边的【端口管理】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053816fd25481&type=med)

4.点击【添加端口】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190538170de5482&type=med)

5.点击【保存】，重复上一步工作，添加3个端口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190538171b65483&type=med)

6.点击【刷卡】，跳转到配置卡信息填写界面；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190538171c15484&type=med)

## 写配置卡

### 路由器密码设置

若知道路由器密码，可直接进行设置，

若不知道，则可随意编辑设置；

展示如下：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190538171cb5485&type=med)

### 填写配置卡信息

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190538172e15486&type=med)

1.在生成设置卡界面，填写配置卡信息，分别录入以下信息：

- 服务器通讯方式：勾选外网；

- 服务器域名地址：输入门店域名地址，如y********.yun.youcaihua.net；

注意：域名地址不需要填末端的88，只需要到net结束，域名地址由销售助理提供

- 机台端口：输入四个数字的机台端口，

由于机台端口每个门店都不一样，请咨询值班技术获取

- IP地址：请填写本碎票机使用的IP地址，根据现场提供的网线的IP地址来填写；

- 网关：填写本碎票机使用的IP地址所对应的网关，根据现场提供的网线的IP地址来填写；

若不知道如何查找网络ip地址或网关，可用笔记本电脑接入碎票机预留网线，参考下述文档进行查找判断：

怎么查看自己电脑网关和ip地址？_百度知道 (baidu.com)

比如，笔记本电脑获取到的一个ip地址为：

ip地址：192.168.110.20

子网：255.255.255.0

网关：192.168.110.1

则可以给碎票机分配为

IP地址：192.168.110.* （*号代表2~254之间的任意数字）

子网：255.255.255.0

网关：192.168.110.1

此时，在通过电脑运行cmd命令行，并尝试用ping 准备给碎票机分配的地址，看看有没有连接，如果没有任何设备连接，则代表此IP可以用；例如你想分配给碎票机192.168.110.241，则用ping来测试，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190538172ed5487&type=med)

注意：如果发现地址已经被占用，则需要再次跟换地址，直到不被占用为止，建议使用ip地址段200-250之间的地址会比较好。

2.上述信息填写录入完成后，将读卡器接入电脑，将准备好的空白会员卡放在读卡器上，点击【保存并写入卡中】，配置卡配置完成。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190538173c15488&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190538173cc5489&type=med)

## 3P存票站读取配置卡信息

1.打开3P存票站，找到内部主板，在主板上找到下图的按钮长按5~10秒

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c20190537f50445479&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c201905804a8a96281&type=max)

2.把配置卡放到读卡卡头区域，然后等待片刻就可以完成配置，展示如下：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c201905805afd06288&type=max)

3.配置成功，碎票机显示界面如下：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c201905805d9b66289&type=max)

4.其他2个碎票位置按照此方法重复操作配置即可。

# 七、设备测试

## 读卡碎票测试

1.将会员卡防止【刷卡】位置，检查屏幕是否正确读取出会员卡卡内彩票数；

2.将20~40张彩票放置到碎票口进行碎票，检查碎票数量和存入数量是否一致。

## 反扫测试

将会员二维码放置在反扫口进行读取，测试是否能正常读取会员，并且尝试碎票20张，保存后在小程序中是否能看到存票记录。

# 八、配件使用说明

## 1. 钢尺

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053817993548f&type=med)

#### 使用方法：

当碎票机卡票时，可打开碎票机的档板，用钢尺直接捅入进票口，连续多次捅入，一般可以快速解决

## 2. 光眼、胶圈

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053817ac95493&type=med)

#### 使用说明：

- 胶圈用于替换压票滚轮位置的胶圈。

- 光眼用于替换感应光眼用。

以上设备都是易损件，当使用时间较长的情况下，可能出现损耗，损耗后可自行更换

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053817ad35494&type=med)

## 3. 备用刀组

#### 使用说明：

碎票机内部有备用刀组，当原刀组已经磨损消耗较为厉害，并且出现票已经切不断卡顿的情况，此时需要更换备用刀组。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053817add5495&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053817ae85496&type=med)

# 九、常见问题

1.3P存票站上出现E25是什么原因？

答：连接不上服务器，检查配置卡IP及服务器IP是否正常。

2.扫码登录直接退出

答：保存按键短路

3.经常显示断线

答：

a.更换ip再刷配置卡

b.更换网线

c.主板出现问题

4.碎票会减票

答：清理光眼或者更换光眼

5.存票的时候没有成功

答：重启碎票机是否显示A802报错，机台碎票机端口冲突

6.连接显示E50-E33

答：

a.路由器DNS填上119.29.29.29，一般在DHCP服务器设置中找到该配置，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2019053817af45497&type=med)

b.路由器开启DHCP功能

c.在系统上填写域名地址不要加http://和结尾的端口号（如:88）

d.联系运维检查域名连接端口是否正常

7.屏幕显示FULL

答：碎票已满，需要更换底部的碎票垃圾桶

<
