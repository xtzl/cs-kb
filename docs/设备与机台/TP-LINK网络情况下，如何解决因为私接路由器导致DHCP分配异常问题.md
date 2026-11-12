---
title: TP-LINK网络情况下，如何解决因为私接路由器导致DHCP分配异常问题
category: 设备与机台
tags: 
source: KMS
updated: 2025-12-27
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a19b20ef28019b5f1db69825a5.html
section: 网络调试安装
toc_path: 现场实施知识库 / 网络调试安装
author: 梁建宁
kms_id: 00002958
---

# 问题描述

由于局域网内有私接路由器，导致DHCP获取的IP地址异常，从而引起无法联网或者无法连接服务器的情况。

# 解决条件

1.使用TP-LINK的云网管交换机，或者有网管功能的交换机

# 解决方案

配置DHCP信任接口，非信任接口不接收DHCP配置信息，原理如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19b20ef28019b5f1840732592&type=max)

# 解决方法

1.登录交换机配置界面

如果使用云管理功能，则可以通过商云平台看到交换机对应的IP地址，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19b20ef28019b5f1a65e12595&type=max)

如果是非云管理的交换机，底部也有对应的IP地址，可通过固定自己电脑IP地址与交换机同一网段后来进入配置

2.登录后，找到DHCP监听功能，开启该功能后，将上级路由器接入的端口设置为启用信任，其他端口禁用信任即可

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19b20ef28019b5f1d1daf25a0&type=max)

<
