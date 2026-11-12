---
title: 自助售货机配置说明（游乐宝）（WIFI版）
category: 库存与采购
tags: 
source: 语雀·油菜花硬件
updated: 2026-03-02
url: https://ychylb.yuque.com/staff-gcg8pk/hg1x92/xo6z4eacocnk7arg
section: 娱乐管家系统
toc_path: 娱乐管家系统 / 游乐宝系统 / 其他类 / 售货机
---

# **<font style="color:#333333;">一、作业说明</font>**
<font style="color:#333333;">本文旨在用于指导自助售货机的安装</font>

# **<font style="color:#333333;">二、外观展示</font>**
![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244405490-58a48bff-6e40-484f-addb-1968fee3bd77.jpeg)

# **<font style="color:#333333;">三、安装准备</font>**
<font style="color:#333333;">1. 十字螺丝刀*1  
</font><font style="color:#333333;">2. 放置位置预留设备电源</font>

<font style="color:#333333;">3. 现场预留给设备使用的无线网络</font>

<font style="color:#333333;">4. 读卡器*1</font>

<font style="color:#333333;">5. 会员卡*1</font>

<font style="color:#333333;">6. 提前准备好服务器连接域名地址（该设备只支持域名连接）</font>

<font style="color:#333333;">7. 手机*1</font>

<font style="color:#333333;">8.系统版本：</font><font style="color:#E56600;">游乐宝8.1.6404以上，娱乐管家10.3.4453以上</font>

# **<font style="color:#333333;">四、安装标准</font>**
<font style="color:#333333;">1.自助售货配件安装到位（顶部发光字）</font>

<font style="color:#333333;">2.自助售货机天线垂直立正</font>

<font style="color:#333333;">3.自助售货机地脚已固定</font>

<font style="color:#333333;">4.自助售货机连接系统正常，功能能正常使用（包括加货功能、兑换功能以及售货功能均正常）</font>

<font style="color:#333333;">5.培训客户使用售货机（包括如何加货、如何更换货物和如何兑换使用）</font>

# **<font style="color:#333333;">五、注意事项</font>**
<font style="color:#333333;">1.售货机运输要求会将货道用扎带进行固定，安装前需要将扎带全部清理完毕</font>

<font style="color:#333333;">2.售货机重量比较重，请至少两个人以上进行搬运，避免发生倾倒</font>

<font style="color:#333333;">3.由于售货机网络要求较高，请提供专用无线网络给予售货机使用，避免因为无线网络不稳定导致功能异常</font>

# **<font style="color:#333333;">六、作业步骤</font>**
## **<font style="color:#333333;">第一步：配件安装</font>**
<font style="color:#333333;">配件清单：发光字</font>

<font style="color:#333333;">1.发光字</font>

<font style="color:#333333;">售货机顶部有发光字，直接安装到顶部即可，并接入预留电源即可</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1584417/1732244405813-53988c4f-7f85-4227-a095-a1d78884f56e.png)

<font style="color:#333333;">2.天线</font>

<font style="color:#333333;">顶部天线将其树立</font>

<font style="color:#333333;">3.地脚</font>

<font style="color:#333333;">将地脚打到底，使售货机不摇晃</font>

## **<font style="color:#333333;">第二步：现场网络设置</font>**
### **<font style="color:#333333;">情况一：现场无线网络可自定义，且支持长wifi名，则可使用自动连接wifi的连接方式进行设置，不需要使用配置卡进行配置</font>**
<font style="color:#333333;">1.在后台生成通用WIFI</font>

<font style="color:#333333;">路径：游乐宝后台→设置→卡头wifi通讯→通用配置卡</font>

<font style="color:#333333;">在【通用配置卡】界面，点击【重新设置通讯网络】</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244406035-6b0b3425-ebed-4917-9668-c72aa9b3de9b.jpeg)

