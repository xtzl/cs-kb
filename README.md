# 场地客服知识库（本地版）

一个跑在你自己电脑上的知识库搜索器：语雀 / 飞书 / 公司自建网站的资料导进来，统一归类，
一个搜索框就能查到，离线可用，数据不出本机。

---

## 一、30 秒上手

双击 **`start.bat`**，浏览器会自动打开 `http://127.0.0.1:8765`。

或者手动：

```bash
cd kb
python tools/build_index.py     # 生成索引
python tools/serve.py           # 启动界面（只监听本机）
```

> 只有 Python 3，**不需要 pip 安装任何东西**。

---

## 二、界面怎么用

| 操作 | 说明 |
| --- | --- |
| `/` | 光标跳到搜索框 |
| 输入问题 | 边打边搜，标题命中优先，正文命中也会出结果 |
| `↑` `↓` | 上下切换结果，右边立刻显示正文 |
| `Enter` | 打开第一条 |
| `Esc` | 清空 / 关闭正文 |
| 左侧分类 | 按业务板块过滤，点第二次取消 |
| 左侧来源 | 按语雀 / 飞书 / 官网过滤 |
| ★ 收藏 | 常用条目收藏后，搜索时排序会更靠前 |
| 复制正文 | 一键复制，方便粘到聊天窗口回复客户 |

搜索做了**三层兜底**，越往后越宽松：

1. **同义词扩展**——客户说"退币"，文档写"退彩票"也能搜到
2. **口语改写**——客户说"钱少了""权限不够""吞币"，自动换成文档里的"余额""权限""卡币"
3. **长句分词**——整句搜不到时，用词表把"兑换礼品"切成"兑换 + 礼品"再搜

词表都在 `config/synonyms.json`：`groups` 是同义词组，`phrases` 是口语→书面词改写。
**客服反馈"搜不到"的时候，八成是这两个表缺词，加一行就解决。** 改完跑 `python tools/build_index.py`。

---

## 三、把资料灌进来

### 1. 语雀（公开库不需要 token，推荐）

**公开知识库**直接抓，不需要任何凭据（增量，可反复跑）：

```bash
python tools/scrape_yuque_public.py https://ychylb.yuque.com/staff-gcg8pk/ylgj   # 娱乐管家
python tools/scrape_yuque_public.py https://ychylb.yuque.com/staff-gcg8pk/hg1x92 # 油菜花硬件
```

**私有知识库**才需要 token：

```bash
set YUQUE_TOKEN=你的token
python tools/import_yuque.py --list          # 先看有哪些知识库
python tools/import_yuque.py                 # 全量导入
python tools/import_yuque.py --book 客服手册  # 只导一个
```

> 语雀不给开 API 时，网页上「导出为 Markdown」打包下载，然后：
> `python tools/import_local.py "下载的文件夹" --source 语雀`

### 2. 飞书 / Lark

在 open.feishu.cn 建自建应用，开通 `wiki:wiki:readonly`、`docx:document:readonly`，
发布后把应用「添加为知识库成员（可阅读）」，拿到 App ID / Secret。

```bash
set FEISHU_APP_ID=cli_xxx
set FEISHU_APP_SECRET=xxx
python tools/import_feishu.py --list
python tools/import_feishu.py
```

> 飞书也能在网页端「下载为 Word」，再用 `import_local.py` 导入 docx，效果一样。

### 3. 公司 KMS 知识库（泛微系）

```bash
python tools/scrape_kms.py https://kms.gzych.vip                 # 全量，约 900 篇
python tools/scrape_kms.py https://kms.gzych.vip --limit 20      # 先试跑
python tools/scrape_kms.py https://kms.gzych.vip --max-pages 140 # 加深列表翻页
```

自动翻 `webtype/view/Pub{n}.html` 列表页、解析 `webdoc/view/Pub*.html` 正文，
表格会转成 Markdown 管道表，图片转绝对地址。增量执行，已导入的 URL 会跳过。

### 4. 其它网站 / 手工文档

```bash
python tools/crawl_site.py "http://kb.公司域名.com/" --cookie "SESSION=xxxx" --max-pages 300
```

- Cookie：浏览器 F12 → Network → 任意请求 → 复制 Cookie 整行
- 只爬同域名；`--include "/faq/"` 可限定目录
- 自动去掉导航、页脚这类每页都有的模板文字
- 默认每页间隔 0.8 秒，别给公司服务器压力

### 5. 手工写的文档

复制 `文档模板.md` 到 `docs/` 下，改个名，填内容。
格式就是普通的 Markdown，开头那段 `---` 之间是属性：

```markdown
---
title: 打印机不出小票
category: 设备与机台     # 必须是 config/categories.json 里的分类
tags: 小票机, 打印异常
aliases: 打不出票, 小票机坏了   # 客户可能的说法，能提高命中率
source: 手工
updated: 2026-11-12
---
```

**每次新增或修改文档后，执行一次 `python tools/build_index.py`**（或重开 start.bat）。

---

## 四、归类是怎么做的

导入时按关键词自动判断，规则在 `config/classify_rules.json`：

```json
"设备与机台": ["卡头", "机台", "兑币机", "取卡机", "闸机", "打印机", ...]
```

标题命中算 3 分、正文命中算 1 分，取最高分的分类；都不过关就归「其他」。
分类不准的时候，直接改文档开头的 `category:`，或者往规则里加词——
改完规则跑一次 `python tools/reclassify.py` 就能全库重算（会同时移动文件），不用重新导入。

分类清单本身在 `config/categories.json`，可以改成你们内部叫法
（比如「机台维护」「会员运营」）。

---

## 五、目录结构

```
kb/
├─ start.bat            一键启动
├─ index.html           搜索界面（单文件，不依赖网络）
├─ 文档模板.md
├─ docs/                所有知识文档（markdown，可以按分类分子目录）
├─ data/                生成的索引 index.json / index.js
├─ config/
│  ├─ categories.json   分类清单
│  ├─ classify_rules.json  自动归类关键词
│  └─ synonyms.json     同义词表
└─ tools/
   ├─ build_index.py    建索引
   ├─ serve.py          本地服务
   ├─ scrape_yuque_public.py  抓取公开语雀知识库（无需 token，增量）
   ├─ import_yuque.py   语雀导入（需 token，可读私有库）
   ├─ import_feishu.py  飞书导入
   ├─ crawl_site.py     官网爬取
   ├─ import_local.py   本地文件/导出包导入
   ├─ reclassify.py     改完规则后全库重新归类
   └─ kb_lib.py         公共函数
```

---

## 六、常见问题

**改了文档但界面没变？**
重新执行 `python tools/build_index.py`，然后 Ctrl+F5 刷新。

**端口 8765 被占用？**
`set KB_PORT=8899` 后再启动。

**能不能同事一起用？**
现在是纯本地。要共享可以：把 `kb` 目录放共享盘 / 网盘同步，各自打开；
或者告诉我，我改成局域网版（内网其他电脑访问你的机器）。

**数据安全吗？**
所有文件都在本地磁盘，服务只监听 `127.0.0.1`，外网访问不到。
唯一的外发行为是你主动运行导入脚本时会请求语雀/飞书/公司站点。

**文档多了会不会卡？**
纯前端检索，几千篇（几十 MB 文本）以内都是毫秒级。真到上万篇再换 SQLite 全文索引。
