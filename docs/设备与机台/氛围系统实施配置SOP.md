---
title: 氛围系统实施配置SOP
category: 设备与机台
tags: 
source: KMS
updated: 2026-04-20
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a19cff446a019daa6610382d6b.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准 / 卡头类（刷卡终端）
author: 梁建宁
kms_id: 00003051
---

# 文档说明

氛围系统功能核心包含以下内容：影音功能、灯光功能以及彩票竞技赛等相关功能。该功能配置教程说明如下。

# 功能支持

1.支持电视显示控制，可播放视频、图片等功能。

2.支持灯光控制，包括闪烁、流水、常亮等模式选择

3.支持播放背景音乐

4.支持定时广播和插播广播功能，并支持AI文字自动转化成播报语音功能。

5.支持按不同区域划分来展现不同风格的视频、音频、图片、灯光效果等。

6.支持彩票竞技赛。

7.支持展示特定的本地会员任务功能。

8.支持展示大额充值展示功能。

9.支持摇一摇功能。

10.支持播报高级会员到店提醒

11.支持玩家抓到娃娃播报新讯功能

# 氛围系统图链接参考图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019da9d5df01291d&type=max)

# 前期准备

## 客户准备阶段

参考文档如下：

《氛围系统前期准备工作说明》

## 实施安装准备阶段

1.联系销售，开通系统氛围功能

2.升级软硬件版本

娱乐管家：V10.4.2190或以上
边缘网关版本：2026031701以上

影音盒子：V1.1.8以上

抽奖机版本：V1.0.5以上

抽奖机卡头版本：V1.0.0以上
卡头版本：目前只支持钻石V9，V321及以上版本

3.开通氛围设置的账号以及开通游乐掌柜设置功能

# 建议施工时间

工作日白天时间（需要授权开通部分功能）

# 安装调试说明（氛围主机）必要设置

## 第一步，开启系统的氛围系统功能

①联系助理开通对应的氛围系统功能，如果已经确认开通后，将门店编码发送给实施组组长或者其他有权限卡通该功能的人员进行开通

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019da9e134b22978&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019da9e1b4a62979&type=max)

②确认氛围系统的界面是否已经齐全

界面包括【彩票竞技赛】【摇一摇】

## 第二步，娱乐管家系统开起氛围功能

①进入【技术支持设置界面】

路径：后台→右上角→选择系统信息

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019da9e5e5f1298c&type=max)

在下图位置连续点鼠标5~10次

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019da9e6a6662990&type=max)

②
在娱乐管家后台系统添加settings参数
路径：技术支持专用界面→settings管理→增加

点击该界面，点击增加，并输入：

key输入OpenServerEvents

Value输入1

注意：除此方法外，也可以直接在系统安装目录下找到settings配置文件，并直接在配置文件中添加参数为

OpenServerEvents=1

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019da9e796ab2995&type=max)

上图为直接在【技术支持】网站中添加的图，下图为settings配置文件中添加的图（2选1来执行即可）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019da9ed614c29af&type=max)

③开启SSE通讯

路径：技术支持界面→网关设置→开启SSE通讯

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019da9ef2ee329ba&type=max)

④（云服务器客户必要操作）提供加密狗编码给运维组（郑力宣），让他帮忙配置SSH。

⑤等待运维配置完毕后，重启娱乐管家服务。

## 第三步，接入氛围网关主机

说明：此步骤中的氛围网关主机原则上只需要接入网线和电源即可。但是配置阶段时，还需要接入显示屏、鼠标以及键盘来进行配置。

①接线如下图

正面需要接USB口，用于接鼠标和键盘使用（调试必要，后续运行时可不用）

背面需要接网口（只需要接其中一个，接入到和服务器同一个交换机中）、屏幕视频线（VGA或HDIM其中一个）以及电源接口

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f8dec1b7b2731&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f8dec1b8f2732&type=med)

②按开机键开机，并进入到氛围主机界面

PS：氛围主机开机密码为：youcaihua

主机界面右键，点击【设置】，找到【网络】设置路径，进行配置。进入到网络界面，找到以太网，确认开启开关开启后，点击

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f8dec1ba22733&type=med)

进入到设置界面。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f8dec1bb22734&type=med)

③记录目前IP地址信息

