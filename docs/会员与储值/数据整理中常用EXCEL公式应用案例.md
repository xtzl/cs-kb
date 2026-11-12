---
title: 数据整理中常用EXCEL公式应用案例
category: 会员与储值
tags: 
source: KMS
updated: 2025-02-17
url: https://kms.gzych.vip/webdoc/view/Pub2c93a81490676e70019511abfe311fcc.html
section: 现场实施知识库
toc_path: 现场实施知识库
author: 梁建宁
kms_id: 00001956
---

# 文档说明

本文档用于提供一些方案给予大家在处理客户会员数据时如何来处理数据

## 案例一：原来数据上有不合规的手机号时，如何筛查出不合规的手机号？

原理：EXCEL公式中，可以通过 LEN 公式来筛查出单元格中的数字位数，所以可以通过配合IF公式来判断

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511a986d31fc3&type=max)

公式为： =if（LEN（单元格）=11,1,2）

公式说明：if为判断公式，LEN（需要判断的单元格），如果判断的单元格的位数为11，则输出1，否则输出2

通过此公式判断后，则通过筛选就2的数据，则可以找到那些数据时不符合条件的。

## 案例二：重复会员筛查，原来旧系统有可能存在会员同时有期限卡和储值，但是表格是通过多个表格呈现，如何将此类会员添加到一个表格中

原理：先将会员逐一复制到新表格，然后通过标记数据来源后，进行删除重复项，最后筛选后得出只有期限卡和次卡的会员卡号有哪些

第一步：先将会员余额的会员卡号都复制到A列，并将这部分数据标记为1

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511c0b7ba200e&type=max)

第二步，重复第一步，将其他表格的会员数据都复制过来，并且标记为 2~4

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511c332fd2013&type=max)

第三步，选择A列，选择删除重复项

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511c4eb1d2014&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511c535d22016&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511c593b62017&type=max)

第四步，筛选B列，并筛选2~4的数据即可

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511c6c6f2201a&type=max)

以上这部分则为只有套票没有储值的会员卡号

## 案例三：出现总次数和剩余次数都在同一个单元格，如何分开？

原数据如图所示：

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511ca7a1d2039&type=max)

方案原理：利用EXCEL的分裂功能进行分裂

第一步：在次数右侧，先新增空白列（非常重要，直接分列会覆盖后面的数据，所以需要新增空白行）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511cbe3a32044&type=max)

第二步，选择需要分列的数据列，并选择【分列】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511cd57ec204a&type=max)

第二步，选择分隔符号，并选择下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511ce11f6204c&type=max)

第三步，选择其他，并输入/作为分列标识，然后预览结果看看是不是想要的结果，然后点击下一步

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511cfdf8f204f&type=max)

第四步，选择常规，点击完成即可

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511d0613b2050&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511d08ad02052&type=max)

处理后，总次数和剩余次数就分开了

## 案例四：如何将按照会员卡号/手机号找到对应的数据

例子：将套票会员号/手机号复制到储值报表时，如何找到此会员对应的有效期

原理：通过VLOOKUP按照手机号/会员号，找到原报表的数据

公式说明：vlookup（目标值，查找范围，引用第几列的数据，是否精确查找）

第一步，此处先处理年卡，所以先找到年卡的数据

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511e163e32087&type=max)

第二步，选择第一个处理的会员对应的单元格，输入=vlookup函数

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511e2d0cb208b&type=max)

第三步，选择目标值、查找列，并输入查找的数据在查找列的第几列，以此案例为准，查找列就在从F到J数过去第5列，最后选择匹配条件，我们直接输入0即可。

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511e40f06208f&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511e5ea312092&type=max)

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511e80fe52099&type=max)

最后下拉数据即可同步出来

## 案例五，如何合并统计次卡次数

说明：由于次卡可以多种套票充值到同一个会员卡中，如果只是想计算会员次数，可以通过sumif公式进行按条件合计

公式说明：sumif(查找目标值范围，目标是哪个，合计列是哪列）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511fe720020e4&type=max)

公式编写说明，同样在空白列，输入=sumif(在哪里找到会员号，目标会员号是哪个，合计列是哪列）

## 案例六：匹配会员等级（按储值数量算）

案例说明：如何根据不同的储值数量来匹配会员等级

解决思路，通过IF公式进行比较，如下图所示，不同的储值数量，区分等级，则可以进行多次比较得出最后会员等级

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511f0e10a20c6&type=max)

公式说明：if(条件判断，符合条件输出什么，不符合条件输出什么）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019511f4795620cd&type=max)

公式使用说明：

在后面新增一列，用于存放等级，选择该列第一个个单元格，输入公式，=if(比对的单元格对应的条件，符合条件输出内容，不符合条件进入下一个if，如此类推，最后输出最后值）

## 案例七：覆合型会员，如何判断最终会员等级

解决思路：

1.先分别输出储值时会员等级、套票对应的会员等级

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700195121e2b152157&type=max)

