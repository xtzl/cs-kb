---
title: Mini APP 中转服务部署操说明
category: 系统与设置
tags: 
source: KMS
updated: 2026-10-30
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a19cff446a01a18c0b82fa7ecd.html
section: 服务器相关
toc_path: 现场实施知识库 / 服务器相关
author: 梁建宁
kms_id: 00003193
---

# 文档说明

此文档用于指引海外服务器需要使用Mini App功能时，需要在总部服务器（连锁门店）或者单店服务器（单店版）中配置该服务，以用于支撑该功能使用

# 前置准备

1.总部/单店需要提前配置域名（不能使用国内域名，需要客户自己搭建配置）

2.需要开通9980端口，并且配置域名也要映射9980端口出来。

# 安装服务

1、 登陆业务系统安装的服务器安装中装服务，步骤如下：

a. 拷贝中转服务文件到服务器，如下文件（注：请以最新版本为主，后续如有版本更新需要更新文件）

下载链接：https://nos-pulic.oss-cn-shenzhen.aliyuncs.com/%E5%AE%9E%E6%96%BD%E7%BB%84%E5%AE%89%E8%A3%85%E5%B7%A5%E5%85%B7/4.%E6%9C%AC%E5%9C%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%BF%85%E8%A6%81%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6/YarpServiceManager.zip

b. 解压到本地磁盘根目录，任意盘符，建议解压到D盘；

c. 打开中转服务文件夹\YarpServiceManager\YarpServiceManager2\目录下的YarpServiceManager.exe，双击文件运行，如图所示;（注：此工具需要.NET工具包支持，如果电脑弹出如下提示，请按照提示下载工具包安装后再打开）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5c987d79&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5c9d7d7a&type=med)

安装后，如果服务没法启动，看看Windows的系统日志，是否有以下报错

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5ca37d7b&type=med)

有的话，点击这个链接，安装框架

d. 在打开的网关服务管理器上进行配置，参考如下图表示；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5ca97d7c&type=med)

e. 在打开的网关服务管理器上进行配置完成后，点击网关管理器上的安装服务，看到安装成功后，参考如下图表示；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5cae7d7d&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5cb37d7e&type=med)

f. 服务安装成功后，点击下图的启动按钮，当看到启动成后，表示中转服务安装完成，参考如下图表示；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5cb67d7f&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5cbb7d80&type=med)

2、 确认上述启动成功后，打开业务系统总部-》MINIapp -》line 配置，选中需要开启mini app的门店；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5cc07d81&type=med)

3、 上述步骤完成后，打开业务系统已经开启的门店-》MINIapp -》二维码管理，扫码或者是复制本店连接进行打开均可以打开H5页面；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5cc67d82&type=med)

# 卸载服务

1、 当中转服务已经安装成功需要进行卸载或者更新时，需要先进行卸载操作，步骤如下：

a. 打开中转服务文件夹\YarpServiceManager\YarpServiceManager2\目录下的YarpServiceManager.exe，，点击网关管理器上的“卸载服务”按钮进行卸载，参考如下图表示卸载成功；

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a01a18bfa5cca7d83&type=med)

# 更新服务

将新的工具上传到服务器任何位置，然后点更新即可，更新后，检查配置

1.路由前缀填写oversea|online,以及勾选了重定向选项框，

2.如果域名后面多出了oversea，删除掉

然后点击下保存配置重启服务

然后把旧的删除或者重命名（免得别人打开错了，开始的时候也可以直接覆盖了旧的工具，但是一定要点更新！！只上传，不点更新等于没用）

<
