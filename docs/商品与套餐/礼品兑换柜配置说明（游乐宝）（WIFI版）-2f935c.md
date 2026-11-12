---
title: 礼品兑换柜配置说明（游乐宝）（WIFI版）
category: 商品与套餐
tags: 
source: KMS
updated: 2024-08-02
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81490676e70019111c1c2936e59.html
section: 硬件安装说明及标准
toc_path: 现场实施知识库 / 硬件安装说明及标准 / 自助设备
author: 梁建宁
kms_id: 00001808
---

# 一、作业说明

本文旨在用于指导礼品兑换柜的安装、调试及使用方法

# 二、外观展示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111fda1d86fec&type=max)

# 三、安装准备

1. 十字螺丝刀*1
2. 放置位置预留设备电源

3. 现场预留给设备使用的无线网络

4. 读卡器*1

5. 会员卡*1

6. 提前准备好服务器连接域名地址（该设备只支持域名连接）

7. 手机*1

8.系统版本：游乐宝8.1.6404以上，娱乐管家10.3.4453以上

# 四、安装标准

1.礼品兑换柜配件安装到位（顶部发光字）

2.礼品兑换柜天线垂直立正

3.礼品兑换柜地脚已固定

4.礼品兑换柜连接系统正常，功能能正常使用（包括加货功能、兑换功能以及售货功能均正常）

5.培训客户使用礼品兑换柜（包括如何加货、如何更换货物和如何兑换使用）

# 五、注意事项

1.礼品兑换柜运输要求会将货道用扎带进行固定，安装前需要将闸机全部清理完毕

2.礼品兑换柜重量比较重，请至少两个人以上进行搬运，避免发生倾倒

3.由于礼品兑换柜网络要求较高，请提供专用无线网络给予礼品兑换柜使用，避免因为无线网络不稳定导致功能异常

# 六、作业步骤

## 第一步：配件安装

配件清单：发光字

1.发光字

礼品兑换柜顶部有发光字，直接安装到顶部即可，并接入预留电源即可

2.天线

顶部天线将其树立

3.地脚

将地脚打到底，使礼品兑换柜不摇晃

## 第二步：现场网络设置

### 情况一：现场无线网络可自定义，且支持长wifi名，则可使用自动连接wifi的连接方式进行设置，不需要使用配置卡进行配置

1.在后台生成通用WIFI

路径：游乐宝后台→设置→卡头wifi通讯→通用配置卡

在【通用配置卡】界面，点击【重新设置通讯网络】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a4b56e32&type=med)

2.选择【外场】，并输入域名地址，一般域名地址为：y********.yun.youcaihua.net，端口为88，然后点下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a4c36e33&type=med)

3.点【生成自动连接WIFI】，这里会自动生成特定wifi名称和密码，注意不要修改生成的WIFI名称和密码，直接将自动生成的WIFI名称和密码配置到现场给礼品兑换柜使用的网络设备中。此界面点击下一步，完成设置。

特别提醒：该设备WIFI只支持2.4G网络，所以需要将WIFI中的双频合一功能关闭掉

网络配置参考可参照以下配置文档：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a5a36e34&type=med)

《游乐宝/娱乐管家云服务器网络调试文档，适用范围：油菜盒子》

《游乐宝/娱乐管家本地服务器网络调试文档，适用范围：油菜盒子（低配版AP方案）（本地服务器）》
《游乐宝/娱乐管家本地服务器网络调试文档，适用范围：油菜盒子（中配版AP方案）（本地服务器）》
《游乐宝/娱乐管家本地服务器网络调试文档，适用范围：油菜盒子（高配版AP方案）（本地服务器）》
《游乐宝/娱乐管家网络调试文档，适用范围：油菜盒子（无线方案）（云服务器、本地服务器通用）》

4.点击【服务器地址同步到游智云】完成网络设置。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a5ad6e35&type=med)

### 情况二：现场无线网络不可自定义，或者使用不支持长wifi名设备（锐捷/锐易），则可设置自定义WIFI名称连接，并需要读卡器写配置卡
现场网络配置步骤如下：
1.修改后台通用配置卡信息

路径：设备→基础设置→卡头 wifi 通讯设置→通用配置卡

在【通用配置卡】界面，选择【重新设置通讯网络】，并选择【外场】，输入服务器域名地址，一般域名地址为：y********.yun.youcaihua.net，端口为88，然后点下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a5b76e36&type=med)

输入现场给予礼品兑换柜使用的无线网络名称和对应的连接密码，点下一步。

注意：此WIFI需要符合以下要求

a.无线WIFI需要是2.4G无线网络，并且不支持双频合一功能，如现场网络开启了双频合一功能需要关闭掉。

b.此无线WIFI名称和密码不能有符号和中文，必须纯英文或者纯数字或者是英文加数字组合。

c.无线WIFI需要能通外网

d.无线WIFI不能是隐藏网络

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a69a6e37&type=med)

点击同步至游智云，完成现场网络配置。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a6a46e38&type=med)

## 第三步：礼品兑换柜联接网络

说明：

当现场为上一步骤情况一，则礼品兑换柜会自动联网进入到带配置过程，可跳过此步骤；

当现场为上一步骤情况二，则礼品兑换柜需要刷通用配置卡才能联网，请按照下述步骤进行操作。

1.将空白卡放置到读卡器上，并在通用配置卡界面，点【网络参数写入配置卡】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a6ad6e39&type=med)

2.用螺丝刀打开兑换柜侧面的小门，拉出通讯盒子,并将礼品兑换柜进行通电。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019112002d926ff9&type=max)

