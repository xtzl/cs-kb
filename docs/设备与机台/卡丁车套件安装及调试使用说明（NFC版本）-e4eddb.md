---
title: 卡丁车套件安装及调试使用说明（NFC版本）
category: 设备与机台
tags: 
source: KMS
updated: 2023-03-16
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81485aecc240186e9a7133c0530.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准 / 卡头类（刷卡终端）
author: 梁建宁
kms_id: 00000609
---

# 一、说明

卡丁车套件（通用套件）用于安装在卡丁车上，通过控制开关（一般控制油门开关）来达到控制卡丁车的效果。

# 二、产品参数

1、产品电压DC＜48V—0.8A、DC5V—0.4A；

2、额定功率100W；

3、产品材质：ABS、PVC、亚克力、五金

4、使用温度：-20℃--60℃

5、产品尺寸：

卡丁车套件电源板W x D x H 120*90*48mm

# 三、图形说明

1、卡丁车套件电源板

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ac9204f6&type=med)

注意：电源正负极不能接反，DC供电需小于48V。

2、卡丁车开始按键

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ac9e04f7&type=med)

3、卡丁车套件显示板

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6acaa04f8&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6acb404f9&type=med)

4、卡丁车地感

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6acc104fa&type=med)

6、起点终点地感（NFC版）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6accb04fb&type=med)

7、卡丁车遥控器

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6acd804fc&type=med)

复位键：复位圈数或时间，重新设置

计圈设置：输入完数字圈数后按此件设置圈数

计时设置：输入完数字圈数后按此件设置计时

数字键：计圈或计时数字输入

8、卡丁车紧急遥控器

长按卡丁车套件显示板按键10秒，数码显示管会显示设备号，长按紧急遥控需要设置的车号（1号为1号车，2号为2号车，以此类推），直到遥控器和显示板响一声就完成设置车号。设置完成后，需要紧急停车时，按对应的车号停车，再按一下启动。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ace704fd&type=med)

# 四、基础接线（如下图所示）

1.开关控制接线图

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6acf204fe&type=med)

# 五、安装工具

1.开孔器（开木）25mm

2.锉刀

3.扎带

4.0.5mm电线（如有需要）

# 六、安装说明

1.使用开孔器在卡丁车适当位置开孔，用于放置安装按键

2.翻开卡丁车底部，放置卡丁车地感，用扎带或者螺丝固定

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad0104ff&type=med)

3.拆开卡丁车面板，找到油门控制线，卡丁车电源线如下图接入线（卡丁车与油门线路颜色可能与下图有所差异，请根据实际情况来接入）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad0e0500&type=med)

4.终点搭建

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9ae52e405bf&type=max)

铺完NFC卡后在铺上终点地毯

# 七、调试说明

1.准备说明

1)系统要区分本地服务器和云服务器，如果是本地服务器，需要开通云互联功能。

2)卡丁车功能需要额外开通卡丁车增值服务，需要联系油菜花实施组组长进行开通，不需要额外费用

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad1a0501&type=med)

3)调试前需要对卡丁车进行编号，以方便管理。

4)卡丁车支持收银台启动及POS机启动，由于卡丁车需要服务员管理，如果卡丁车入口没有收银台，建议配备POS来扣费启动。

5)确保业务系统是否支持卡丁车，游乐宝需要8.0.9以上，娱乐管家暂不支持。

6)卡丁车需要有电视显示排行榜等信息，需要确保电视是否为智能电视，并支持安装APP

2.软件操作

1)添加项目类型及游乐项目

(1)第一步：进入游乐宝后台界面→选择设备→设备管理→游乐项目→新增分类→保存。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad2c0502&type=med)

(2)第二步：进入游乐宝后台界面→选择设备→设备管理→游乐项目→卡丁车→新建项目→输入项目信息→下一步→完成。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad3c0503&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad480504&type=med)

2)设置卡丁车配置网络

(1)第一步：第一步：进入游乐宝后台界面→选择设备→基础设置→卡头wifi通讯设置→通用配置卡→重新设置通讯网络

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad570505&type=med)

(2)第二步：选择内网-填入服务器地址-点击下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad620506&type=med)

注意：域名地址不需要填入http: // 以及地址末端的/ ，如你获得的域名地址为http ://Y 加密狗编号.yun.youcaihua.net:88/admin/,则这里填入Y 加密狗编号.yun.youcaihua.net，后面端口填88

(3)第三步：不用理会无线名称等信息，直接点击完成

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad720507&type=med)

(4)第四步：点击“服务器地址同步到游智云”，等待右上角提示“数据保存成功”即可完成服务器地址同步。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad820508&type=med)

3)激活卡丁车流程

(1)第一步：进入游乐宝后台界面→选择设备→基础设置→卡头wifi通讯设置→通用配置卡→手机扫码二维码设置→用手机浏览器扫描二维码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad930509&type=med)

(2)第二步：点击手机待配置端口→手动激活端口→输入卡丁车套件电源板上9位设备码并确定→提示激活成功

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ad9f050a&type=med)

(3)第三步：点击项目卡丁车→显示未关联卡丁车→点击关联→添加成功

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6adb0050b&type=med)

3.后台其他参数设置（主要涉及游玩模式、计费模式等设置）

1)设置游玩方式（计圈/计时）

说明：此方式决定着游玩的计费方式

计圈模式：设置游玩一次可以玩多少圈，假如设置为3圈，当卡丁车已经跑完3圈后，就会开始倒计时10秒，随后停车。（优点，顾客无论水平如何，都可以完成预设的圈数，并且每圈都会有相关的单圈成绩，较为适合竞技类卡丁车；缺点是假如顾客水平较低的情况下，整体游玩时间偏长）

