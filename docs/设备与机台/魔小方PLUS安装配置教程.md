---
title: 魔小方PLUS安装配置教程
category: 设备与机台
tags: 
source: KMS
updated: 2026-09-15
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a19cff446a01a0a2aec3663c89.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准
author: 梁建宁
kms_id: 00003132
---

# 一、作业说明

本文档用于指导魔小方 PLUS 卡头在彩票机、蓝票机和礼品机场景下的现场安装、接线、调试及日常运维，同时兼容不带安全盒子的简易部署方案，覆盖设备固定、线路接驳、网络配置、项目绑定、参数调试、功能验收全流程。

# 二、外观及功能说明

## 外观

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548a23be3&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548a83be4&type=med)

- 魔小方 PLUS 卡头：一体化刷卡终端，集成读卡、显示、通讯模块，支持 2.4G/5G 双频段 WiFi，可实现刷卡扣费、电子票管理、设备状态展示等功能。

- 安全盒子 V3：信号安全防护设备，内置干扰检测、信号屏蔽模块，配备专用屏蔽天线，可检测并屏蔽 10-100MHz 无线电干扰信号，保障投币、出票信号稳定传输。

## 功能说明

1.支持按键消费或直接刷卡消费

2.支持多种储值扣费

3.支持扫码扣费

4.支持2.4G网络和5G网络

5.兼容国内版和海外版本

6.支持干扰检测，干扰隔断

7.支持自定义灯光

8.支持礼品统计、退电子实物彩票、退电子实物蓝票，并支持同时退彩票和蓝票。

9.支持维修模式

# 三、作业准备

### 工具准备

1.小十字螺丝刀×1

2.手电钻×1

3.批头×1

4.开孔器（木）×1、开孔器（铁）×2

5.读卡器×1

6.会员卡×1

7.记号笔×1

*注意：工具准备清单目录请参考：链接

### 网络准备

卡头专用5G网络，调试方法连接如上：

《网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（低配版AP方案）》

设备型号：

主路由器：TL-R476G
隔离路由器：TP-LINK TL-R479GPE-AC

《网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（中配版AP方案）》

设备型号：

主路由器：TL-R476G
隔离路由器：TL-ER3210G

《网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（高配版AP方案）》

设备型号：

主路由：TP-LINK TL-ER6110G
隔离路由器：TP-LINK TL-ER6110G
AC控制器：TL-AC100

《网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（无线方案）》

设备型号：

主路由器：TL-R476G
无线路由器：WDR5620

注意：此配网方案用于针对自动连接WIFI使用，现场如果有【油菜盒子】设备则不能采用此方案

### 系统准备

娱乐管家系统版本需升级至10.4.3196及以上版本。

# 四、注意事项

- 卡头安装前，必须确保机台处于断电状态，禁止带电作业；特殊情况需带电作业的，须与客户沟通并双方确认后方可操作。

- 卡头安装位置需提前与客户核对，达成一致后再施工。

- 安装完成后，及时清理施工残渣，保持机台与现场整洁。

# 五、卡头固定安装

## 安装方法：

- 位置确认：与客户沟通初步确定安装位置，用记号笔标记开孔点位。

- 结构核查：打开机台投币器护板，观察内部结构，确认安装位置不影响游客操作与日常维护，同时确认投币信号线、马达信号线可正常接驳至对应部件。

- 开孔施工：使用手电钻搭配对应开孔器开孔，根据机台表面材质选择方案：

- 纯铁质面板：使用 20mm 铁制开孔器开孔

- 木质 / 亚克力面板：使用 20mm 木工开孔器开孔

- 复合双层面板（表层亚克力、底层铁质）：先用 20mm 木工开孔器开表层，再用 20mm 铁制开孔器开底层

- 底座固定：手电钻更换适配批头，将卡头底座对准开孔位置，用自攻螺丝固定，不同材质对应要求：

- 纯铁质面板：直接用自攻螺丝固定

- 复合双层面板：先用 3mm 麻花钻开表层引导孔，再用自攻螺丝固定

- 木质 / 亚克力面板：直接用自攻螺丝固定

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548ba3be5&type=med)

