```
 _____   _____       ___   _   _____  __    __ 
| ____| |  _  \     /   | | | |  _  \ \ \  / / 
| |__   | |_| |    / /| | | | | |_| |  \ \/ /  
|  __|  |  _  {   / / | | | | |  ___/   \  /   
| |___  | |_| |  / /  | | | | | |       / /    
|_____| |_____/ /_/   |_| |_| |_|      /_/    

``` 
[![PyPI](https://img.shields.io/pypi/v/ebaipy.svg)](https://pypi.org/project/ebaipy)


饿百零售（饿百外卖） 第三方 Python SDK


Author: Bruce He <bruce@shbewell.com>


[[饿百零售官方API文档]](https://open-be.ele.me/dev/api/doc/v3/)

# 功能特性

已接入饿百零售所有下行接口，包括：
1. 商户相关的接口
2. 商品相关的接口
3. 营销相关的接口
4. 订单相关的接口
5. 基础数据接口

# 安装

推荐使用 pip 进行安装:

```bash
pip install ebaipy
```

升级版本:

```bash
pip install -U ebaipy
```

# 使用示例

```python

from ebaipy import EbaiClient

# 初始化客户端类
source = 111111
secret = 'my_secret'
client = EbaiClient(source, secret)

# 获取sku列表
client.sku.list(shop_id=10001)

# 获取订单列表
client.order.list(shop_id=10001)

```

# 问题反馈

我们主要使用 [GitHub issues](https://github.com/brucehe3/ebaipy/issues) 进行问题追踪和反馈。

E-Mail: <bruce@shbewell.com>

