---
title: 非品牌机安装windows server 2016或以上版本系统后网卡驱动无法安装解决方法之一
category: 设备与机台
tags: 
source: KMS
updated: 2024-12-20
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81490676e700193e2296ce55a98.html
section: 服务器相关
toc_path: 现场实施知识库 / 服务器相关
author: 梁建宁
kms_id: 00001930
---

# 文档说明

由于windows server 2016或以上的服务器操作系统已经不支持家用组装机的网卡驱动，导致即使驱动是能正常工作也因为windows版本不兼容导致无法安装或者无法识别安装，下述文档则是指引如何强制安装驱动。

# 准备工作

1.将驱动文件下载到对应的电脑中

下载连接：

https://pulic.oss.youcaihua.net/%E5%AE%9E%E6%96%BD%E7%BB%84%E5%AE%89%E8%A3%85%E5%B7%A5%E5%85%B7/6.%E5%B8%B8%E7%94%A8%E9%A9%B1%E5%8A%A8%E7%A8%8B%E5%BA%8F/%E5%AE%9E%E6%96%BD%E7%BB%84_%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%A9%B1%E5%8A%A8%E6%96%87%E4%BB%B6(202412%E4%B8%8A%E4%BC%A0).rar

2.解压驱动文件

3.确认网卡芯片，如果想确认网卡芯片，且服务器原来系统为win10且驱动正常运行情况下，可以利用360驱动大师，先备份驱动，备份时，即可显示对应的驱动型号（虽然这个备份不可用，但是可以知道时什么型号，在下面步骤时就可以减少尝试的次数）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e22855645a92&type=max)

# 注意事项

由于此文件并不是直接安装的驱动工具，所以需要手动导入驱动，需要按照下述步骤试试

# 操作说明

1.打开服务器管理器

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e21192965a51&type=max)

2.右上角点【工具】，选择【计算机管理】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e21247765a52&type=max)

3.选择【设备管理器】-【其他设备】-【以太网控制器】-【属性】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e212d0425a53&type=max)

4.选择【更新驱动程序】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e213d3e25a56&type=max)

5.选择【浏览计算机以查找驱动程序软件】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e2143ad25a58&type=max)

6.选择【从计算机的设备驱动程序列表中选取】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e214deb45a5a&type=max)

7.选择【显示所有设备】，并选择【下一步】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e215ad235a5b&type=max)

8.选择【从磁盘安装】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e216b1c35a5d&type=max)

9.选择【浏览】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e217440c5a5f&type=max)

10.选择下载的文件，并双击打开

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e217e75f5a61&type=max)

11.可以先尝试PRO1000里面的驱动看看行不行，如果不行的再试一下PRO开头的其他文件内容

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e2192c715a64&type=max)

12.选择【WINX64】文件夹，然后选择【WS2022】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e21b33265a69&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e21bb3025a6b&type=max)

13.选择里面的安装信息，先尝试【e1d】，点【打开】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e21c35025a6d&type=max)

14.回到磁盘安装的界面，选择确定

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e21d08e15a6e&type=max)

15.选择列表中的驱动，一般是210结尾或者350结尾居多，主要是看主板用的网口芯片是哪个，这个只能碰下运气了。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e22292d25a7a&type=max)

16.有警告提示，直接点【是】即可

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e2238ec85a80&type=max)

17.完成安装，如果完成不了，从第11步重新选择一下，看看哪个驱动文件可以用就用哪个，多试几次

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700193e22416535a81&type=max)

# 常见问题

1.通过此方法后，依然无法安装驱动咋办

答：找供应商协助处理。

<