1.记录硬件地址

2.IP地址（云服务器客户才需要）

3.默认路由地址（云服务器客户才需要）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f8dec1bc02735&type=med)

④选择IPv4页，并在IPv4界面选择【手动】并固定IP地址以及填写DNS地址

要求：

#### 本地服务器情况

a.IP地址填写为服务器后一位地址（需要确保此地址可用）

如：服务器地址为192.168.110.10，则固定为192.168.110.11

其他子网掩码和网关与服务器保持一致

b.DNS去掉自动，填写为119.29.29.29

#### 云服务器地址情况

a.IP地址填写上一步记录的IP地址以及网关地址（路由器地址）

b.DNS去掉自动，填写为119.29.29.29

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f8dec1bd12736&type=med)

⑤在路由器中，添加MAC地址绑定IP地址功能（非常重要，路由器不设置静态，极有可能断电后IP地址会被乱分配，引起故障）
登录服务器对应的主路由，找到【静态地址分配】，以TP-Link为例，如下图所示登录对应设置界面。通过上面记录的MAC地址（硬件地址）和氛围网关的IP地址，填写到这里来并生效静态地址。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f8dec1bde2737&type=med)

⑥网关编码检验，在跟网关盒子同一网络的电脑（本地服务器则在服务器中打开）上，打开浏览器，http://网关IP/home/index，可看到右上角编码（网关编码），匹配判断是否跟网关盒子上的标签是否一致，若一致，则该网关编码正确。

## 第四步，在娱乐管家系统配置氛围网关主机

路径：【会员】->【运动打卡设置】->【门店配置】->【边缘网关】

#### 核心需要填写的内容

1.边缘网关编码：填写氛围网关主机上的编码，一般贴在氛围网关主机外观上。

2.业务后台地址：填写本地服务器的服务器地址 业务端口，例如：192.168.110.10:9999；云服务器则填写完整域名，如y5******2.yun.youcaihua.net:88

3.推送门店地址：填写该门店的加密狗编码

4.推送appid：填写A001

5.推送key：填写B002

6.开启本地MQTT：勾选开启

7.自动配置MQTT默认参数：勾选开启

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019daa1162362ae9&type=max)

按以上内容填写后，点击保存，并点击【重启边缘网关】（重启时间大概需要3~5分钟，后续修改以上内容均要点击重启边缘网关）。偶尔出现无效的情况时，可手动直接在边缘氛围网关主机中手动重启生效。

## 常见问题处理

请参考《氛围系统配置常见问题》

# 开通氛围系统账号功能

1. 需要在系统新建好账号

2. 开通游乐展柜功能，并且在游乐掌柜功能中开启氛围系统权限

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa2a83bb2fdc&type=max)

3. 微信小程序搜索游乐掌柜，若使用的微信手机号是已经分配了该权限，则直接授权登录，在游乐掌柜页面点击【氛围系统】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa2b0fbf300b&type=max)

# 安装调试说明（影音盒子）

## 影音盒子外观

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019daa3f20bd2c61&type=max)

## 接线说明

1.影音盒子接入局域网网线，网线需要接入到与氛围网关主机同一个交换机（推荐使用），如无条件则可以通过链接WIFI使用。

2.视频输出（HDMI接口）接入到电视中。

注意：部分场地可能需要同一个内容显示在不同电视上时，可根据现场情况使用分屏器来分屏复制显示。

3.音频输出（3.5mm音频接口）接入到场地功放中。

注意：当未接入音频输出端时，氛围系统声音默认从HDMI中输出，并在电视上播放。

4.电源线接电。

5.（调试时可接）USB接入键盘和鼠标，用于调试时使用，非必要，也可以直接通过遥控器进行遥控。

6.（非必要）分屏器说明：目前使用的分屏器有两款，一种是一拖七，HDMI线转网线进行传输，末端再从网线转回HDMI接入电视，可获取更远的分屏范围（注意网线最大不超过60米）；另一种是一拖四，一根HDMI线分四根HDMI线。

一拖七优势：传输距离远，最大可以分7个电视来接。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019daa4be14a2ca1&type=max)

一拖四优势：简单易接，最大可接4台电视，但是适用距离较近。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019daa4c53b32ca4&type=max)