5. 线材收纳：将连接线材从开孔穿入机台内部，接入卡头对应接口，盖上卡头上盖，用小十字螺丝拧紧固定。

## 安装标准：

- 所有卡头必须安装在客户认可的位置。

- 全程断电操作，禁止带电安装。

- 卡头固定必须采用自攻螺丝，客户有特殊要求除外。

- 客户无安装经验时，可按以下原则提供安装建议：

- 安装高度不低于机台实物币投币器位置，不影响实物币投币功能

- 卡头正面与机台呈水平或垂直状态

- 卡头显示板朝向机台正前方，便于玩家识别与刷卡操作

- 安装位置不影响机台正常游玩与日常维护

- 优先选择机台平面位置安装

- 卡头垂直安装时，若配备专用支架，需使用支架辅助固定。

# 六、接线标准

## 1.魔小方 PLUS 内部接口

魔小方 PLUS 主控板集成电源接口、通讯接口、投币输入 / 输出接口、彩票输入 / 输出接口、干扰检测接口等，支持 5V/12V 信号电平切换，适配不同机台规格。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548c33be6&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a334c84245f3&type=med)

## 2.安全盒子 V3 内部接口

安全盒子 V3 配备卡头接口、投币器接口、彩票器接口、退币马达接口、屏蔽天线接口，内置拨码开关可配置信号模式、干扰灵敏度、数码币支持等功能。

注意：安全盒子 V3 必须连接屏蔽天线，用于检测并屏蔽 10-100MHz 无线电干扰信号。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a334c85745f4&type=med)

## 3.线材认识

根据是否搭配安全盒子 V3，线材配置分为两类，不同机台场景对应不同线材组合：

#### （1）不带安全盒子线材

基础配置，适用于无强干扰需求的简易部署场景：

- 礼品机场景：投币线 + 礼品线

- 彩票机场景：投币线 + 彩票线

备注：若机台投币器为 6P 接口，需额外配备 4P 转 6P 转接线转接。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a3a42d174de6&type=med)

礼品机/彩票机无安全盒子组合

#### （2）带安全盒子线材

标准防护配置，安全盒子串联在卡头与机台之间，提供信号防干扰保护：

- 彩票机场景：卡头连接线 + 盒子投币线 + 盒子彩票线

- 蓝票机场景：卡头连接线 + 盒子投币线 + 盒子蓝票线

- 退彩票 + 退蓝票场景：卡头连接线 + 盒子投币线 + 盒子彩票线 + 盒子蓝票线

备注：若机台投币器为 6P 接口，需额外配备 4P 转 6P 转接线转接。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548cb3be7&type=med)

蓝票机推币机线材组合

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548d03be8&type=med)

蓝票机线材组合

## 3.接线说明：

### 魔小方PLUS无安全盒子接线如下：

#### 情况一：接礼品机使用投币+彩票线、礼品线，如图：

注：如果机器投币线是6P接口的则需要转接线。支持同时接彩票+礼品，或者单独接礼品。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a3267e804546&type=max)

#### 情况二：接彩票机使用投币+彩票线，如图

注：如果机器投币线是6P接口的则需要转接线。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a327ffbb4556&type=max)

### 魔小方PLUS与安全盒子V3接线如下：

#### 情况一：接彩票器

注：如果机器投币线是6P接口的则需要转接线。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2fdab2341ce&type=max)

#### 情况二：接蓝票马达

注：如果机器投币线是6P接口的则需要转接线。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2fe4cfb41d7&type=max)

#### 情况三：同时接彩票器和蓝票马达

注：如果机器投币线是6P接口的则需要转接线。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2fea3eb41df&type=max)

特别注意：安全盒子V3新增了一根屏蔽天线，安装时需特别注意，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548ef3bed&type=med)

天线作用：检测周围是否存在10～100MHz的无线电信号并进行屏蔽。

### 卡头投币信号线与机台对接说明

#### a.用螺丝刀打开卡头盖子，卡头内部接线如图所示；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548f73bee&type=med)