计时模式：设置付费一次可以玩多久，并可以设置计时结束后是否到终点后才停车，假如设置为10分钟，卡丁车游玩10分钟，在最后一分钟快结束时开始倒计时。

2)设置默认圈数及最多圈数（计圈）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6adcb050d&type=med)

说明：默认圈数为服务员为顾客扣除一次游玩费用后，默认开启的圈数，这个圈数可视情况增加，但增加的最大值不能超过最多圈数

3)设置默认分钟及最多分钟（计时）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6add7050e&type=med)

说明：默认圈数为服务员为顾客扣除一次游玩费用后，默认设置的可玩时间，这个时间可视情况增加，但增加的最大值不能超过最多分钟数。

4)设置停车提醒（计圈）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ade1050f&type=med)

说明：在通过最后一圈后，开始倒计时多少秒停车。

5)设置停车提醒（计时）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6adef0510&type=med)

说明：设置计时后，计时结束倒计时多少秒停车，可设置经过最后一圈终点后再停车。

6)设置排行榜计算规则

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6adfc0511&type=med)

7)设置计圈器感应间隔

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae080512&type=med)

说明：此间隔为卡丁车重复经过计圈器后，多少秒内不再重复感应（用于防止顾客走错路重复经过导致计时时间错误的情况）

8)设置背景图片

设置排行榜的背景图片

# 八、卡丁车客户端使用

1、POS机使用（V1）

第一步：进入POS机油菜花界面→选择卡丁车→读取会员卡或二维码→选择时长→选择车辆→激活车辆→激活成功。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae190513&type=med)

第二步：进入POS机油菜花界面→选择卡丁车→读取会员卡或二维码→选择车辆解锁→解锁→解锁成功

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae270514&type=med)

2、POS机使用（V2）

POS版本：V19.1226以上

查询会员并登录

说明：支持扫会员码（LG_\LQR \LT ）手机号、会员卡查询会员，并登录查看会员储值余额、套票信息。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae330515&type=med)

登录成功

说明：可以选择扣费次数和发车圈数/时长（根据后台设置），最多支持1-99输入

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae400516&type=med)

核销/核销并发车

说明：扣减会员相应储值（代币/金币/预存款）、套票（计次票/期限票）次数，且会员核销信息进入待发车界面（此时卡丁车未发车）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae500517&type=med)

发车

说明：

①、在待发车界面，选择会员核销记录，并选择相应车辆

②、可以对同一辆卡丁车进行加时操作

首次发车：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae5c0518&type=med)

加时：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae670519&type=med)

确定之后，核销记录清除，对应圈数/分钟数，下发到卡丁车上（通过卡丁车“发车”按键开启通电并开始计时）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae72051a&type=med)

解绑

说明：

①、正常游玩结束，卡丁车停止，自动解绑。

②、卡丁车非正常结束，需要人工解绑车辆（手动解绑车辆后产生的圈时不记录）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae7f051b&type=med)

3、收银台使用（V1）

路径：游乐宝收银台->游乐->卡丁车

功能详解图：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6ae95051d&type=med)

会员登录后->选择游玩的卡丁车辆->游玩时长->点击激活车辆->扣费成功后激活卡丁车

4、遥控器使用

1.上个记录按键：回到上个记录的数字

2.下个记录按键：回到下个记录的数字

3.复位按键：复位卡丁车的所有状态，可强制解绑卡丁车

4.计圈按键：在已经输入数字的情况下，按“-”进入计圈模式

5.计时按键：在已经输入数字的情况下，按“ ”进入计时模式

6.清除按键：卡丁车未启动时，清除数码管一位数字，以此类推

7.数字按键：设置游玩的圈数/时长

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6aeb6051f&type=med)

# 九、卡丁车扣费类型

1.支持储值扣费

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6aec10520&type=med)

2.支持套票扣费

当会员有套票，且套票项目包含当前卡丁车，则优先扣票

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6aed60522&type=med)

# 十、在线/离线激活卡丁车

1、在线激活卡丁车

卡丁车在线时，用户可正常激活并扣费

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6aee10523&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6aeea0524&type=med)

2、离线使用卡丁车

当卡丁车不在线时，客户可选择继续或者取消扣费

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6aef60525&type=med)

若继续扣费时，扣费后，可使用遥控器离线激活卡丁车游玩

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6af000526&type=med)

# 十一、常见问题

1、新出厂卡丁车可能遇到无法激活的情况，一般由于卡丁车在出厂前进行绑定检查，出厂时未进行解绑，如出现这种情况，需要手动解绑一下，解绑方法如下：

第一步，确认卡丁车编号

第二步，在网页上输入以下内容：https://yzy.gzych.vip/yzy/api/v1/device/unbind/卡丁车盒子串码

回车后即可强制解绑

2、常见错误代码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6af0e0527&type=med)

3、更换物联卡：把盒子的螺丝拧松打开盖子即可更换

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6af1b0528&type=med)

4、匹对遥控器

用手按住盒子上的白色小按键10秒左右之后放开，待显示板上显示0以后再按住遥控器上跟车
号匹配的相应数字键5秒左右即可，如无法遥控需把盒子断电重启然后再来一遍：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186e9a6af290529&type=med)

# 十二、卡丁车排行榜APP

下载链接：

新版卡丁车排行版

https://nos-pulic.nos-eastchina1.126.net/油菜花工具包/5.常用的APK软件/卡丁车排行榜APP（新）.apk

旧版卡丁车实时记录榜:

https://nos-pulic.nos-eastchina1.126.net/油菜花工具包/5.常用的APK软件/游乐宝-卡丁车实时记录.apk

<
