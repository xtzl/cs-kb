---
title: host 文件被windows defender 安全中心 删除？
category: 制度与流程
tags: 
source: KMS
updated: 2024-04-22
url: https://kms.gzych.vip/webdoc/view/Pub2c93a8148c3e04c2018f03b006813c69.html
section: 外部知识库
toc_path: 外部知识库
author: 陈刚
kms_id: 00001695
---

背景：

最近有很多客户反馈 系统突然登录不上去了。经过排查发现 mall.host.exe文件被 windows defender 安全中心当作病毒查杀了。可能不止这一个文件。

解决方案：

1、从相同版本的其他服务器的 YCHMALL 文件夹中复制以下内容：（特别注意，不要拷贝 setting.inf、Settings_copy.inf、instance.bin、latest.yml）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f03aa4a993c51&type=max)

2、手动设置排除项

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f03ac259c3c56&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f03ac7ad53c58&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f03acd6c63c5a&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f03ad67503c5f&type=max)

3、或者直接使用小工具来添加排除路径：ExcTool_v1.3

![](https://kms.gzych.vip/webdoc/view/actionImg/PubIcon.do?id=2c93a8148c3e04c2018f03b126503c77)

ExcTool.zip
预览 下载 详情

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a8148c3e04c2018f03aee1f73c62&type=max)

4、注意：已安装火绒的，也最好设置以下排除文件夹

<