3.将读卡模块接入到通讯盒子，并长按通讯盒子的设置键5~10秒后将刚刚写好的配置卡放置到读卡模块中进行读取。联网成功后，盒子会显示【电源】【联网】【强度】都常亮绿色灯，【待机】显示红色闪烁。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1a9c66e3d&type=med)

## 第四步：配置礼品兑换柜

1. 在兑换柜背面可以找到设备二维码，并记下该码。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019112009ec76ffa&type=max)

2. 登录系统后台，新建一个礼品兑换柜项目，输入设备码进行绑定，并标记填写设备名称

路径：设备→设备管理→ 营业设备

在营业设备界面中点击【新增】，选择【自助售货机】并填写设备盒子码

展示如图：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1aab16e3f&type=med)

4. 找到刚才创建的项目，设置礼品兑换柜仓库，及礼品兑换柜货道，如图所示：

设置礼品兑换柜仓库：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111cc4f406f32&type=max)

设置货道数量，请根据实际情况选择，一般为16格子兑换柜；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111ca5cd96f2e&type=max)

设置售货方式，支持仅购买（只支持微信支付）、仅兑换、或者两者都支持

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1ae986e42&type=med)

下载消费二维码：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111cce1896f36&type=max)

5. 将该消费二维码打印出来，并贴于礼品兑换柜上

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019112015c6c6ffb&type=max)

6.在后台设置小程序支付（如有可跳过）

路径：后台→财务→支付方式

在【支付方式】中，点击【新增】，在支付类型中选择“小程序支付”，并填写支付名称，保存该支付方式。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1b1fa6e45&type=med)

## 第五步：新建礼品兑换柜需要上架的商品并添加库存到仓库

说明：一般门店会将礼品兑换柜库存单独设置一个仓库进行管理，当门店采购商品回来后，会先入到门店主仓库，只有在礼品兑换柜缺货时才通过系统调拨的功能调拨到礼品兑换柜仓库，以下流程为采购入库到门店主仓库的流程。

1.后台设置零售商品，设置定价及初始化库存。（新商品适用，已有商品请直接看第5点）

商品设置路径：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1b2066e46&type=med)

2.单个商品可以以这种方式进行设置。

点击【新增】---选择【零售商品】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1b34c6e47&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1b5426e48&type=med)

3.若商品数量多的话，也可以以批量导入的形式进行商品资料录入。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1b6596e49&type=med)

4.下载好模版之后，将商品资料按照模版的格式导进系统，如图：

注意：导入不支持商品图片导入

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1b8536e4a&type=med)

5.后续库存可通过入库单进行入库补充到门店仓库

路径：商品→仓储管理→入库单

点击【新增】添加入库单

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1b8606e4b&type=med)

按照下述信息填写入库单，点击保存完成入库

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1b9756e4c&type=med)

## 第六步：给员工开通礼品兑换柜补货权限

1.员工需要提前新增好账号（不要求管理员权限）

路径：后台→设置→员工管理→用户管理

点击新增，给员工添加新账号，已有系统登录账号可跳过此步骤

注意：此位置需要将联系电话也要填上，而且此电话需要和员工微信的手机号一致

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1ba5f6e4d&type=med)

2. 开通游乐掌柜账号，并勾选授权【仓管】功能

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1bb7f6e4e&type=med)

3. 登录游乐掌柜账号关联的手机微信，在程序搜索栏，搜索【游乐掌柜】，点击售货机补货功能，进行补货入仓；

微信搜索游乐掌柜：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1bc636e4f&type=med)

若该手机微信是已经关联后台且开通了游乐掌柜功能，则登录进去即可看到【售货机补货】功能，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1be536e50&type=med)

## 第七步：上架货物/补货

1.打开游乐掌柜，选择【售货机补货】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019111c1bfaf6e52&type=med)

2.先选择对应的货道，然后点击测试货道，先打开对应的兑换格子门

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001911205889e7005&type=max)

3.选择相应货道，进行上货：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191120958797017&type=max)

4.后台设置好零售商品，在弹窗口搜索该商品，进行货品上架

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191120b2e6a701f&type=med)

5.上架完毕后将礼品兑换柜门关闭即可。

## 第八步：更换货物

在游乐掌柜中，选择对应的货道，并点击【更换商品/货回主仓】可以进行商品变更

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700191120ab5c4701d&type=max)

# 七、测试流程

1.打开微信，扫一下兑换码，兑换一下其中一个商品；检查对应的格子柜是否打开。

2.检查所有商品的定价和兑换价是否正确。

# 七、常见问题

1.礼品兑换柜兑换后不出货

答：一般因为礼品兑换柜没有联网或者联网失败导致，检查盒子连接情况，如果连接成功，盒子应该是【电源】【联网】【强度】【待机】等都亮绿色灯，且不会灭；网络强度弱则【强度】为黄色灯；

2.顾客扫码后，提示设备离线，如何处理？

解决：

如果是WiFi版礼品兑换柜，检查当地网络是否稳定，WIFI是否覆盖到位；

以上检查了无误后，再检查下礼品兑换柜设备里边的盒子状态，看下盒子是否正常。

3.顾客扫码支付后，货道不出货或者出错货品。

解决：

检查游乐掌柜后台货道上架是否设置错误，库存是否不足。

4.礼品兑换柜的库存能否直接通过入库单进行补货？

答：不可以，只能通过游乐掌柜补货。

5.使用测试货道时，商品掉落下来后，会减少系统库存吗？

答：不会，所以需要将商品放回去。

<
