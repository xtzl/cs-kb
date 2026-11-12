---
title: 如何通过镜像文件不用PE系统情况下重新安装windows系统
category: 系统与设置
tags: 
source: KMS
updated: 2021-02-22
url: https://kms.gzych.vip/webdoc/view/Pub4028801e77994e670177c74fa7390201.html
section: 服务器相关
toc_path: 现场实施知识库 / 服务器相关
author: 梁建宁
kms_id: 00001494
---

# 文档说明

此文档用于在服务器电脑不使用PE启动盘的情况下重装操作系统使用，好处是解决做了阵列后PE盘不识别阵列盘的问题。

# 前期准备

1.下载好镜像，并解压到非系统盘，建议放到E盘里面，D盘会在安装系统时会格式化掉。

下载后如图所示：（建议将镜像名称改成简单的名称，方便后面输入方便）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b49c1d1f71c9&type=max)

2.备份好驱动，如果没有驱动，建议可使用360驱动大师进行驱动备份（建议备份驱动和360安装程序都备份到E盘里面）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b49e7cb971d5&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4a00f4071dd&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4a05dcd71de&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4a1a29371e4&type=max)

3.如果有油菜花系统，请将油菜花系统和数据库文件都进行备份，并备份到E盘

# 操作说明

1.记录一下镜像内的setup.exe应用程序的路径，路径不要有中文，如E:\Win2016\sources\ 这种路径就可以用了，记录好等下需要通过路径来安装

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4a525e771f4&type=max)

3.按照shift键，点左下角的开始菜单中的重启，成功后会进入维护菜单

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4a7d60e7201&type=max)

4.在维护菜单中，选择【疑难解答】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4ae93217214&type=max)

5.选择【命令提示符】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4af5a137215&type=max)

6.选择登录账号administrator

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4b1f6ee721a&type=max)

7.输入开机密码，如果没有开机密码就直接点继续

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4b2d8ac721c&type=max)

8.等待显示此界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4b405ee721e&type=max)

9.在CMD命令行输入输入刚刚记录的路径，如：E:\Win2016\sources\setup.exe 然后按enter确认，路径正确的话就会正常开始安装程序，如果不正确就换一下盘符试试（因为在系统上显示的盘符可能和电脑内置的盘符不一致的，也就是可能你看到的盘符是E盘，实际电脑记录的这个盘符是F盘）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4b57a3c7224&type=max)

10.输入正确后，会进入到windows安装程序中，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4b61bb27226&type=max)

11.点击下一步后，选择安装的系统版本，一定要选择【桌面体验】版本，根据你需要安装的版本来选择

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4b71af7722c&type=max)

12.选择自定义：仅安装Windows（高级）（C）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4b77e11722d&type=max)

13.这个界面可以删除分区然后再重新新增，新增时如果原来没有“恢复”“系统分区”“MSR（保留）”这三个分区时，系统会自动生成，所以删除分区时可以先把这些分区都删除了，然后一次性重新新增。唯一要注意不要删除原来E盘的分区，不然会连镜像都删除掉导致安装失败。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4ba9b927241&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4bc6c407245&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4bc8c097246&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4bd9bd47249&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4be1975724b&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4bf6c6e7250&type=max)

14.等待安装完成即可

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4c029c47251&type=max)

15.安装完毕后提示设置开机密码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193b4c643fc7272&type=max)

16.剩余就是还原驱动以及重新激活一下系统即可。

<