接线原理图如下：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862c7f33bd&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862c8b33be&type=med)

## 安装固定要求

1.尽量使用网线作为进网来源，如果使用WIFI连接时，需要WIFI天线尽量外漏，并且不要碰到金属。

2.遥控接收端尽量往外对，方便遥控来进行控制

3.如有条件，影音盒子用自攻螺丝进行固定，或者使用3M双面胶进行固定，务必确保影音盒子不能掉落。

## 影音盒子放置建议

1.由于影音盒子需要控制声音，所以建议音影盒子放置在门店的音箱功放控制器中，因为音频线一般无法接太远。

2.氛围系统虽然支持上传MP3文件来进行播放背景音乐，但是使用体验较差（一方面因为版权问题MP3格式的音乐文件很难找，另一方面是上传比较麻烦），一般会搭配混响器一起使用（需要客户额外购买），使用混响器就可以实现同时输出电脑音频和影音盒子音频，推荐购买链接：【淘宝-混响器】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019daa5ef4d12cf2&type=max)

3.如果确实视频显示和音频分隔距离太远，那就只能分别通过2个影音盒子来进行控制。

## 电视选型说明

电视品牌选型：推荐使用商用电视（通电自动开机、无广告、耐用）

推荐购买链接：京东购买链接

电视尺寸（挂顶）：

1、收银台短＜2.2m、顾客站距1.5～3m（小店/社区小型电玩）
首选43英寸（行业通用标配）
- 优势：安装不压顶、价格划算，近处结账文字清晰，3米内能看清充值活动小字
- 适用：单工位收银台、层高2.7～3m
2、收银台2.2～3.5m、客距2.5～4.5m（标准中型电玩，最常用）
首选55英寸（电玩收银台万能尺寸，90%门店在用）
- 最佳方案，横向刚好贴合收银台上方，近看结账、远至门店入口5米都能看清活动海报、币值套餐
- 可单台横装；台面超3.2m可选两台43寸并排，整体连贯大气
3、收银台＞3.5m、大厅开阔、层高≥3.3m（商场大型电玩）
65英寸单屏 / 双55寸拼接
- 远距离进门客流也能被优惠活动吸引，视觉冲击力强，适合大额储值活动展示

## 影音盒子调试步骤

### 1.影音盒子联网

情况一：影音盒子端有预留网线，直接接网线即可（推荐接网线）

情况二：影音盒子端没有预留网线，需要接入无线（请按下面步骤进行无线联网）

①准备一个显示屏幕， 用HDMI线连上影音盒子，影音盒子接上键盘鼠标，在影音盒子待机桌面鼠标右键点3次，跳转到影音盒子桌面程序

②连接屏幕后，进入到应用菜单界面，选择“设置”应用

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa149d622ec3&type=max)

③点击“网络和互联网”，进入Wifi连接配置，并链接到局域网无线网络。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa159f352ee6&type=max)

注意：影音盒子的网络必须与氛围网关同一个网络下，并且可以互相通讯。

### 2.配置绑定影音盒子

进入到手机端的氛围系统界面，按下面操作进行绑定

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa2ce8073024&type=max)

#### 常见问题

《氛围系统影音盒子开机时会出现死机情况解决方法》

# 安装调试说明（灯光盒子）

## 灯光控制盒外观

①灯光控制盒主体外观

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa2f53853042&type=max)

②灯带信号放大器外观

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa3001c9304b&type=max)

## 如何判断是什么灯带

说明：灯带种类主要看灯节与灯节之间的接口。如下面说明：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa4033d830cd&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa42cb9730e3&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa454e4630f3&type=max)

## 灯带相关说明

