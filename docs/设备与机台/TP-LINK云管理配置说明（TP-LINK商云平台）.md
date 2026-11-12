---
title: TP-LINK云管理配置说明（TP-LINK商云平台）
category: 设备与机台
tags: 
source: KMS
updated: 2022-05-05
url: https://kms.gzych.vip/webdoc/view/Pub8a92809980511fee018094e279fd1378.html
section: 网络调试安装
toc_path: 现场实施知识库 / 网络调试安装
author: 梁建宁
kms_id: 00001164
---

# 一、说明

本文档用于将客户购买指定网络设备后，如何加入到TP-LINK商云平台中的操作方法以及简单问题排查；遇到网络调试问题可通过共享平台信息来达到快速排查问题的途径。

# 二、功能说明

使用商云平台，可通过云平台快速推算出网络架构，并可进行远程调试

# 三、准备工作

1.手机下载TP-LINK商云APP
2.现场网络已经按照标准规格调整完毕
3.现场已经通外网
4.路由器都开启云管理功能
5.开通油菜花组织的子账号（可联系油菜花实施组组长进行开通）

可通过应用市场搜索【TP-LINK商云】来下载

登录名称为，自己姓名拼音@ych

# 四、注意事项：

1.由于绑定时，云平台会判断登录路由器设置的管理密码是否带“.”，所以设置路由器的管理密码建议统一设置为****（已脱敏，请向运维索取）

2.绑定时，不要将网络设备绑定到其他门店

3.绑定前，务必确认整个网络已经处于通外网状态

# 五、流程操作

## 电脑端：

### 步骤一：如何登录

1.打开TP-LINK商云平台网页

网址如下：

https://smbcloud.tp-link.com.cn/login.html

2.使用子账号登录，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920d74981d2e09&type=max)

### 步骤二：添加项目（添加门店）

1.点击【添加项目】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920d7722e12e1c&type=max)

2.填写项目名称，名称以门店编码+门店名称命名，例如“00052345-油菜花演示”

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920d7953b92e29&type=max)

### 步骤三：绑定网络设备

1.点击刚刚添加的项目

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920d83302a2e76&type=max)

2.选择【添加网络设备】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920d849dca2e7a&type=max)

3.提示分组，选择默认分组，点击【继续】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e406a8632a8&type=max)

4.选择【用MAC地址添加】，并按照下述要求填写内容（如果可以看到设备底部的二维码，也可以选择设备ID添加，通过输入设备底部二维码ID来绑定）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e51a63a330b&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e52e1c73311&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e5412fc331e&type=max)

5.点击【添加】完成添加，注意，只需要添加主路由和隔离路由即可，如果有AC控制器，需要AC也添加到该项目。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e55d9ee3325&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e569ce43326&type=max)

## 手机端：

### 步骤一：下载APP，并登录app

1.扫一下二维码可以下载对应的app

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e5a72dd3339&type=max)

2.打开TP-LINK商云APP，选择子账号，并输入自己的账号及密码

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e6641333374&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e66a46b3378&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e67262e337a&type=max)

### 步骤二：添加项目（添加门店）

1.在企业《广州油菜花信息科技有限公司》中，新增项目，名称命名规则为门店编号+门店名称，如下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e67c8353380&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001920e6e353633ac&type=max)

### 步骤三：在此项目中添加设备

情况一：如果已经接入无线信号可选择无线添加

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e1325a136b&type=med)

情况二：如果没有加入无线网络则可通过扫码添加

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e13269136c&type=med)

情况三：如果没有接入无线网络且二维码不清晰可通过手动添加

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e13279136d&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e13279136e&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e13289136f&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e132891370&type=med)

4.添加设备时需要填入该设备的管理员账号以及密码，并为此设备命名

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e132981371&type=med)

5.添加成功后如下图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e132a81372&type=med)

# 六、操作标准

1.需要将主路由、主交换机、隔离路由器、POE交换机、AC控制器、AP均添加到平台中

# 6、其他功能

1.可以在网络管理中选择【拓扑网络】来查看现场网络架构是否符合需求，但只能参考不能作为准确判断标准,如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e132b81373&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e132b81374&type=med)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=8a92809980511fee018094e132c71375&type=med)

<