如图所示，将安全盒子线接到对应位置，并确认灯板与魔小方PLUS主板接口无松动。

#### b.拔下机台的投币线，将卡头的投币器线插在机台投币器上，再接回投币器。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a548fc3bef&type=med)

注意：竖装投币器需使用4P转6P转接线进行转接，如图所示。

#### c.拔下机台的彩票器线，与盒子彩票线进行转接。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549013bf0&type=med)

#### d.找到机台的蓝票马达线，进行转接。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549063bf1&type=med)

# 七、后台配置说明

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5490b3bf2&type=med)

卡头待配置状态

## 后台网络配置

### 1.配置通用配置卡二维码

登录娱乐管家后台，进入【卡头 wifi 通讯设置】-【通用配置卡】页面：

1. 选择部署模式：

- 本地服务器门店选择「内场」，填写服务器 IP 与端口（默认 9999）；

- 云服务门店选择「外场」，填写服务器域名。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549113bf3&type=med)

若不知道如何查看服务器ip地址，可参考以下文档进行查看：

win2012服务器电脑如何查看IP和端口-百度经验 (baidu.com)

2. WiFi 配置分为两种模式：

- 自动生成 WiFi：点击「生成自动连接 WiFi」，系统自动生成 WiFi 名称与密码，卡头通电后自动连接。

- 自定义 WiFi：手动输入 WiFi 名称、密码，选择网络模式（默认 WPA），点击保存。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549183bf4&type=med)

### 2.配置场地WiFi信息

完成配置后，后台会生成配置二维码，请将场地WiFi信息设置为二维码上的WiFi账号和密码。

如图所示：

1. 点击「服务器地址同步到游智云」，将配置信息同步至云端。

2. 将场地的 WiFi 名称、密码修改为与配置卡完全一致。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5491d3bf5&type=med)

无线网络配置教程请参考：

《网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（低配版AP方案）》

《网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（中配版AP方案）》

《网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（高配版AP方案）》

《网络调试文档，适用范围：魔方卡头V9、钻石卡头V9（无线方案）》

### 3.魔小方PLUS卡头操作及显示效果

#### 若使用自动生成的WiFi，卡头会自动连接；若使用自定义WiFi名称，则需手动刷通用配置卡写入WiFi信息。

写卡方法：将空白卡放到读卡器中，点击写入通用配置卡，等待写卡完成。

卡头通电后，屏幕依次显示「连接网络→获取 IP→获取设备配置→预注册设备」，最终显示设备 ID 与联网成功状态，即为网络连通正常。

PS：魔小方 PLUS 支持 2.4G 和 5G 双频段 WiFi。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549243bf6&type=med)

卡头连接配置状态

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549293bf7&type=med)

卡头连接网络成功状态

## 项目创建、配置及调试

### 1.项目创建

1.手机可以先通过支付宝扫一扫或手机扫码工具扫第一个二维码连接门店卡头无线网络

2.再打开微信或手机扫码工具，扫描通用配置卡二维码。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5492e3bf8&type=med)

3.进入卡头配置界面后，输入管理员 / 机修账号密码登录。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549333bf9&type=med)

4.点击【新增】，选择项目分类为「彩票机 / 蓝票机/礼品机/模拟机」，填写项目分类名称，点击保存完成项目分类创建。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549393bfa&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5493d3bfb&type=med)

5.返回界面后，点击项目分类栏，在弹窗中点击刚创建的项目类型。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549423bfc&type=med)

6.补充填写该项目名称、每局投币数、消费类型等基础信息，点击保存完成项目创建。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549483bfd&type=med)

### 2.卡头关联绑定项目

在项目列表中找到对应游戏项目，点击【添加端口】。并输入卡头屏幕显示的设备编号，点击【关联】，完成绑定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2c3f7073e90&type=max)

绑定成功后，卡头屏幕显示对应项目名称与 “扫码投币” 提示。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2b9b8793db3&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2b9ccb83db6&type=max)

注意：若绑定错误或需更换项目，长按卡头重置按键 5 秒，重置网络后可重新绑定。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a3bd9e4950af&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a3bde77f50b6&type=max)

