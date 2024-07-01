<div align="center">
   <img width="160" src="img/logo.png" alt="logo"></br>

<h1 width="95" align="center">Pakzat</h1></div>



----

### **介绍**

Kroyf telegram bot是一个在python平台下运行，提供Telegram协议支持的高效率机器人库

------

### **功能**

- #### 从MySQL数据库中（全部表）搜索指定关键词,TG上也可以称为"猎魔查询",然后返回给用户。

- #### 可以高度自定义的Button

------

### 未来的发展

- 桌面化
- 接入AI (目前已完成,不久后会上线)
- 集群化

------



### 使用的第三方库

```python
import asyncio
import aiomysql
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
```

------

## 变量和变量函数

```python
# TG BOT变量
TOKEN = "[Your TG BOT TOKEN]"
# MySQL变量
async def create_pool():
    # 创建连接池
    pool = await aiomysql.create_pool(
        host='[Your MySQL Server Host]',
        port=[Port],
        user='[User Name]',
        password='[Password]',
        db='[Database Name]',
        autocommit=True
    )
    return pool
```

------

## 支持

<img src="img\微信支付宝收款码二合一.png" style="zoom:50%;" />

------



## **声明**

> 此程序仅用来查询合法数据，开发此程序的目的是为了查询备忘数据和学习用途。因违法操作所带来的一切连带责任作者即本人概不负责。

------

### 最后

好用就给个⭐Star⭐
