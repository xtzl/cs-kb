---
title: AI分控-咸鱼倒卖币
category: 会员与储值
tags: 
source: 语雀·娱乐管家
updated: 2026-10-30
url: https://ychylb.yuque.com/staff-gcg8pk/ylgj/gesl1wkxg4gtv8o0
section: 🔥亮点功能说明文档
toc_path: 🔥亮点功能说明文档
---

**<font style="color:rgb(37, 51, 74);">一、功能场景</font>**

<font style="color:rgb(38, 36, 76);">为有效管控会员异常提币行为，系统新增</font>**<font style="color:rgb(38, 36, 76);">自动加入黑名单</font>**<font style="color:rgb(38, 36, 76);">机制及</font>**<font style="color:rgb(38, 36, 76);">白名单豁免</font>**<font style="color:rgb(38, 36, 76);">机制。当会员当日提币次数或提币总笔数超过预设规则时，系统将自动将其加入黑名单，限制其在兑币机上的提币操作；同时支持将特定玩家加入白名单，使其不受自动黑名单规则约束。</font>

****

**二、功能设置及版本要求**

业务系统：10.4.4314版本及以上

连锁设置：总部后台-总部-AI分控-咸鱼倒卖币

单店设置：设置-AI分控-咸鱼倒卖币

![](https://cdn.nlark.com/yuque/0/2026/png/1584417/1793334859856-8154081d-3539-418f-806e-3b6e9535a101.png)

****

**三、自动加入黑名单**

**2.1 触发条件**

| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">条件类型</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">说明</font> |
| :---: | --- |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">当日提币</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">次数</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">超限</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">会员当日提币次数超过系统设置的阈值</font> |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">当日提币</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">总笔数</font>**<font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">超限</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">会员当日提币总笔数超过系统设置的阈值</font> |


+ **<font style="color:rgb(38, 36, 76);background-color:rgba(0, 0, 0, 0);">满足以上任一条件</font>**<font style="color:rgb(38, 36, 76);background-color:rgba(0, 0, 0, 0);">，该会员将自动加入黑名单。</font>

**2.2 黑名单限制范围**

加入黑名单后，该会员**禁止**通过以下方式在兑币机提币：

| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">禁止方式</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">说明</font> |
| --- | --- |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">会员码</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">不可使用</font> |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">提币码</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">不可使用</font> |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">主扫登录码</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">不可使用</font> |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">手机号</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">不可使用</font> |


**2.3 黑名单下仍可用的提币方式**

| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">可用方式</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">说明</font> |
| --- | --- |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">收银台提币</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">支持前往收银台人工提币</font> |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">实体会员卡刷卡</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">支持使用实体会员卡在兑币机刷卡提币</font> |


****

**四、白名单机制**

**3.1 功能说明**

支持将部分玩家手动加入**白名单**。

**3.2 白名单特权**

| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">特权</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">说明</font> |
| --- | --- |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">不受自动黑名单规则约束</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">即使提币次数/笔数超过阈值，也不会被自动加入黑名单</font> |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">无限制提币</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">提币次数及提币数量均不受限制</font> |


---

****

**五、移除或转白/黑**

4.1、已在黑/白名单会员支持手动移除，或进行转入白名单或黑名单。

![](https://cdn.nlark.com/yuque/0/2026/png/1584417/1793334859818-1fcf7e7c-72b1-41f4-a809-1c49b506d916.png)

****

**六、与历史版本的区别**

| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">对比项</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">历史版本</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">当前版本</font> |
| --- | --- | --- |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">加入黑名单方式</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">仅支持手动填写卡号加入</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">新增自动触发机制 + 保留手动方式</font> |
| <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">白名单</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">不支持</font> | <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">新增白名单豁免机制</font> |


****

**注意事项**

1. <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">自动黑名单的触发阈值由后台规则配置决定，可根据实际运营需求调整。</font>
2. <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">白名单中的会员完全豁免自动黑名单规则，请谨慎添加。</font>
3. <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">黑名单会员仍可通过收银台或实体卡提币，并非完全封禁。</font>
4. <font style="color:rgb(0, 0, 0);background-color:rgba(0, 0, 0, 0);">本功能旨在防范倒卖币行为，建议结合日常运营数据合理设置阈值。</font>