<font style="color:#333333;">2.选择【外场】，并输入域名地址，一般域名地址为：y********.yun.youcaihua.net，端口为88，然后点下一步</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1584417/1732244406316-ba07922f-85d9-4b75-aad5-08710aefc9ae.png)

<font style="color:#333333;">3.点【生成自动连接WIFI】，这里会自动生成特定wifi名称和密码，注意不要修改生成的WIFI名称和密码，直接将自动生成的WIFI名称和密码配置到现场给售货机使用的网络设备中。此界面点击下一步，完成设置。</font>

<font style="color:#E53333;">特别提醒：该设备WIFI只支持2.4G网络，所以需要将WIFI中的双频合一功能关闭掉</font>

<font style="color:#333333;">网络配置参考可参照以下配置文档：</font>



![](https://cdn.nlark.com/yuque/0/2024/png/1584417/1732244406510-f721f685-a2ce-4fcf-b4b6-5e7550594060.png)

<font style="color:rgb(51, 51, 51);">《</font>[<font style="color:rgb(79, 124, 206);">游乐宝/娱乐管家云服务器网络调试文档，适用范围：油菜盒子</font>](http://kms.gzych.vip/webdoc/real/Pub2c93a81485aecc240186815bd4a64cde.html?STATE=0&OPERATE=3)<font style="color:rgb(51, 51, 51);">》</font>

<font style="color:rgb(51, 51, 51);">《</font>[<font style="color:rgb(79, 124, 206);">游乐宝/娱乐管家本地服务器网络调试文档，适用范围：油菜盒子（低配版AP方案）（本地服务器）</font>](http://kms.gzych.vip/webdoc/real/Pub2c93a81485aecc24018712c0fa8c2053.html?STATE=0&OPERATE=3)<font style="color:rgb(51, 51, 51);">》  
</font><font style="color:rgb(51, 51, 51);">《</font>[<font style="color:rgb(79, 124, 206);">游乐宝/娱乐管家本地服务器网络调试文档，适用范围：油菜盒子（中配版AP方案）（本地服务器）</font>](http://kms.gzych.vip/webdoc/view/Pub2c93a81485aecc2401872722a42e2b6f.html)<font style="color:rgb(51, 51, 51);">》  
</font><font style="color:rgb(51, 51, 51);">《</font>[<font style="color:rgb(79, 124, 206);">游乐宝/娱乐管家本地服务器网络调试文档，适用范围：油菜盒子（高配版AP方案）（本地服务器）</font>](http://kms.gzych.vip/webdoc/real/Pub2c93a81485aecc240187278bbad42d4c.html?STATE=0&OPERATE=3)<font style="color:rgb(51, 51, 51);">》  
</font><font style="color:rgb(51, 51, 51);">《</font>[<font style="color:rgb(79, 124, 206);">游乐宝/娱乐管家网络调试文档，适用范围：油菜盒子（无线方案）（云服务器、本地服务器通用）</font>](http://kms.gzych.vip/webdoc/view/Pub2c93a81485aecc240187309c2d7d340b.html)<font style="color:rgb(51, 51, 51);">》</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1584417/1732244406738-87c1cbc0-af6a-49d1-bf55-1909975358e7.png)



### **<font style="color:#333333;">情况二：现场无线网络不可自定义，或者使用不支持长wifi名设备（锐捷/锐易），则可设置自定义WIFI名称连接，并需要读卡器写配置卡</font>**
<font style="color:#333333;">现场网络配置步骤如下：</font>

<font style="color:#333333;">1.修改后台通用配置卡信息</font>

<font style="color:#333333;">路径：设备→基础设置→卡头 wifi 通讯设置→通用配置卡</font>

<font style="color:#333333;">在【通用配置卡】界面，选择【重新设置通讯网络】，并选择【外场】，输入服务器域名地址，一般域名地址为：y********.yun.youcaihua.net，端口为88，然后点下一步</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244406923-acf8a2ec-c76a-4e80-b3d1-9c0e769d1e79.jpeg)

<font style="color:#333333;">输入现场给予售货机使用的无线网络名称和对应的连接密码，点下一步。</font>

<font style="color:#333333;">注意：此WIFI需要符合以下要求</font>

<font style="color:#333333;">a.无线WIFI需要是2.4G无线网络，并且不支持双频合一功能，如现场网络开启了双频合一功能需要关闭掉。</font>

<font style="color:#333333;">b.此无线WIFI名称和密码不能有符号和中文，必须纯英文或者纯数字或者是英文加数字组合。</font>

<font style="color:#333333;">c.无线WIFI需要能通外网</font>

<font style="color:#333333;">d.无线WIFI不能是隐藏网络</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1584417/1732244407265-9cb27fb0-7861-43d6-b2eb-6b978e536fec.png)

<font style="color:#333333;">点击同步至游智云，完成现场网络配置。</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1584417/1732244407629-9e66d6ba-1c01-4052-8aca-04e202185733.png)

## **<font style="color:#333333;">第三步：售货机联接网络</font>**
<font style="color:#333333;">说明：</font>

<font style="color:#333333;">当现场为上一步骤</font>**<font style="color:#E53333;">情况一</font>**<font style="color:#333333;">，则售货机会自动联网进入到带配置过程，可跳过此步骤；</font>

<font style="color:#333333;">当现场为上一步骤</font>**<font style="color:#E53333;">情况二</font>**<font style="color:#333333;">，则售货机需要刷通用配置卡才能联网，请按照下述步骤进行操作。</font>

<font style="color:#333333;">1.将空白卡放置到读卡器上，并在通用配置卡界面，点【网络参数写入配置卡】</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244407930-8d896146-82c4-4adc-978d-1b78be46b80f.jpeg)

<font style="color:#333333;">2.用十字螺丝刀卸掉背面的防尘网，拉出通讯盒子,并将售货机进行通电。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244408190-dd6d7a52-4e28-4ff4-9f14-197a41cc3e66.jpeg)![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244408420-fb950d1d-0bff-4164-9d09-3d88ca4e9819.jpeg)![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244408701-70e9e7a4-4281-428b-9f70-a155639f6344.jpeg)

<font style="color:#333333;">3.将读卡模块接入到通讯盒子，并长按通讯盒子的设置键5~10秒后将刚刚写好的配置卡放置到读卡模块中进行读取。联网成功后，盒子会显示【电源】【联网】【强度】都常亮绿色灯，【待机】显示红色闪烁。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244409021-6999aba0-2d80-4de7-998c-04d02ed70929.jpeg)

