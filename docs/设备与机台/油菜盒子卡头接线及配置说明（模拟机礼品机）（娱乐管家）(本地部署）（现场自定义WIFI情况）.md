---
title: 油菜盒子卡头接线及配置说明（模拟机礼品机）（娱乐管家）(本地部署）（现场自定义WIFI情况）
category: 设备与机台
tags: 
source: 语雀·油菜花硬件
updated: 2026-03-02
url: https://ychylb.yuque.com/staff-gcg8pk/hg1x92/xdf4v5rap37f17ek
section: 娱乐管家系统
toc_path: 娱乐管家系统 / 卡头类 / 反扫卡头/果冻卡头调试说明 / 油菜盒子调试说明
---

# **<font style="color:#333333;">一、 作业说明</font>**
<font style="color:#333333;">新到场地的盒子要与场地系统连接，就要安装接线与配置，下列为油菜盒子的安装说明</font>

# **<font style="color:#333333;">二、卡头外观</font>**
![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179996713-005dad1c-ea4e-4c5a-a378-1b1b15145dc2.jpeg)

# **<font style="color:#333333;">三、作业准备</font>**
### **<font style="color:#333333;">工具准备</font>**
<font style="color:#000000;">1.扎带（若干）</font>

<font style="color:#000000;">2.3M双面胶</font>

<font style="color:#333333;">*注意：工具准备清单目录请参考：</font>[<u>链接</u>](http://kms.gzych.vip/webdoc/real/Pub4028801e784962e1017af550e00c4c1f.html?OPERATE=3&STATE=0)

### **<font style="color:#333333;">网络准备</font>**
<font style="color:#333333;">第三方网络设备请参考此文档进行配置</font>[《<u>第三方网络配置要求</u>》](http://kms.gzych.vip/webdoc/real/Pub2c93a81490676e7001914b14df55705f.html?OPERATE=3&STATE=0)

### **<font style="color:#333333;">系统准备</font>**
<font style="color:#333333;">娱乐管家系统版本升级为10.3.6171以上版本</font>

# **<font style="color:#333333;">四、 注意事项</font>**
<font style="color:#333333;">1.卡头安装前，必须机台处于断电情况；</font>

# **<font style="color:#333333;">五、固定标准</font>**
<font style="color:#333333;">1.油菜盒子内置在机台里面，并且通过扎带或者双面胶固定在机台内部</font>

<font style="color:#333333;">2.油菜盒子的天线，尽量外置摆放，并且保持垂直，部分特殊机台无法外置情况下，也要保证油菜盒子天线垂直并且不与机台内壁接触。</font>

<font style="color:#333333;">3.接线后，线路需要整理梳理好，用扎带固定，且要求不能影响机台正常功能，包括不影响调试机台、回收硬币，打开检修口等操作。</font>

# **<font style="color:#333333;">六、接线标准</font>**
## **<font style="color:#333333;">1.油菜盒子认识</font>**
<font style="color:#333333;">    油菜盒子的样式图，如图所示：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179996921-98e409f2-687c-4679-aaaf-8115285f4e9f.jpeg)

## **<font style="color:#333333;">2.油菜盒子线材认识</font>**
<font style="color:#333333;">    线材样式图，如图所示：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179997098-fc9b418e-ebda-4f94-80b8-a17839ea489a.jpeg)

<font style="color:#333333;">    线材说明：</font>

<font style="color:#333333;">        黄色线--电源12V线；  </font>

<font style="color:#333333;">        黑色线--地线；</font>

<font style="color:#333333;">        灰色线--投币输出线；</font>

<font style="color:#333333;">        绿色线--投币输入线；</font>

## **<font style="color:#333333;">3.油菜盒子接线说明</font>**
<font style="color:#333333;">a.按下图对机台线路进行接入，如图所示：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179997327-5026bf21-053d-43d7-aeb7-25d5f3c778b4.jpeg)

<font style="color:#333333;">    b.油菜盒子实际接线说明：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179997605-0a88093d-a74b-404b-b1e4-6b4378157051.jpeg)

<font style="color:#333333;">说明：</font>

<font style="color:#333333;">假如该机台是接入协议线情况下，不需要再接入其他线材（天线除外），包括投币输入线、投币输出线和礼品线。</font>

<font style="color:#333333;">反之，如果该机台不支持接入协议，则需要接除协议线外其他线路。</font>

# **<font style="color:#333333;">七、后台配置说明</font>**
## **<font style="color:#333333;">1.获取场地WiFi信息</font>**
<font style="color:#333333;">如果现场网络设备并非使用标准网络设备情况下，则需要提前了解现场无线网络是否符合使用要求。</font>

<font style="color:#333333;">要求如下：</font>

<font style="color:#333333;">①无线名称和密码必须不含有中文和符号</font>

<font style="color:#333333;">②给予卡头使用的无线网络为2.4G网络，且不能使用双频合一或2.4G和5G设置同一个WIFI名称密码</font>

<font style="color:#333333;">③无线网络DHCP服务功能需要开启，且自动分配的IP地址数量需要大于现场安装卡头数量，可修改LAN口配置参数中的【子网掩码】来增加地址范围</font>

<font style="color:#333333;">④DHCP服务中，dns首选需要固定成119.29.29.29，否则可能会影响扫码游戏</font>

<font style="color:#333333;">⑤无线网络中的WIFI加密方式为WPA-PSK/WPA2-PSK</font>