| | 单色灯带 | RGB灯带 | 幻彩灯带（推荐）
| --- | --- | --- | ---
| 灯带成本 | 较低 | 中等 | 较高
| 效果控制 | 单色、闪烁 | 彩色、闪烁、呼吸 | 彩色、闪烁、呼吸、流光
| 油菜花配件 | 需采购信号放大器 | 需采购信号放大器 | 不需要放大器
| 单个控制器可控制长度 | 不限距离 | 不限距离 | 约50~100米（1024个节点）
| 信号放大器放置长度 | 12V(5米）/24V（10米） | 约8~10米 | /

## 灯带控制原理

### 单色灯带

因单色灯只有电源正极（12V/24V）和电源负极（GND），所以此类灯带只有开启和关闭的状态，通过快速变换开启和关闭实现闪烁功能。

### RGB灯带

RGB灯带有较多种类，常用的种类接口为W、R、G、B、12V。通过不同接口发出不同的灯光颜色以及灯光亮度实现彩色效果。如红色灯+蓝色灯同时亮就可以产生紫色灯的效果。

对应接口说明：

12V/24V：为整个灯带的供电接口。有5V/12V/24V三种规格。（灯光氛围盒子必接）

W：为白光的负极接口，同时接通12V和W，则灯带显示白光。（部分特殊灯带会额外有WW和CW，指代的是暖白和正白效果灯）（灯光氛围盒子不需要接）

R：为红光的负极接口，同时接通12V和R，则灯带显示红光。（灯光氛围盒子必接）

G：为绿灯的负极接口，同时接通12V和G，则灯带显示绿光。（灯光氛围盒子必接）

B：为蓝灯的负极接口，同时接通12V和B，则灯带显示蓝光。（灯光氛围盒子必接）

### 幻彩灯带

幻彩灯带每一颗灯珠自带驱动 IC，可单独设置颜色、亮度，能实现流水、渐变、动画、文字、图案、声控律动等复杂效果，统称幻彩像素灯。常见的幻彩灯接口有VCC-GND-C0/C1-D0/D1，对应接口说明如下：

VCC：电源正极（常见为12V/24V）

GND：电源负极（灯光氛围盒子必接）

D0/D1：信号输入，用于接入信号源，用于控制灯的效果（灯光氛围盒子必接）

C0/C1：备用信号源

## 接线原理

### 单色灯带接线示例图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa39b34330a1&type=max)

### RGB灯带接线示例图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa3a901730ab&type=max)

### 幻彩灯带接线示例图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa3be66030b0&type=max)

注意事项：灯带电源盒需要合理结算灯带所需电源盒功率，避免功率不足导致异常。一般5~10米之间增加电源盒进行补电。计算功率/电流时，需要在灯带所需的额带功率基础上乘以1.3倍以上作为冗余，避免在使用灯带效果时引功率不足导致无法实现相应效果。（参考功率电流如下表所示）

### 各类灯带常规功率及电流说明

| 灯带类型 | 电压 | 单米功率 | 单米电流
| --- | --- | --- | ---
| 单色灯 | 5V | 3 W/m | 0.6 A/m
| 12V | 4.8 W/m | 0.4 A/m
| 24V | 4.8 W/m | 0.2 A/m
| RGB | 5V | 5 W/m | 1.0 A/m
| 12V | 7.2 W/m | 0.6 A/m
| 24V | 7.2 W/m | 0.3 A/m
| 幻彩灯 | 5V | 6 W/m | 1.2 A/m
| 12V | 6 W/m | 0.5 A/m
| 24V | 6 W/m | 0.25 A/m

## 灯光盒子绑定系统配置方式

1. 登录游乐掌柜，并打开氛围系统

2. 手机打开蓝牙功能

3. 按照下图操作，给灯光盒子进行联网

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa6f283b32b6&type=max)

# 功能说明

## 场景一：希望电视可以显示门店的推广套餐，或者播放宣传视频

### 效果图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862c9733bf&type=med)

### 操作说明

#### 第一步：将素材都存放到手机中（支持图片素材、视频素材以及音频素材）

a 如果是其他同事处理好的素材通过微信转发给你，建议可以保存到手机中（这样可以进来保存原图，清晰度更高）

b 如果是电脑文件，建议可以通过微信的文件传输助手功能，传输到手机微信中。

无论哪种情况，后续操作都是通过微信直接上传上去。

#### 第二步：在微信搜索游乐掌柜，并登录进去，依次打开【店务】→【氛围系统】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862ca133c0&type=med)

#### 第三步：点击氛围系统中的【素材】，点【上传】，将素材上传上去

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862cab33c1&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862cb633c2&type=med)

#### 注意事项

1.上传的素材，仅只有你自己的手机能看到，其他的手机是无法看到已上传的素材

2.素材可以重复使用，只要不删除，可以一直引用素材

