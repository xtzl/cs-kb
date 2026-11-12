---
title: VPN服务端配置流程（部署VPN服务器用）
category: 系统与设置
tags: 
source: KMS
updated: 2026-04-14
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a19cff446a019d89b1c87642de.html
section: 网络调试安装
toc_path: 现场实施知识库 / 网络调试安装
author: 梁建宁
kms_id: 00003042
---

# 文档说明

当客户使用云服务器时，并且门店为本地服务器且无公网IP时，则门店服务器需要通过VPN来链接。我们可以利用客户自己的云服务器搭建VPN服务器，并通过VPN软件构建自己的VPN网络实现门店和总部数据互通。

# 前期准备

1.VPN服务器端和客户端下载

VPN服务端下载链接：https://nos-pulic.oss-cn-shenzhen.aliyuncs.com/实施组安装工具/4.本地服务器必要安装软件/VPN服务端安装包（部署VPN服务器用）.exe

VPN客户端下载链接：https://nos-pulic.oss-cn-shenzhen.aliyuncs.com/实施组安装工具/4.本地服务器必要安装软件/油菜花工具包_2.服务器安装必要软件及环境_VPN客户端.exe

2.准备云服务器一台，需要带有公网IP

3.需要提前开通5555TCP的访问端口（可以改成其他，需要提前开放给VPN使用）

# 具体操作方法

## 第一步：安装VPN服务端并配置

1.打开VPN服务端安装包。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80bd94285&type=med)

2. 选择vpn Server

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80bdd4286&type=med)

3. 选中同意许可，然后点击下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80be14287&type=med)

4. 下一步就好

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80be74288&type=med)

5. 需要的话就变更安装的目录，也可以默认

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80bef4289&type=med)

6. 点击下一步开始安装

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80bf4428a&type=med)

7. 等待安装结束，点击完成即可。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80bf8428b&type=med)

8. 点击桌面【SoftEther VPN Server管理工具】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80bfd428c&type=med)

9. 直接选中本地主机，并点击连接

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c03428d&type=med)

10. 接着会提示你先设置密码，此处是设置管理员密码，以后登录vpn服务器时使用

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c07428e&type=med)

11. 下一步选择网络模式，选择【远程访问VPN Server】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c0c428f&type=med)

12. 选完后下一步就会提示你vpn的sever会被初始化，点确定就好

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c124290&type=med)

13. 设置服务器端的vpn名称的，填完后点确定

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c174291&type=med)

14. 这里无需理会，直接点退出

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c1b4292&type=med)

15. 这里也不需要理会，直接点确定就好

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c204293&type=med)

16. 这里选择禁用vpn Azure，然后点确定

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c254294&type=med)

17. 到了这步，是给客户端创建用户的：选择创建用户

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c2a4295&type=med)

18. 这个界面的解析，只需要填写用户名和密码这里设置的是客户端登录的密码，是用于客户端登录的密码用

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c2e4296&type=med)

19. 这里是你创建的用户名，能看到登录的次数，和上次登录的时间

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c324297&type=med)

20. 然后回到这个界面，再次点击连接

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c384298&type=med)

21. 在上个界面点击链接，会输入管理员密码后，出现下面的界面点解管理虚拟HUB

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c3e4299&type=med)

22.点完后会出现下面的界面，选择虚拟NAT和虚拟DHCP服务器

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c44429a&type=med)

23. 点击启用SecureNAT就好

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c4a429b&type=med)

24. 提示是否启用，点确定

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c50429c&type=med)

25. 回到启用的界面，看到SecureNAT已经启用状态

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c55429d&type=med)

至此，vpn服务器设置完成，接着我们需要安装VPN客户端来配置这个服务器的IP地址。

## 第二步：安装VPN客户端来完成总部服务器的VPN的连接

26.双击运行安装程序

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c59429e&type=med)

27. 点击下一步，出现下面界面，选择第一个【SoftRther VPN Client】,点击下一步。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c5e429f&type=med)

28. 勾选“我同意最终用户许可协议”，点击一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c6342a0&type=med)

29. 直接点击下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c6842a1&type=med)

30. 选择安装目录之后，点击下一步。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c6d42a2&type=med)

31. 等待安装完成之后，点击完成即可。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c7242a3&type=med)

32. 打开SoftEther VPN Client 管理工具

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c7842a4&type=med)

33. 在下面虚拟网络适配器名列表中右键选择‘创建新虚拟网络适配器’

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c7d42a5&type=med)

34. 填写对应的网络适配器名，点击【OK】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c8242a6&type=med)

35. 在下面虚拟网络适配器名就出现新的虚拟网卡。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c8642a7&type=med)

36. 右键‘虚拟网络适配器名’下的空白处，选择【打开Windows网络连接】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80c8c42a8&type=med)

37. 右键刚刚设置的VPN连接，并点击属性

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80ca542a9&type=med)

38. 选择【Internet协议版本4（TCP/IPV4）】,点击属性。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80cad42aa&type=med)

39. 固定本机VPN的IP地址，并填写对应的子网掩码，注意不要填写网关，点击确认

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80cb642ab&type=med)

40. 返回管理器界面，点击创建新的VPN连接，并填写相关信息。如下图所示

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19cff446a019d89a80cbb42ac&type=med)

注：其他参数不需要做修改。

41. 点击连接，测试连接是否正常即可。

<