# 八、物理参数调试方法

## 魔小方PLUS卡头物理参数调试方法

请参考《如何对卡头参数进行调试》

## 魔小方PLUS调试路径

注意：如果在安全盒中，选择【按盒子拨码为准，则以下设置无效】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2f0433a40b7&type=med)

#### 调试路径：

网页设置路径如下图所示

进入对应项目的【参数设置】页面，可分别调试投币参数、出彩票参数、出礼品参数，所有参数调整后卡头重启生效。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5495f3c02&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549633c03&type=med)

手机上调整投币参数与彩票参数路径如下图所示

进入对应项目的【参数设置】页面，可分别调试投币参数、出彩票参数、出礼品参数，所有参数调整后卡头重启生效。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549683c04&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5496e3c05&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549733c06&type=med)

## 基础调试说明

魔小方 PLUS 主控板支持投币信号 5V/12V 切换，通过主板跳针调整输出电平，适配不同机台的信号规格。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549773c07&type=med)

投币参数设置：

- 投币高电平：常开 / 常闭可选，必须与机台投币器电平拨码一致

- 投币速度：单位毫秒，默认 200ms，出现吃币现象时增加该值

- 识别投币脉宽：单位毫秒，默认 10ms

- 投币脉宽：单位毫秒，默认 80ms，推荐参考值为「投币速度 ×0.6」

- 投币脉冲数：可设置与投币数相同，或自定义单局脉冲数；填0则未与投币数相同。
调整后点击【测试】或刷入机修卡观察机台币数与卡头扣费是否一致

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2c287de3e7c&type=max)

出票参数设置

- 光眼电平：常开 / 常闭可选，必须与出票器拨码一致

- 马达有效电压：低电压 / 高电压可选，必须与出票器规格一致

- 出票延时：单位毫秒，默认 100ms，出票顿卡时可降低至 10ms

- 出票放大倍数：设置出票数量倍率，默认 1 倍

- 出票速度：单位毫秒，默认 100ms，计数不准时调整该值大小

- 出票脉宽：单位毫秒，默认 35ms，推荐参考值为「出票速度 ×0.6」

- 出票模式：可选择 “会员存电子票、散客出实物票” 等模式

- 单次最大出票数：默认 5000 张，用于防止线路异常导致无限出票，可根据需求调整

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2c2daf43e81&type=max)

## 魔小方PLUS灯光设置

灯光颜色调整无法完全自定义，只能按目前系统内置好的几种颜色去调整，并且是按卡头规划的区域去进行统一设置，设置路径如图：

第一步：设置卡头区域

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2c81b4f3ec0&type=max)

第二步：按不同区域设置灯光颜色

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2c74e7a3eb4&type=max)

# 九、测试要求

#### 投币信号匹配测试

将会员卡放到卡头上读取，卡头能显示卡内余额，按键1能扣除对应币数，机台自带码表正常增加扣币数量，则代表投币信号正常；

#### （接彩票线）彩票信号匹配测试

1.先清空彩票器中的彩票，再通过游玩获得奖励，待累计100张以上彩票（此时机台应报错"彩票器缺票"）后记录数量；将会员卡/机修卡插回卡头，按复位键复位彩票信号，观察出票数量与卡头显示的彩票数量是否一致；

2.先清空彩票器中的彩票，再通过游玩获得奖励，待累计100张以上彩票（此时机台应报错"彩票器缺票"）后记录数量；将彩票放回彩票器并出票，待出票完成后，核对本次出票数量与机器记录的数量是否一致。

#### （接礼品线）礼品信号匹配测试

将礼品放入出礼品口，模拟出礼品过程；机器显示中奖、油菜花后台记录出礼品数量，即完成礼品测试；

#### （接马达线）出实物币信号匹配测试

1.通过游玩获得奖励，待机台累计100积分以上后，将机修卡或会员卡插入卡头，点击机台退分按钮并记录数量，观察出币数量与卡头显示的币数量是否一致；

2.通过游玩获得奖励，待机台累计100积分以上后，点击机台退分按钮并记录实体币数量，观察出币数量与机器退分时显示的待退币数量是否一致；