3.删除素材库是不影响已经在轮播的内容。

#### 第四步：点击【设备】，选择你要展示图片/视频的区域，并选择【节目】，在节目点击【图片】【视频】【榜单】任意一个添加你要播放的内容，点进去后，就可以选择刚上传的素材，点击对应素材，完成设置。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862cbf33c3&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862cc933c4&type=med)

#### 注意事项

1.图片是可以设置每张图片显示多少秒。

2.如果是视频，可以设置有声音还是无声音，如果是需要有声音，点一下“屏幕轮播”傍边的喇叭即可切换。

## 场景二：门店想设置每隔一段时间播放安全须知等内容。

### 常见应用案例

电玩城：每隔30分钟播放一次禁止吸烟提醒。

儿童乐园：每隔30分钟播放一次提醒家长看管小孩注意事项。

### 操作说明（以AI生成播报语音为案例进行说明）

#### 第一步 点击【设备】，选择播放区域并点击【音乐】，进入到设置界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862cd433c5&type=med)

#### 第二步，点击【添加】，并点击【AI语音合成】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862cde33c6&type=med)

#### 第三步 输入你要合成的语音播报的内容，并选择音色进行合成

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862ce833c7&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862cf333c8&type=med)

#### 第四步 等待合成结束，并试听效果，确认无误后，点击确定保存素材。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862cfe33c9&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d0c33ca&type=med)

#### 第五步 点击选中生成的素材，并设置播报间隔，完成设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d1733cb&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d2033cc&type=med)

### 其他额外功能：背景影音播放

在音乐这个界面，可以在【音乐】一栏添加MP3音乐用于背景播放

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d2b33cd&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d3633ce&type=med)

MP3文件可使用以此网址免费下载：明月浩空音乐 - 免费多站合一音乐搜索

#### 注意事项：

1.生成后的素材，在素材库可以重复调用，但只能是生成人才能调用

2.删除素材库的记录不会影响已经设置好的语音播报功能。

3.支持自己录制语音（即不适用AI语音生成功能）然后上传播报。

## 场景三：门店想插播寻人启示或实物认领等临时播报。

### 常见使用案例

小孩自己走丢，需要工作人员帮忙喊麦找父母。

### 具体操作步骤

#### 第一步，在氛围系统【设备】界面，点击【插播】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d4133cf&type=med)

#### 第二步 通过AI生成插播的内容（也支持直接上传语音）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d4b33d0&type=med)

#### 第三步 可选择模板生成插播内容，也可以手工输入插播内容。模板生成需要修改相关的内容后再生成。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d5533d1&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d5f33d2&type=med)

#### 第四步 试听插播内容是否正确后，选择播放次数以及播报间隔，点击马上插播即可完成。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d6933d3&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d7333d4&type=med)

#### 注意事项：

1.插播内容不会生成素材库，所以每次插播都是一次性素材；

2.插播优先级比较高，所以直接插播会直接广播相关内容。

3.AI语音的好处是咬字清晰，效果较好，除非门店有专业的广播员，否则都建议用AI语音生成。

4.门店的影音盒子必须接入门店音箱中的音频线，否则无法实现相关播报功能

## 场景四：门店希望在人流高峰期通过摇一摇功能炒热气氛

### 功能说明

摇一摇功能可以在特定时间，通过屏幕显示摇一摇活动并对活动进行广播，让玩家在游玩之余参加摇一摇小游戏，赢取丰厚的储值奖励或实物奖励。通常建议在举办某一些活动前开启该功能，以此来吸引玩家注意力，提高接下来的活动的参与度。

### 活动效果图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d7d33d5&type=med)

报名阶段的电视画面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d8833d6&type=med)

活动中的电视画面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d9433d7&type=med)

活动结束的结算电视画面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862d9d33d8&type=med)

参与者的手机画面

### 建议活动流程

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862da833d9&type=med)

流程核心：①提前预热；②现场造势；③延续热度。

### 注意事项

设置注意点： 【防止薅羊毛】、【活动奖励】、【语音播放内容】、【门店定位】

### 具体操作步骤

#### 第一步，登录游乐掌柜，并打开氛围系统功能，选择【场景】，开启摇一摇功能，并设置摇一摇活动每隔环节与现场哪些灯光进行联动（需要有灯光盒子硬件支持）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862db233da&type=med)

