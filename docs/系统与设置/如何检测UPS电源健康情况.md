---
title: 如何检测UPS电源健康情况
category: 系统与设置
tags: 
source: KMS
updated: 2026-04-17
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a19cff446a019d992bb4bb4cc9.html
section: 服务器相关
toc_path: 现场实施知识库 / 服务器相关
author: 梁建宁
kms_id: 00003048
---

# 文档说明

UPS电源是维护服务器正常运行的必要保障。UPS电源在场地断电情况下可以保障服务器依然可以正常运行，从而有充足时间为服务器正常关机避免突然断电导致服务器异常。此文档用于日常检查UPS电源是否处于正常的状态。

此文档以雷迪司H1500此产品来说明如何进行检查。

# 检查过程

## 1.在通市电模式下，以此点击屏幕下方按钮，观察显示检查是否有异常，如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d991847944cb0&type=max)

注意：输出电压一般在198V~235.4V‌ 之间为正常。高于或者低于此范围都属于异常，异常电压会容易导致服务器损坏。出现此情况代表电池需要维修。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d991a31044cb1&type=max)

注意：输入电压一般在198V~235.4V‌ 之间为正常。高于或者低于此范围都属于异常，异常电压会容易导致电池（UPS）损坏。出现此情况需要检查门店电路是否有异常。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d991b8dc14cb4&type=max)

注意：此负载值代表目前电池的链接设备的负荷数，超过100%代表过载，需要减少接连到电池的设备。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d991d395c4cb6&type=max)

注意，此界面为电池容量，在未停电状态下，电池容量如果少于100%，则代表电池有异常，需要维修。

## 2.服务器关机，并断开市电，检查电池情况。

2.1先听声音，电池模式下，电池应每个10秒鸣响一次。

2.2依次按屏幕下方按钮，检查电池状态

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d9925594b4cbd&type=max)

注意：如果电池容量快速下落，有可能电池寿命不足，需要更换新UPS。

# 其他常见报错

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d992ba4bf4cc6&type=max)

# UPS电源使用注意事项

1.不要过多接入负载设备，一般只接入服务器电脑主机以及显示屏幕，用于断电时可用于正常关机使用。过多的负载会降低电池可用时间，导致没有足够时间让服务器正常关机。

2.UPS请放置在通风位置，避免散热不足。本身UPS会产生一定热量，如果放置在密封环境会导致UPS无法正常散热导致寿命下降

3.UPS不要接入启动电源较大的设备，如扫码仪或者激光打印机等设备。启动电源过大会导致UPS损坏。

# UPS电源说明书下载

详细内容可下载该说明书进行阅读

下载链接：

https://nos-pulic.oss-cn-shenzhen.aliyuncs.com/%E5%AE%9E%E6%96%BD%E7%BB%84%E5%AE%89%E8%A3%85%E5%B7%A5%E5%85%B7/8.%E5%B8%B8%E7%94%A8%E6%96%87%E6%A1%A3%E7%95%99%E5%BA%95/%E9%9B%B7%E8%BF%AA%E5%8F%B8%EF%BC%88LADIS%EF%BC%89H%E7%B3%BB%E5%88%97%E5%90%8E%E5%A4%87%E9%95%BF%E5%BB%B6%E6%97%B6%E4%B8%8D%E9%97%B4%E6%96%AD%E7%94%B5%E6%BA%90%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%E6%89%8B%E5%86%8C.pdf

<
