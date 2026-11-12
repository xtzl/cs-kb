---
title: CPCM安装教程：尚莹（黑白）碎票机改造说明
category: 设备与机台
tags: 
source: KMS
updated: 2026-04-01
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a19cff446a019d482a708469a1.html
section: 特殊门店安装流程
toc_path: 现场实施知识库 / 特殊门店安装流程
author: 梁建宁
kms_id: 00002990
---

# 尚莹（黑白）碎票机外观

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d48107cf76910&type=max)

# 准备说明

黑白碎票机改造，油菜花是使用卡头进行改造，需要使用到以下材料

①油菜花卡头一个（需要特殊程序）

②油菜花投币彩票信号线一条

# 改造说明

## 第一步、找到原碎票机主板

如图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d481750a26950&type=max)

## 第二步、确认需要改的线

此款碎票机需要改以下这些线

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d481bd2b16956&type=max)

和MAX碎票机一样，需要先将卡头彩票线端子剪掉，然后保留蓝色线（彩票光眼输出）、绿色线（彩票使能输出）、黑色线（地线）、黄色线（12V）以及红色线（彩票使能输入），其他线不需要。

## 第三步、接线

按照以下线的颜色进行接入

卡头蓝线（彩票输出）--》接碎票机 紫线

卡头绿线（彩票使出）--》接碎票机 灰线

卡头黑线（地线）--》接碎票机 黑线

卡头黄线（12V）--》接碎票机 橘线

卡头红线（彩票使入）--》接碎票机 淡绿色

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d482075f2695b&type=max)

## 第四步、拔掉原主板的排线以及电源

将下图两个位置的线从主板中拔掉

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d482220a2695d&type=max)

注意：接好线后，一定要把主板上的接线端子拔掉，不拔掉还是会用到旧程序

## 第五步、拆除旧卡头并安装固定新卡头

1.拆掉原有卡头,安装卡头底座

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d482a7020699c&type=med)

2.安装卡头底板,注意螺丝不能用电动螺丝刀打会滑丝.或者用更长的螺丝

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d482a7037699d&type=med)

3.穿线绑扎带

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d482a704b699e&type=med)

4.做好内部扎线

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d482a706a699f&type=med)

## 第六步、把小票纸清空拿走，并用电工胶布将小票口封上。

到这步为止，改造完成。

## 第七步、刷通用配置卡，让卡头自动联网，联网后设备会自动注册完成配置

接好线后进行启动机器，刷通用配置卡，卡头链接上网络，会自动进行注册项目

# 改造后测试方法

1.不插卡,塞彩票碎票机不会吸票进去

2.插卡后,塞彩票碎票机会吸票并且开始计数

# 常见问题

问：碎票后，还会进行打印散客暂存彩票小票，这个该如何处理

答：需要把小票打印机的打印纸去除掉，然后再小票打印机的打印口贴上电工胶布，模拟小票纸存在，没有纸，只会空转，但是不会打印小票。如果直接把小票去除或者把小票模块去除，机器会报错。

问：碎票后，卡头已经保存彩票成功，但是碎票机记票屏幕还显示上次存票数，没有清零。

答：看看主板上的绿线是否有接对，绿线接口第一个和最后一个易接反。

<
