---
title: 天时同城核销对接指引
category: 商品与套餐
tags: 
source: KMS
updated: 2025-08-27
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a1963f44000198ea71e0d237c7.html
section: 软件相关
toc_path: 外部知识库 / 软件相关 / 新娱乐管家系统 / 新娱乐管家后台 / 门店 / 线上 / 天时同城
author: 梁建宁
kms_id: 00002636
---

天时同城核销对接指引

文档说明

天时同城是类似于票付通的一个第三方票务系统，此票务系统同样可以对接其他第三方系统进行分销卖票，通过天时同城进行核销。业务逻辑入下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71ca8f37b2&type=med)

对接准备

1.系统准备，仅娱乐管家支持，支持娱乐管家单店版、娱乐管家连锁版、娱乐管家多商户版；

2.提前从天时同城获取AppID、AppKey、核销url参数；如下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71ca9537b3&type=med)

天时同城基础功能说明

登录链接

天时同城： https://test.sjdzp.cn/Admin/Index/

商家基础功能简介

商家账号可在天时同城后台查看、设置、新增产品

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71caa237b4&type=med)

分销商基础功能简介

分销商账号可在天时同城后台中下单

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cab337b5&type=med)

娱乐管家对接天时同城

第一步：配置线上渠道

操作路径：娱乐管家商户后台-线上-线上渠道管理

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cabc37b6&type=med)

天时同城渠道设置字段说明

渠道类别：选择天时同城

渠道名称：默认天时同城

是否自营：默认是

以下参数要找天时同城提供

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cac437b7&type=med)

以上配置设置完毕后，点击保存，并点击授权，待显示授权成功则代表设置正确。

第二步：天时同城商品与娱乐管家商品进行关联

1. 获取天时同城商品

路径：娱乐管家管理后台—线上—OTA门票管理

操作：点击获取天时同城商品，获取渠道设置的对应商品

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cad437b8&type=med)

2. 绑定娱乐管家本地商品

操作：点击列表【未绑定】按钮，绑定本地商品（通用商品，预存款充值，游乐套票（只能绑定计次票、期限票，包含总部票），游戏币，组合商品），商品选择类型默认游乐套票。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cadd37b9&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cae137ba&type=med)

3.解除绑定或重新绑定商品操作

操作：点击对应商品最右边的绑定商品则可以重新绑定商品，而点击解绑则解除已绑定的商品。

备注：

1）如：OTA(A商品)绑定娱乐管家A套票，用户购买A商品后，未进行核销，但娱乐管家将A商品重新绑定到B套票，用户进行核销时对A套票项目无效，只对B套票项目有效。

2）如：OTA(A商品)绑定娱乐管家A套票，用户购买A商品后，未进行核销，但娱乐管家将A商品解绑，用户进行核销时会提示：没有获取到对应渠道的在售门票。重新绑定娱乐管家商品后可进行核销。

3）绑定商品后会生成本地订单，自动创建对应商品的渠道定价

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cae837bb&type=med)

4. 渠道入会套餐设置已定价的入会套餐

渠道入会套餐用法：在收银台核销时，先在读卡器放一张空卡，然后点击【核销订单】，会自动进入会员入会流程，入会成功后，可将商品核销到会员中

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71caed37bc&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71caf137bd&type=med)

5.娱乐管家OTA订单查询

路径：娱乐管家管理后台—线上—OTA订单查询

可查询对应核销的OTA订单明细，订单号、取票人姓名、手机号、核销时间、价格等，切换界面可按分销商汇总或者按照套票汇总；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71caf637be&type=med)

第三步：核销

核销流程：天时同城票务系统上买票——订单页面获取凭证码——到业务系统上的收银台/售票机/闸机上核销

注意：到业务系统上核销，核销出来的商品取决于后台OTA门票管理菜单，天时同城产品绑定的业务商品

一、购票步骤

1、首先进入天时同城票务系统，登录买票的账号：

地址： https://test.sjdzp.cn/Admin/Index/ ；

2、购买产品下单

3、到订单页面，拿到凭证码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cafc37bf&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cb0137c0&type=med)

二、在收银台核销

进入OTA取票页面，选择天时同城渠道，输入在天时同城拿到的凭证码，点击查询，勾选订单进行核销

当购买了多个数量的票，可以选择核销数量一次性核销多张票

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cb0737c1&type=med)

三、自助售票机核销

用户可以在售票机上，选择取票——OTA取票——反扫天时同城拿到的凭证码或者手输凭证码，进行核销

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cb0b37c2&type=med)

四、闸机验票过闸

前提条件：后台—设置—系统设置—票务基础设置—闸机验证二维码默认渠道设置为天时同城

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cb1037c3&type=med)

用户拿着凭证码直接在闸机上反扫核销，若凭证码有多张票，则核销一次扣一票，核销多次扣多张票

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a1963f44000198ea71cb1537c4&type=med)

五、拉卡拉验票过闸

拉卡拉也支持核销天时同城凭证码过闸，也需要在后台开启开关，反扫凭证码核销，与闸机一致

<
