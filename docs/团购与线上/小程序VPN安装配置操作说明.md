---
title: 小程序VPN安装配置操作说明
category: 团购与线上
tags: 
source: KMS
updated: 2021-07-21
url: https://kms.gzych.vip/webdoc/view/Pub4028801e784962e1017ac72a37353bb8.html
section: 服务器相关
toc_path: 现场实施知识库 / 服务器相关
author: 杨晓华
kms_id: 00000390
---

# 一、作业说明

本安装说明为 VPN
客户端软件安装， VPN
功能涉及到很多线上功能，包括：旧版手机报表、盈客宝小程序、连锁商城门店与总部通信以及部分特殊功能等。请安装安装说明规范安装 VPN
软件。

# 二、 作业准备

1. VPN安装包。

下载链接如下：

https://nos-pulic.oss-cn-shenzhen.aliyuncs.com/%E5%AE%9E%E6%96%BD%E7%BB%84%E5%AE%89%E8%A3%85%E5%B7%A5%E5%85%B7/4.%E6%9C%AC%E5%9C%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%BF%85%E8%A6%81%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6/VPN%E5%AE%A2%E6%88%B7%E7%AB%AF-v4.44-9807-rtm-2025.04.16-windows-x86_x64-intel.exe

# 三、 作业标准

1. VPN安装完毕并能正常运行。

# 四、 注意事项

无

# 五、 作业步骤

## 步骤一：安装程序

1. 双击运行安装程序。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac72904cf3bb0&type=max)

2. 点击下一步，出现下面界面，选择第一个【SoftRther VPN Client】,点击下一步。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac72935f13bb1&type=max)

3. 勾选“我同意最终用户许可协议”，点击一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac7296b0b3bb2&type=max)

4. 直接点击下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac7299ac63bb3&type=max)

5. 选择安装目录之后，点击下一步。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac729bdee3bb4&type=max)

6. 等待安装完成之后，点击完成即可。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac729ea7c3bb5&type=max)

## 步骤二：配置小程序VPN连接信息

1.获取小程序VPN信息，可咨询油菜花人员获取，一般如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001932418225f1ff4&type=max)

2.打开SoftEther VPN Client 管理工具

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da65d200c&type=med)

7. 在下面虚拟网络适配器名列表中右键选择‘创建新虚拟网络适配器’

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da667200d&type=med)

8. 填写对应的网络适配器名，点击【OK】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da670200e&type=med)

9. 在下面虚拟网络适配器名就出现新的虚拟网卡。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da679200f&type=med)

10. 右键‘虚拟网络适配器名’下的空白处，选择【打开Windows网络连接】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da6822010&type=med)

11. 右键刚刚设置的VPN连接，并点击属性

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da68a2011&type=med)

12. 仅勾选【Internet协议版本4（TCP/IPV4）】，其他均不勾选。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da6922012&type=med)

13. 选择【Internet协议版本4（TCP/IPV4）】,点击属性。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da7722013&type=med)

14. 固定本机VPN的IP地址，并填写对应的子网掩码， 注意不要填写网关， 点击确认

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241b97f72003&type=max)

15. 返回管理器界面，点击创建新的VPN连接，并填写相关信息。如下图所示

注意：虚拟HUB需要根据IP地址来进行填写

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019394c7932e2279&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241d7310200b&type=max)

注：其他参数不需要做修改。

16. 点击连接，测试连接是否正常。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da77b2014&type=med)

17. 右键链接，选择【启动连接设置】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193241da7852015&type=med)

18. 完成VPN连接。

<
