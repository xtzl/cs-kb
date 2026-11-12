---
title: WINDOWS系统激活教程
category: 系统与设置
tags: 
source: KMS
updated: 2024-09-01
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81490676e700191ac5ecff96ae2.html
section: 现场实施知识库
toc_path: 现场实施知识库
author: 梁建宁
kms_id: 00001864
---

# 文档说明

本文档用于本地服务器激活服务器WINDOWS功能使用，由于未激活的windows操作系统会存在很多功能上的限制，会导致服务商出现异常，请务必发现服务器未激活状态时，使用本教程提供的工具进行激活。

# 注意事项

激活有风险，如服务器内已有数据，请务必先备份数据到自己的U盘或者其他地方后，再进行激活，避免因为激活失败导致数据丢失

# WINDOWS激活版本支持

不同教程支持的激活版本有所区别，请根据情况使用

一般支持：

windows server 2012 版本

windows server 2016 版本

windows 10 版本

windows 11 版本

windows 7 版本

# 激活方式一：使用工具进行激活

#### 注意事项：激活工具会很容易被杀毒软件直接杀掉，下载和使用时务必提前将杀毒软件关闭掉

#### 使用方法：下载软件并运行，根据软件提示操作使用

## 工具一：神龙激活工具（特点：操作简单，激活方式单一）

https://nos-pulic.nos-eastchina1.126.net/%E6%B2%B9%E8%8F%9C%E8%8A%B1%E5%B7%A5%E5%85%B7%E5%8C%85/1.%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E9%95%9C%E5%83%8F%E6%96%87%E4%BB%B6/%E7%A5%9E%E9%BE%99%E6%BF%80%E6%B4%BB%E5%B7%A5%E5%85%B7.rar

## 工具二：HUE激活工具（特点：有多种激活方式，适用场景更广，但操作略微复杂）

https://nos-pulic.nos-eastchina1.126.net/%E6%B2%B9%E8%8F%9C%E8%8A%B1%E5%B7%A5%E5%85%B7%E5%8C%85/1.%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E9%95%9C%E5%83%8F%E6%96%87%E4%BB%B6/HUE%E6%BF%80%E6%B4%BB%E5%B7%A5%E5%85%B7.zip

# 激活方式二：使用命令行进行激活（需要有网络环境下使用，备选方案，仅支持windows server 2016版本）

1.打开cmd控制台，按顺序输入以下命令，有报错不要管它
slmgr /upk
slmgr.vbs /ipk CB7KF-BWN84-R7R2Y-793K2-8XDDG
slmgr.vbs /skms kms.lotro.cc
slmgr.vbs /ato

（注意：第二行的激活码与下面第二步的匹配，根据激活的版本来修改对应的激活码）
2.进入电脑属性激活服务器
Windows server 2016 数据中心
CB7KF-BWN84-R7R2Y-793K2-8XDDG
Windows server 2016 标准版
WC2BQ-8NRM3-FDDYY-2BFGV-KHKOY
Windows server 2016 嵌入式版
JCKRF-N37P4-C2D82-9YXRT-4M63B

# 其他激活（win10专用）

1.windows+R
2.输入powershell 回车
3.输入 irm https://massgrave.dev/get |iex 自动下载激活脚本
4.输入数字“1”选择永久激活即

<