勾选所需要显示摇一摇活动的氛围区域，可配合【灯光盒子】设置摇一摇活动各阶段的灯光氛围。

#### 第二步，新增摇一摇活动

路径：【小程序】-->【营销活动】-->【氛围摇一摇】-->【新增】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862dbc33db&type=med)

#### 第三步，设置摇一摇具体内容

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862dc533dc&type=med)

#### 字段说明

活动名称：可设置重复的活动名称。

开始时间：设置开始时间，到点后自动开始摇一摇活动，因定时任务为1分钟执行一次，所以建议设置的活动开始时间与当前时间间隔大于1分钟。

防止薅羊毛：可设置每个手机号参与每天一次（默认勾选），会判断同一手机号是否在历史活动中有参与；距离门店X米，根据【小程序】-【门店资料维护】中设定的门店定位来作圆心判定玩家当前距离。

报名限时：氛围大屏上会显示活动报名阶段，该限时为参与人员扫码报名期限。

比赛时长：氛围大屏上会显示活动开始阶段的活动结束倒计时。

活动排名显示：氛围大屏上会显示活动结束后的获奖排名页面，页面显示倒计时。

奖品：弹窗设置每个排名或排名区间的奖品，排名不可重复。

氛围语音：已接入AI语音包，可根据所填内容生成摇一摇活动各阶段对应的语音播报。

注意： 当会员获得排名时，奖励是会自动下发的，包括实物商品

### 第四步，完成设置，等待活动开始

活动创建成功后，应显示如下状态，且根据设置的“开始时间”会自动开始活动。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862dcf33dd&type=med)

### 其他列表功能说明

1.如何查看哪些会员参与活动以及奖励发放情况

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862dd833de&type=med)

答：摇一摇活动结束后所有参与活动的会员数据均记录在【营销】-->【摇一摇活动】-->【活动详情】

奖励发放情况状态分别为：处理中、已发放、发放失败，其中，处理中状态为系统自动发放奖励任务执行中，发放失败状态会有相应失败原因文案记录在“错误信息”中，且可进行手动“重发”操作。

2.如何在活动前进行广播

答：参考场景二的内容。

3.设置内容太多，我是否可以复用上一次设置的活动内容，修改一下开始时间即可再次举行？

答：可以的，在上一个活动操作一栏点复制即可。

## 场景五：门店希望通过举办彩票竞技赛来提升彩票机游玩率

### 功能说明

门店可创建彩票竞技赛，玩家游玩指定彩票机台即可参与活动，在规定活动时间范围内，玩家从彩票机台获取的彩票数越多，排名就越高。活动结束后，玩家可根据活动结束时的排名名次获取对应的名次奖励，期间无需额外支付任何储值，其本质就是一个冲榜活动。

### 注意事项

1. 彩票竞技赛是基于卡头获取彩票的数据进行统计，因此不建议出奖率特别大的机台进行比赛。因为出奖率大的机台在活动开始前可能已经在出彩票，此时举行比赛实际只是在比较机台的出彩票速度，没有太大意义；

2. 彩票竞技赛比赛机台，建议取用出票速度相近机台，公平性会更好。

活动效果图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862de233df&type=med)

报名阶段电视显示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862ded33e0&type=med)

报名阶段卡头显示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862df733e1&type=med)

比赛阶段电视显示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e0333e2&type=med)

比赛阶段卡头显示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e0e33e3&type=med)

活动结束电视显示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e1e33e4&type=med)

活动结束卡头显示

### 具体操作步骤

#### 第一步，新增彩票竞技赛活动

在【营销】-->【彩票竞技赛】-->【新增】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e2733e5&type=med)

#### 第二步，设置具体活动内容

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e2f33e6&type=med)

#### 字段说明

活动名称：活动名称可重复。

开始时间：设置活动开始时间，到点自动开始大赛，两活动之间开始时间间隔需大于1小时。

适用机台：读取所有机台类型为彩票机，状态为开启的机台。

参与条件：需会员在卡头投币多少数量才能参与活动，例如：设置数量为10，则会员需在卡头上刷卡、实物币等方式投币数量达到10，参与成功会点亮氛围大屏幕对应的机台P位。