## **<font style="color:#333333;">第四步：配置售货机</font>**
<font style="color:#333333;">1. 在机台取货口找到设备二维码码，并记下该码，若找不到设备盒子码，也可在机身后部查找到。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244409207-e6e72462-373f-46bd-8f5c-c1f8f1d6fc14.jpeg)

<font style="color:#333333;">3. 登录系统后台，新建一个售货机项目，输入设备码进行绑定，并标记填写设备名称</font>

<font style="color:#333333;">路径：设备→设备管理→ 营业设备</font>

<font style="color:#333333;">在营业设备界面中点击【新增】，选择【自助售货机】并填写设备盒子码</font>

<font style="color:#333333;">展示如图：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244409500-07d6460e-e258-496c-b0bc-83274f2c6dd3.jpeg)

<font style="color:#333333;">4. 找到刚才创建的项目，设置售货机仓库，及自助售货机货道，如图所示：</font>

<font style="color:#333333;">设置售货机仓库：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244409800-5b8e7f0f-2aa7-4f4c-945b-39151919adb1.jpeg)

<font style="color:#333333;">设置货道数量，请根据实际情况选择，一般为36货道6*6；</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244410195-b51dbb35-ff6f-4f15-9589-24cefbd17d30.jpeg)

<font style="color:#333333;">设置售货方式，支持仅购买（只支持微信支付）、仅兑换、或者两者都支持</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1584417/1732244410484-1d246750-b810-4f6b-a7b6-171907af015b.png)