2.通过IF函数进行比对，if函数是按照层次一步步比对的，所以可以按照客户需求来比对，下面按照下述案例来说明

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e700195121f2ebc215b&type=max)

分析到客户需求是，只要有年票，就是V3等级，也就是第一层匹对就是年票，按照上图所输出，年票的等级代号为“3”，没有就是0，也就是大于0的就是v3等级，所以IF第一层就是 if(年卡等级>0,就输出V3等级，不符和条件继续进行比对）

第二层比对时，按照不同等级门店，比对顺序有所变动，所以第二层就根据门店等级来选择是比对储值等级还是比对次卡等级，加入是二三级门店，就继续if(储值等级>0,输出储值等级，否则就输出次卡等级）

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e70019512249bf62163&type=max)

## 案例八：如何给会员号加前缀

说明，利用公式符号 &来实现

注意事项，加入的非公式内容，需要用冒号来引用，如加前缀zq，则需要用引号来写公式

公式说明="zq"&单元格

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c93a81490676e7001951228ccc52185&type=max)

## 案例九：拆分表格

说明：当门店会员数据非常大时，由于系统只支持5W条数据导入一次，这时候就需要拆分表格来分批导入

#### 方案一：使用第三方工具进行分割

分割工具下载链接：

https://nos-pulic.oss-cn-shenzhen.aliyuncs.com/%E5%AE%9E%E6%96%BD%E7%BB%84%E5%AE%89%E8%A3%85%E5%B7%A5%E5%85%B7/5.%E5%B8%B8%E7%94%A8%E8%BD%AF%E4%BB%B6%E5%B7%A5%E5%85%B7/EXCEL%E5%88%86%E5%89%B2%E5%99%A8.exe

#### 方案二：使用windows office 内置工具进行分割

注意事项：此方法只适用与windows office 2016官方软件才可以，WPS不支持此方法

操作过程：

1.打开文EXCEL表，按ALT+F11调出宏命令，则出现以下界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19ad88ff3019b0c03f572550a&type=max)

2.选择【插入】→【模块】

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19ad88ff3019b0c048a35550b&type=max)

3.将以下命令全量复制到里面

Option Explicit
Sub SplitSheet50000()
Dim wsSrc As Worksheet, ws As Worksheet
Dim lastRow As Long, lastCol As Long
Dim rowsPerPage As Long, totalPages As Long
Dim i As Long, startRow As Long, endRow As Long
Dim sheetName As String, baseName As String

Set wsSrc = ActiveSheet
baseName = wsSrc.Name
rowsPerPage = 50000
Application.ScreenUpdating = False
Application.DisplayAlerts = False

lastRow = wsSrc.Cells(wsSrc.Rows.Count, 1).End(xlUp).Row
If lastRow <= 1 Then GoTo ExitProc
lastCol = wsSrc.Cells(1, wsSrc.Columns.Count).End(xlToLeft).Column

totalPages = IIf((lastRow - 1) Mod rowsPerPage = 0, _
(lastRow - 1) \ rowsPerPage, _
(lastRow - 1) \ rowsPerPage + 1)

For i = 1 To totalPages
startRow = (i - 1) * rowsPerPage + 2
endRow = IIf(i = totalPages, lastRow, i * rowsPerPage + 1)

Set ws = ThisWorkbook.Worksheets.Add(After:=ThisWorkbook.Sheets(ThisWorkbook.Sheets.Count))
On Error Resume Next
sheetName = baseName & "_" & Format(i, "000")
ws.Name = sheetName
If Err.Number <> 0 Then
sheetName = baseName & "_" & Format(i, "000") & "_" & Format(Now, "hhmmss")
ws.Name = sheetName
Err.Clear
End If
On Error GoTo 0

' 复制表头
wsSrc.Rows(1).Copy Destination:=ws.Rows(1)
' 复制数据块
If startRow <= endRow Then
wsSrc.Range(wsSrc.Cells(startRow, 1), wsSrc.Cells(endRow, lastCol)).Copy _
Destination:=ws.Cells(2, 1)
End If
Next i

ExitProc:
Application.DisplayAlerts = True
Application.ScreenUpdating = True
MsgBox "拆分完成，共生成 " & totalPages & " 个工作表。", vbInformation
End Sub

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19ad88ff3019b0c06c99d5513&type=max)

4.依次关闭此界面

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19ad88ff3019b0c0782475516&type=max)

5.切换到需要分表的表，按ALT+F8 运行脚本

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19ad88ff3019b0c096514551e&type=max)

6.等待执行完成即可

![](https://kms.gzych.vip/webdoc/view/actionImg/Publoadimg.do?id=2c9084a19ad88ff3019b0c09df555521&type=max)

<