#### 投币信号高低电平匹配测试

机台断电，30秒后重新上电；上电后机台和卡头均无错误代码报出，则代表参数设置正常；

#### 网络信号通讯测试

连续刷卡5次，每次读取时间不超过1秒；同一张卡刷卡保护间隔与后台设置一致，则代表网络正常；

# 十、其他

## 1.维修模式

当机台处于维修或不启用状态时，可在卡头上设置维修模式，设置后卡头将不可使用。

1.卡头插入机修卡

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5497d3c08&type=med)

2.按下按键1，进入维修模式

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549833c09&type=med)

3.退出维修模式需重新插入机修卡或重启卡头

## 2.卡头灯光颜色控制

站内链接：魔小方卡头如何更换灯光颜色

https://kms.gzych.vip/webshare/open/Pubc7c160f7327b.html

## 3.安全盒子V3主板说明

安全盒子 V3 主板拨码可配置硬件级功能，核心拨码定义：

- S2：拔掉投币线检测（左开右关，默认关）

- S3：检测到干扰时强行拉低投币信号（左开右关，默认开）

- S4：门锁检测（左开右关，默认关）

- S5：使用数码洞洞币（开启后支持有孔币）

- 电平选择拨码：左档为盒子主板拨码优先，右档为系统后台设置优先

拨至「手动配置模式」后，后台参数修改不再影响卡头物理参数，需通过拨码直接调整。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549893c0a&type=med)

## 4.旧卡头接口与魔小方接口

由于盒子批次或卡头类型不同，线材有新老之分，请注意将不同线材接到对应的接口。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5498e3c0b&type=med)

## 5.安全盒子手动配置切换说明

在安全盒子中找到该开关，可将其设置为手动配置模式；设置后，后台参数修改将不再影响卡头物理参数。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549933c0c&type=med)

## 6.数码币使用说明

数码币即行业所称有孔币，适配需同时满足两个条件：

- 机台投币器、出币器硬件支持数码币，不支持则需更换对应部件

- 安全盒子 V3 开启 S5 拨码（使用数码洞洞币）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549993c0d&type=med)

数码币即行业所称有孔币，适配需同时满足两个条件：

- 机台投币器、出币器硬件支持数码币，不支持则需更换对应部件

- 安全盒子 V3 开启 S5 拨码（使用数码洞洞币）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a5499e3c0e&type=med)

# 十一、常见问题

## 卡头报错代码

1.经常误报检测到干扰

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a0a2a549a23c0f&type=med)

答：检查机台内部是否存在10～100MHz的信号干扰；如无干扰，请在将卡头灵敏度调为"一般"或“迟钝”。

2.游戏机报投币故障

答：尝试切换投币选项的常开/常闭模式。

3.投多个币时，机器显示的币数比卡头少（吃币）

答：投币速度过快导致。请降低投币选项中的投币速度和投币脉宽，一般脉宽＝投币速度×0.6。

4.卡头一直显示"连接WiFi"

a.网络未配置好，请检查网络；

b.恢复出厂设置并重新写通用配置卡（需修改通用配置卡信息）；

c.测量12V电压是否正常，电压低于5V时卡头无法正常工作。

5.卡头放卡即直接扣费

答：卡头消费设置中未设置按键模式。

6.每次出彩票都多一张或者少一张

答：彩票光眼选项的常开常闭切换下尝试。

7.出彩票时卡头记录的比机器显示的多(计数不对)

答：出票速度太快,降低出票选项的出票速度和出票脉宽,一般脉宽=出票速度*0.6

8.出票时卡头出够5000就报缺票了

答：后台设置了单次最大出票数量,此选项是防止线路接触不良或者游戏机死机造成无线出票情况的.出现后只需按下服务键继续出票即可,如果每次出票都很大可适当调整数量

9.出票是出现顿卡,一阵一阵的卡
答：出票延时太高,大部分机器可设置到10ms,如果异常再调整到200ms左右

10.出票时每次出一张就停了
答：单次最大出票数设置成了0,调整好即可

<