<font style="color:#333333;">下载消费二维码：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244410748-dedbaae7-ab08-469c-96d1-f87a4e062859.jpeg)

<font style="color:#333333;">5. 将该消费二维码打印出来，并贴于售货机上</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244411179-c298fe6f-574b-41a4-8f26-48d496e03092.jpeg)

<font style="color:#333333;">6.在后台设置小程序支付（如有可跳过）</font>

<font style="color:#333333;">路径：后台→财务→支付方式</font>

<font style="color:#333333;">在【支付方式】中，点击【新增】，在支付类型中选择“小程序支付”，并填写支付名称，保存该支付方式。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244412176-18731cd5-4c52-4a0d-8ec2-6133965ee3d3.jpeg)

## **<font style="color:#333333;">第五步：新建售货机需要上架的商品并添加库存到仓库</font>**
<font style="color:#333333;">说明：一般门店会将售货机库存单独设置一个仓库进行管理，当门店采购商品回来后，会先入到门店主仓库，只有在售货机缺货时才通过系统调拨的功能调拨到售货机仓库，以下流程为采购入库到门店主仓库的流程。</font>

<font style="color:#333333;">1.后台设置零售商品，设置定价及初始化库存。（新商品适用，已有商品请直接看第5点）</font>

<font style="color:#333333;">商品设置路径：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244412561-8ab04dc9-7dd6-4674-9dc3-a259b4fe2398.jpeg)

<font style="color:#333333;">2.单个商品可以以这种方式进行设置。</font>

<font style="color:#333333;">点击【新增】---选择【零售商品】</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244412843-454c380b-5720-413f-a910-aff3a28ae3ac.jpeg)

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244413195-5824aa33-c852-4ce1-aab6-f865aa80fe78.jpeg)

<font style="color:#333333;">3.若商品数量多的话，也可以以批量导入的形式进行商品资料录入。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244413487-0e59a0b8-2045-4678-9013-5f0a0ec03194.jpeg)

<font style="color:#000000;">4.下载好模版之后，将商品资料按照模版的格式导进系统，如图：</font>

<font style="color:#E53333;">注意：导入不支持商品图片导入</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244413787-a476b7a6-d165-4c49-a47d-9c53ae44fe9d.jpeg)

<font style="color:#333333;">5.后续库存可通过入库单进行入库补充到门店仓库</font>

<font style="color:#333333;">路径：商品→仓储管理→入库单</font>

<font style="color:#333333;">点击【新增】添加入库单</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244414113-22480695-1542-412f-9781-77df6cbfcbfb.jpeg)

<font style="color:#333333;">按照下述信息填写入库单，点击保存完成入库</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244414531-826b139d-2490-4b53-93ed-8b127b96edee.jpeg)

## **<font style="color:#333333;">第六步：给员工开通售货机补货权限</font>**
<font style="color:#333333;">1.员工需要提前新增好账号（不要求管理员权限）</font>

<font style="color:#333333;">路径：后台→设置→员工管理→用户管理</font>

<font style="color:#333333;">点击新增，给员工添加新账号，已有系统登录账号可跳过此步骤</font>

<font style="color:#E53333;">注意：此位置需要将联系电话也要填上，而且此电话需要和员工微信的手机号一致</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244414928-70b594c7-e0bf-42de-a499-9f40e3e41169.jpeg)

<font style="color:#333333;">2. 开通游乐掌柜账号，并勾选授权【仓管】功能</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244415270-41586280-a6d1-4224-8b84-4a8889f7355c.jpeg)

<font style="color:#333333;">3. 登录游乐掌柜账号关联的手机微信，在程序搜索栏，搜索【游乐掌柜】，点击自助售货机功能，进行补货入仓；</font>

<font style="color:#333333;">微信搜索游乐掌柜：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244415604-c4ccb466-c0b9-43e5-9b78-0910ac6c23f4.jpeg)