## **<font style="color:#333333;">2.配置卡的配置说明</font>**
### **<font style="color:#333333;">1.配置通用配置卡二维码</font>**
<font style="color:#333333;">路径如下：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179997858-330dbfa5-4cdf-4982-a6f8-4cbac2e5d089.jpeg)

<font style="color:#333333;">输入服务器地址和端口，服务器地址一般为192.168.**.**，默认端口为9999，</font>

<font style="color:#333333;">若不知道如何查看本地ip地址，可参考以下文档进行查看：</font>

[<u>win2012服务器电脑如何查看IP和端口-百度经验 (baidu.com)</u>](https://jingyan.baidu.com/article/48b37f8df201691a6564887c.html)

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179998075-4bc7b328-866e-44e4-9f9b-c8fc269a16a9.jpeg)

<font style="color:#333333;">填入现场无线网络的WIFI名称和密码，点击保存完成设置</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179998264-b6589bb5-ec9b-4091-adbd-6fa959db565d.jpeg)

<font style="color:#333333;">点击服务器地址同步到游智云，并将空白卡放置到读卡器中，并启用油菜助手后点击【网络参数写入配置卡】完成配置卡写入。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179998438-c9012faf-ddf1-4ae5-a96a-83a1925e5f2f.jpeg)

### **<font style="color:#333333;">2.将读卡模块接入到盒子端的【扫码】接口中，并将会员卡放置到读卡模块中，长按盒子的【设置键】5~10秒，等待盒子读取配置信息，等待盒子连接。</font>**
![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179998641-592091a4-fb4d-48b2-8996-93a91a132745.jpeg)

### **<font style="color:#333333;">3.油菜盒子连接状态</font>**
<font style="color:#333333;">油菜盒子连接成功，并常亮绿色【电源】【联网】【强度】三个灯，【待机】灯闪烁红灯，证明已经进入带配置模式。如果未显示该灯号，按解绑键5S后，等待待机灯快闪，即可进入配置模式。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179998891-3a193d88-3f61-4c12-a2f3-7a285ebae64e.jpeg)

## **<font style="color:#333333;">3.项目创建、配置及调试</font>**
### **<font style="color:#333333;">1.项目创建</font>**
<font style="color:#333333;">手机连上卡头使用的无线网络后，打开手机微信端，用扫一扫，打开手机浏览器，扫描通用配置卡二维码</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179999232-96c7b0a3-850c-4162-9a9e-b99afeae9fb8.jpeg)<font style="color:#333333;"> </font>![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179999560-4b7d9226-6d9a-452d-92e7-f24db805d7dc.jpeg)

<font style="color:#333333;">进入配置界面，点击【新增】，创建该模拟机/礼品机机台项目类型</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732179999772-57951e02-acad-4284-96c3-a180c1697311.jpeg)<font style="color:#333333;"> </font>![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732180000029-800a6ee8-274d-47a7-bc97-a4800cea6780.jpeg)

<font style="color:#333333;">点击项目分类栏，在弹窗点击刚创建的模拟机/礼品机-机台类型</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732180000294-0386794f-caa1-4565-b8cf-aaf22c63f297.jpeg)

<font style="color:#333333;">补充填写该项目信息，完善项目资料，录入完成后点击保存，创建完成。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732180000641-12a4f110-780f-461c-9e06-3eb41510fcf6.jpeg)<font style="color:#333333;"> </font>![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732180001366-53966a74-6fd3-4c60-859b-5fb8c24fa1e3.jpeg)

### **<font style="color:#333333;">2.卡头关联绑定项目</font>**
<font style="color:#333333;">点击添加端口，在跳转界面输入 </font>**<font style="color:#333333;">卡</font>**<font style="color:#333333;"> </font>**<font style="color:#333333;">头显示的编号，点击提交</font>**

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732180001607-e5d3489f-29ad-40e0-9c72-89f965f3eb96.jpeg)<font style="color:#333333;"> </font>![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732180002003-6f9027b2-f3bb-47e1-bc94-9dde2b261f8f.jpeg)

# **<font style="color:#333333;">八、测试要求</font>**
#### **<font style="color:#333333;">投币信号匹配测试</font>**
<font style="color:#333333;">使用实物币投币，机台能正常启动，并且后台【项目消费查询】能查询到对应投币数据，连续测试10次，均为正常代表测试通过；</font>

#### **<font style="color:#333333;">礼品信号匹配测试</font>**
<font style="color:#333333;">将礼品扔到出礼品口，模拟出礼品过程，机器显示中奖，油菜花后台记录【出礼品查询】，则完成礼品测试过程；</font>

#### **<font style="color:#333333;">投币信号高低电平匹配测试</font>**
<font style="color:#333333;">机台断电，等30秒后上电，机台上电后，机台报错误，则代表参数设置正常；</font>

#### **<font style="color:#333333;">扫码游戏功能测试</font>**
<font style="color:#333333;">通过微信扫码，选择已设置的扫码游戏方案，会员扣除储值数与机台上币数一致。</font>

# **<font style="color:#333333;">九、 常见问题</font>**
<font style="color:#333333;">WIFI信号弱</font>

<font style="color:#333333;">答：将天线引出来</font>

<font style="color:#333333;">计数不准</font>

<font style="color:#333333;">答：可能性有几种</font>

<font style="color:#333333;">1.信号弱，盒子会保留累计数据，等待信号恢复一定强度后再一次性上传，此时系统记录的时间是上传时间并不是实际游玩时间</font>

<font style="color:#333333;">2.投币信号电平不对，调整盒子电平</font>

<font style="color:#333333;">3.礼品线线序错，可手动改线调整线序</font>
