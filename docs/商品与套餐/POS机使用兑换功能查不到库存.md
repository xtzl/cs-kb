---
title: POS机使用兑换功能查不到库存
category: 商品与套餐
tags: 
source: KMS
updated: 2026-07-02
url: https://kms.gzych.vip/webdoc/view/Pub2c9084a19cff446a019f221bbe60528d.html
section: 日常问题处理案例归档
toc_path: 现场实施知识库 / 日常问题处理案例归档
author: 梁建宁
kms_id: 00003106
---

# 现象

盘点机兑换商品找不到所有商品。前台OK。绑定仓库和前台一个仓库。有库存。有写彩票兑换数量。没限制终端。客户导入的商品。

# 原因

系统BUG

# 解决方法

数据库执行以下语句

-----兑换视图兼容游乐宝转娱乐管家数据
IF EXISTS (SELECT 1 FROM sys.views WHERE object_id=OBJECT_ID('[dbo].[View_ExchangeGoodInfo]'))
BEGIN
DROP VIEW [dbo].View_ExchangeGoodInfo;
END

go

create view View_ExchangeGoodInfo
as
SELECT gb.ID, gb.GoodName, gb.GoodNO, gb.GoodsType, gb.IsReal,
(SELECT Barcode + ','
FROM dbo.Mall_GoodsBarcode
WHERE (Goods = gb.ID) AND (OwnedBusiness = gb.OwnedBusiness OR
OwnedBusiness IS NULL) AND (IsDelete = 0) FOR XML PATH('')) AS GoodsBarcode, exGd.PriceLottery AS TicketExChangeAmount,
exGd.PriceHeapcent AS HeacentExChangeAmount, exGd.PriceCoin AS CoinExChangeAmount, exGd.PriceGoldCoin AS GoldExChangeAmount,
exGd.PriceDoll AS DollExChangeAmount, exGd.PriceEnergy AS EnergyExChangeAmount, exGd.RecoverPriceLottery AS TicketRecoverAmount,
exGd.RecoverPriceHeapcent AS HeacentRecoverAmount, exGd.RecoverPriceCoin AS CoinRecoverAmount,
exGd.RecoverPriceGoldCoin AS GoldRecoverAmount, exGd.RecoverPriceDoll AS DollRecoverAmount,
exGd.RecoverPriceEnergy AS EnergyRecoverAmount, exGd.IsCanRecover, gb.IsDelete, gb.IsEnable, gb.CreateTime, gb.UpdateTime, exGd.OwnedMall,
exGd.OwnedBusiness, gb.IsNoExchangeRate, gb.MemCode
FROM Mall_ExchangeGoodsPrice AS exGd
JOIN Mall_GoodBase AS gb ON exGd.Goods = gb.ID
LEFT JOIN Mall_GoodExtent as ge on gb.ID=ge.Good
WHERE exGd.IsDelete = 0 AND gb.IsDelete = 0 AND (gb.GoodsType IN (0, 1, 2, 6, 101, 102)) AND gb.IsSys = 0 and (ge.ID is null or ge.GoodsAtt!=4)

<