报名时限：参与活动报名倒计时，会显示在氛围大屏幕，若倒计时结束没有会员达成“参与条件”，活动自动结束。

获胜条件：活动获取第一名的条件，一旦达到即结束活动，若无人达成将持续保持活动进行中。例如：设置累计存票>=1000，会员累计存票或出票达到1000，即会结束比赛。

奖品：可按单独或范围排名设置对应奖品，比赛结束后需手动派发。其中，设置“获奖最低票数”，即会员需存票或出票达到该数量，才能有派发奖品资格。“实物商品”非系统配置的商品，一般是线下商品派发，不参与系统库存等统计。

报名阶段、比赛开始、获奖语音：已接入AI语音包，可根据所填内容生成语音播报。“报名人数”、“获奖机台”填写后会自动填充活动报名成功的总人数，和获取第一名的机台名称与P位。

奖励设置：可设置对应的名次奖励、达到对应名次的彩票数量

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e3933e7&type=med)

#### 第三步。完成活动设置

活动创建成功后显示如下：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e4233e8&type=med)

注意观察活动方案的活动状态，正常情况应显示进行中。

## 场景六：门店希望重要VIP玩家到店有播报提醒

### 功能说明

指定VIP会员在各个设备终端登录即会触发播报提醒 （如收银台登录、卡头登录、自助设备登录等），服务人员以此为提醒针对性对指定VIP客户到店提供专属服务。

### 效果图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e4a33e9&type=med)

### 具体设置步骤

#### 第一步，通过游乐掌柜打开氛围系统，并依次点击【场景】→开启【VIP会员到店】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e5333ea&type=med)

#### 第二步，设置VIP到店规则

在设置界面，可设置对应的区域播报范围，以及哪些会员等级会触发欢迎语。并设置相关欢迎语文案用于播报。以及灯光效果（建议灯光效果使用闪烁效果，效果更佳）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e5b33eb&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e6533ec&type=med)

#### 注意事项

使用VIP会员到店功能建议只针对最高等级会与进行播报，减少过多播报而导致效果降低。另外建议门店搭配会员升降级功能配合使用，提高门店高质量会员的粘性。参考操作：如何设置会员自动升降级？

## 场景七：门店希望玩家捉到娃娃时全场播报并联动灯光进行闪烁

### 触发前提

1. 场地礼品机需要安装油菜花卡头，且有接入礼品线

2. 场地有接入影音盒子，影音盒子同时接入电视和广播

3. 场地有接入灯光盒子，配合灯光氛围效果更加好（非必要）

### 触发机制

当客户在装有卡头的娃娃机上抓到娃娃时，即可触发。散客、会员均可触发。

### 支持卡头设备

钻石V9（推荐）、魔方V9（推荐）、反扫卡头（推荐）、魔小方系列（推荐）、油菜盒子、4G盒子

注意：安装油菜盒子、4G盒子时，需要把天线都引到外面，保证网络信号较好情况下才能实现触发效果的，否则会出现较大延迟（可能长达30~40S延迟）

### 具体设置步骤

#### 第一步，提前准备好抓中娃娃播报视频，可自己制作，或下载默认模板。建议下载到手机中，方便后续上传。

默认模板下载链接如下：抓娃娃效果视频.mp4

注意：升级到10.4.2346以上的版本会自动带有默认视频

#### 第二步，通过游乐掌柜打开氛围系统，并依次点击【场景】→开启【玩家捉到娃娃】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e6d33ed&type=med)

#### 第三步，设置抓到娃娃的相关氛围设置

在【设置】里面，我们则可以根据现场情况，选择抓到娃娃后联动的氛围设备区域范围，并可设置哪些机台才会触发播报。

播报时，需要选择一个夹中娃娃时的播放视频，可采用步骤一中的模板视频，也可以自定义制作视频。

最后选择对应联动的灯光氛围效果（建议选择闪烁，效果较佳）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e7533ee&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e7e33ef&type=med)

#### 第四步，如果想设置不同机台抓中播报不同的效果，可在底部选择增加新规则， 按照步骤三的方式再设置一个。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e8733f0&type=med)

#### 步骤五，全部规则设置后，点击保存完成设置。

