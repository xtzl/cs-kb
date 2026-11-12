---
title: 总部vpn配置流程
category: 系统与设置
tags: 
source: KMS
updated: 2025-11-20
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81485aecc24018658ed26433ddf.html
section: 服务器相关
toc_path: 现场实施知识库 / 服务器相关
author: 高晓钦
kms_id: 00000021
---

# 一、 文档说明

门店本地部署时需配置总部vpn，若不配置总部vpn，则门店无法与总部进行通讯；

# 二、 安装准备

1. VPN客户端已安装完毕，本流程一般在安装小程序VPN后再配置总部VPN连接，所以一般VPN会在安装小程序VPN时已经安装完毕。如果未安装小程序VPN，可参考【小程序VPN安装与配置（所有门店都需要安装）】教程进行安装。

2. 总部VPN信息获取（联系云服务器管理员获取：梁建宁、高晓钦、李韩艳，有权限的也可以自行获取）；

3. 总部域名地址以及总部VPN地址

样式：

总部域名地址：y********.yun.youcaihua.net/admin

总部VPN地址：192.168.**.1:99**

4. 场地外网能正常使用，服务器能正常通外网。

5. 总部VPN的主机地址为：

2025年11月20日之后的总部

主机地址：syn002.youcaihua.net

端口：15555

2025年11月20日之前的总部

主机地址：syn0.youcaihua.net

端口：5555

# 三、 安装要求

1. VPN连接能正常连接。

2. VPN开启了开机自动启动。

3. 总部VPN配置完成。

4. 门店VPN配置完成。

# 四、 注意事项：

1.总部地址一定不可以填错，否则会导致数据同步会出现异常引起总部系统瘫痪

2.配置完VPN之后，一定要同步将门店VPN地址填写到总部系统中门店URL地址中，并且一定要确保地址填写正确。

3.如果总部和门店都是云部署，则不需要配置VPN，可跳过此教程

# 五、 作业步骤：

## 1.总部VPN信息获取

配置总部VPN时，进行总部VPN信息获取 （联系云服务器管理员获取：梁建宁、高晓钦、李韩艳）

总部VPN信息格式如下：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193af85ba6c67b4&type=max)

## 2.总部VPN配置

在门店本地系统配置总部VPN

（1）打开SoftEther VPN Client 管理工具

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186590de9953e28&type=max)

（2）在下面虚拟网络适配器名列表中右键选择‘创建新虚拟网络适配器’

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186590e36ea3e29&type=max)

（3）填写对应的网络适配器名（若无特殊需求，按照默认命名即可），点击【确定】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186590f0ce43e2a&type=max)

（4）在下面虚拟网络适配器名就出现新的虚拟网卡。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186591bcb583e2e&type=max)

（5）右键刚刚设置的VPN连接，并点击属性

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186591c19f53e2f&type=max)

（6）仅勾选【Internet协议版本4（TCP/IPV4）】，其他均不勾选。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186591c4fdc3e30&type=max)

（7）固定本机VPN的IP地址，填写对应的获得的门店VPN的IP地址信息，并填写子网掩码，子网掩码为255.255.255.0，网关留空，DNS留空；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193af86459a67b9&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186591c74393e31&type=max)

（8)返回管理器界面，点击创建新的VPN连接；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186591cff813e32&type=max)

(9)根据给到的VPN信息进行填写，如下图所示：

2025年11月20日之后的总部

主机地址：syn002.youcaihua.net

端口：15555

2025年11月20日之前的总部

主机地址：syn0.youcaihua.net

端口：5555

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b45152a370cb&type=max)

(10)返回管理器界面，右键创建的总部VPN，点击连接，测试连接是否正常。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc240186592423d73e5b&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc2401865924d02c3e5c&type=max)

(11)右键链接，选择【启动连接设置】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81485aecc2401865924fb003e5d&type=max)

(12)完成VPN连接

## 3.总部连接URL地址测试是否正常

#### 字段说明：

总部URL地址：指连接总部VPN后，可以访问到总部系统的IP地址，一般为： 192.168.**.1:999*

门店URL地址：指总部服务器可通过连接VPN后，可以访问到门店服务器的IP地址，一般为：192.168.**.**：9999

由于两个地址都是数据通讯相关的，务必要确认地址的正确性，以避免因为地址错误导致数据同步异常问题。

总部VPN配置完成后，需测试与总部通讯是否正常，从油菜花工作人员获取总部URL地址，并通过浏览器打开总部系统，看看是否可以打开（若不知道，可咨询相关技术--主管梁主管、技术高晓钦，一般给总部VPN信息的时候会一并给到 ）。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193afa450d2680e&type=max)

# 六、 常见问题：
1.若按照文档配置完成后，总部与门店还是无法进行正常通讯，则检查下门店服务器电脑防火墙是否关闭；

<