<font style="color:#333333;">若该手机微信是已经关联后台且开通了游乐掌柜功能，则登录进去即可看到【售货机补货】功能，如下图所示</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244415943-176ea344-43f4-4364-adef-86b97fc11fe3.jpeg)

## **<font style="color:#333333;">第七步：上架货物/补货</font>**
<font style="color:#333333;">1. 打开售货机，将货道架用力往上提，提上之后稍微用力往下拖动，再依次在货道架上上架商品。</font>

<font style="color:#333333;">注：若需要调整货道空间（有时候饮料占地空间过大），可拽紧货道弹簧一端，稍微用力往后拖动，顺时针方向旋转，以此调整货道间隔。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244416160-56eea05e-df34-4b79-8770-660152081a27.jpeg)

<font style="color:#333333;">2.货物放置后，在系统上进行补货数量填写，打开游乐掌柜，选择【售货机补货】</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244416393-4318621b-5184-4746-b1e4-0e6359bdd5c6.jpeg)

<font style="color:#333333;">3.选择相应货道，进行上货：</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244416625-eb8b9cd7-8660-449d-83f7-f9eb314839d0.jpeg)

<font style="color:#333333;">4.后台设置好零售商品，在弹窗口搜索该商品，进行货品上架</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244416919-50e24fa8-bac8-4688-8cb9-aa70ae95aed2.jpeg)

<font style="color:#333333;">5.上架完毕后将售货机门关闭即可。</font>

## **<font style="color:#333333;">第八步：更换货物</font>**
<font style="color:#333333;">在游乐掌柜中，选择对应的货道，并点击【更换商品/货回主仓】可以进行商品变更</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244417257-4cb1a9a3-ecf5-475c-95f6-d2f23a491c34.jpeg)

## **<font style="color:#333333;">第九步：补货</font>**
<font style="color:#333333;">在游乐掌柜上选择对应的货道，输入需要补货的数量，点击加货即可完成</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244417493-f5049593-f1a2-47d3-9526-9a066ef7de87.jpeg)

# **<font style="color:#333333;">七、测试流程</font>**
<font style="color:#333333;">1.打开微信，扫一下设备付款码，购买饮料；检查货物是否从出货正确。</font>

![](https://cdn.nlark.com/yuque/0/2024/jpeg/1584417/1732244417756-6093ec46-59e2-4c33-8bd6-e2d8d5a2a65a.jpeg)

<font style="color:#333333;">2.检查所有商品的定价和兑换价是否正确。</font>

# **<font style="color:#333333;">七、常见问题</font>**
**<font style="color:#333333;">1.自助售货机兑换后不出货</font>**

<font style="color:#333333;">答：一般因为售货机没有联网或者联网失败导致，检查盒子连接情况，如果连接成功，盒子应该是【电源】【联网】【强度】【待机】等都亮绿色灯，且不会灭；网络强度弱则【强度】为黄色灯；</font>

**<font style="color:#333333;">2.顾客扫码后，提示设备离线，如何处理？</font>**

<font style="color:#333333;">解决：</font>

<font style="color:#333333;">如果是WiFi版售货机，检查当地网络是否稳定，WIFI是否覆盖到位；</font>

<font style="color:#333333;">以上检查了无误后，再检查下售货机设备里边的盒子状态，看下盒子是否正常。</font>

**<font style="color:#333333;">3.顾客扫码支付后，货道不出货或者出错货品。</font>**

<font style="color:#333333;">解决：</font>

<font style="color:#333333;">检查游乐掌柜后台货道上架是否设置错误，库存是否不足。</font>

**<font style="color:#333333;">4.售货机的库存能否直接通过入库单进行补货？</font>**

<font style="color:#333333;">答：不可以，只能通过游乐掌柜补货。</font>

**<font style="color:#333333;">5.使用测试货道时，商品掉落下来后，会减少系统库存吗？</font>**

<font style="color:#333333;">答：不会，所以需要将商品放回去。</font>