## 场景八：氛围系统联动抽奖机实现全场播报

### 功能说明

抽奖机是可以联动全场氛围系统，当玩家通过抽奖机抽到奖项时，全场电视、音箱及灯光可以联动播报恭喜玩家。

### 展示效果

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e9033f1&type=med)

### 具体操作步骤

#### 第一步，配置好抽奖机

参考文档：抽奖机操作说明

#### 第二步，通过游乐掌柜打开氛围系统，并依次点击【场景】→开启【抽奖机中奖】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862e9833f2&type=med)

#### 第三步，点击【设置】，对播报效果进行设置

设置播报的氛围设备范围，以及灯光效果，点击保存即可。（建议使用闪烁效果，氛围感更好）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862ea233f3&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eaa862eaa33f4&type=med)

## 场景九：门店想实现大额充值套餐后，全场语音播报并联动灯光闪烁效果

### 功能说明

门店可以设置特定的大额套餐成功充值的时候，全场氛围实现联动播报。

### 触发条件

1.通过收银台直接购买（无论散客还是会员都会触发）

2.自助设备充值（无论散客还是会员，充值还是直接购游戏币）都会触发

3.小程序线上充值

### 具体设置步骤

#### 第一步：准备好对应的套餐所关联的视频，如触发效果所示

此步骤所需的视频，可自己编辑，也可以联系油菜花陈美静和许欣怡来进行编辑。

#### 第二步：系统中设置好对应的套餐，并记录好套餐对应的商品编码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f5ac4a3c44f0b&type=max)

#### 第三步：打开游乐掌柜→选择氛围系统→店务→选择场景

先打开【大额套餐充值】功能，然后点击【设置】进行设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f5ac5032b4f0e&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f5ac529c64f10&type=max)

#### 第四步：设置大额套餐的播报范围、关联播报的套餐，并上传对应套餐播报的视频，以及选择灯光效果，完成设置

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019f5ac5764f4f17&type=max)

### 注意事项

播报的视频，如果场地不会弄，可联系陈美静和许欣怡来帮门店进行视频生成

## 场景十：氛围系统需要对接舞台灯光效果时，希望在【场景】中运用舞台灯光效果（未实现）

### 功能说明

如客户有安装舞台灯光情况下，在场景中（摇一摇、玩家抓娃娃、VIP会员到店、大额套餐充值、抽奖机中奖、彩票竞技赛等），触发效果时展示舞台灯光。

### 接线说明

灯光氛围盒子新硬件支持DMX512接口，目前有两种厂家设备，他们的网口标准不一样，普通舞台灯光的接线是正常的网线就可以，新款的 巨岛LED屏DMX512网线需要将一端的1和2号线对调一下。舞台灯的是1-1，2-2的。巨岛LED屏显示器需要将网线的1-2，2-1。其他线序不变。

巨岛LED屏网线线序

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019fee66b92d2a66&type=max)

# 测试要求

1.测试更换图片、视频播放以及排行榜功能均为正常。

2.测试广播系统，声音正常。

3.测试灯光系统，切换颜色，展示效果均为正常。

4.测试彩票竞技赛功能正常。

# 验收标准

1.协助客户上传套餐图片以及轮播宣传视频（如有）；

2.协助客户设置定时广播功能，包括营业开始广播、定时提醒广播以及营业结束广播；

3.（有灯光盒子必要）协助客户设置灯光显示效果，包括各个播报事件对应的灯光效果；

4.协助客户设置大额套餐充值播报；

5.协助客户设置抓娃娃提醒播报；

6.协助客户设置VIP到店提醒播报；

7. 培训客户以下功能使用，并至少演示一次功能：

①摇一摇功能；

②彩票竞技赛功能；

③插播功能、背景音乐调整；

④基础的图片/视频变更、区域划分、灯光调节、营业广播、VIP到店（修改等级播报设置）、大额套餐充值（修改套餐播报设置）等功能的使用。

注意：以上测试效果技术人员在调试完毕后，需要拍照记录到验收单中！

# 常见问题

1.如果场地不同地方的电视或者灯光需要不同的效果，该如何设置？

答：将对应范围的设备划分区域，不同的区域采用不同的界面和声音。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eab0657f23bd5&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019eab06b3083bd7&type=max)

<
