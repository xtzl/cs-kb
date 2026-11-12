---
title: 01-2-2 NET Framework 3.5运行环境安装说明（windows 2012版本）
category: 系统与设置
tags: 
source: KMS
updated: 2021-07-21
url: https://kms.gzych.vip/webdoc/view/Pub4028801e784962e1017ac6ee44483b0f.html
section: 服务器相关
toc_path: 现场实施知识库 / 服务器相关
author: 杨晓华
kms_id: 00000380
---

# 一、 作业说明：

此步骤为安装数据库的前置步骤，仅在服务器上安装即可，在安装SQL2008数据库前必须先启动服务器中的Net Framework 3.5功能，否则会导致数据库无法正常安装。

此步骤分为windows server 2008 R2版本和windows server 2012 R2版本，不同的版本安装方式有所差异，请务必注意。

# 二、 作业准备：

1. 准备windows server 2012 R2镜像或者镜像内的sxs文件夹

Sxs文件夹下载链接：

https://pulic.oss.youcaihua.net/实施组安装工具/2.本地服务器运行环境/油菜花工具包_6.常用软件工具_运行环境引用文件_2012系统.net3.5应用文件.rar

# 三、 作业标准

Net Framework 3.5在启用状态。

# 四、 作业步骤

1. 把下载好的sxs文件放到D盘目录下，如D:\SXS\,如果准备的是镜像，则打开镜像，在镜像目的下找到\sources\sxs文件夹

2. 点击左下角服务管理器，点添加角色和功能

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac6e7bbbc3b03&type=max)

3. 一直下一步到功能，选择.net3.5功能，点下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac6e88aa53b04&type=max)

4. 点击指定备用源路径，（如有联网情况下可尝试跳过此步骤尝试是否能直接安装完成）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac6ebac863b07&type=max)

5. 复制SXS文件夹路径到备用源路径内。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac6eccb253b0a&type=max)

6. 在这里填写，注意后面是有“\”

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=4028801e784962e1017ac6ed9ba43b0c&type=max)

7. 最后点确定，点安装，等待安装成功。

下一步：安装NET Framework 4.5运行环境

<
