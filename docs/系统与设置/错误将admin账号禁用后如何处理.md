---
title: 错误将admin账号禁用后如何处理
category: 系统与设置
tags: 
source: KMS
updated: 2022-06-27
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81480a4846c0181a3af4c294e45.html
section: 日常问题处理案例归档
toc_path: 现场实施知识库 / 日常问题处理案例归档 / 软件相关
author: 梁建宁
kms_id: 00000265
---

一、登录数据库

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81480a4846c0181a3af4b064e40&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81480a4846c0181a3af4b324e41&type=med)

二、选择门店的数据库

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81480a4846c0181a3af4c154e42&type=med)

三、右键，选择新建查询

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81480a4846c0181a3af4c264e43&type=med)

四、输入一下语句，并执行

update Mall_Employee set IsEnable=1,IsDelete=0 where LoginName ='admin'

点击执行 ， 显示（1行受影响）代表量置成功 ， 然后重新登录admin就可以了

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81480a4846c0181a3ac734c4e3e&type=max)

<
