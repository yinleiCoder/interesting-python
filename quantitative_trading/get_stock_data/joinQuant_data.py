"""
我是个人投资者，所以暂时采取免费接口JoinQuant.

JoinQuant: https://joinquant.com/
申请账户后，安装JQData: pip install jqdatasdk
          升级JQData(每2周发布一次迭代版本，增加更多维度的基础数据以及因子类数据)pip install -U jqdatasdk

JQData证券代码格式：
    上海证券交易所	.XSHG	600519.XSHG	贵州茅台
    深圳证券交易所	.XSHE	000001.XSHE	平安银行
    中金所	.CCFX	IC9999.CCFX	中证500主力合约
    大商所	.XDCE	A9999.XDCE	豆一主力合约
    上期所	.XSGE	AU9999.XSGE	黄金主力合约
    郑商所	.XZCE	CY8888.XZCE	棉纱期货指数
    上海国际能源期货交易所	.XINE	SC9999.XINE	原油主力合约
    场外基金	.OF	398051.OF	中海环保新能源混合

Resample函数转化时间序列：
    Pandas的方法函数。可以转换时间序列的频次、统计汇总。
    如日K转周K，计算开盘价、收盘价、最高价、最低价。
    统计汇总功能：resample.sum/.count
    如统计一只股票的周成交量。

使用JQData查询财务指标：
    以一家企业为例，财务报表=资产负债表(【财务状况】资产、负债、所有者利益)+利润表(【经营成果】收入、成本费用、利润)+现金流量表(【现金流量】现金流入、现金流出)
    资产负债表：体现企业家底和负债情况
    利润表：体现公司盈利能力、赚了多少、怎么赚的，隐含着对未来利润增长的预期。体现市场空间、成长能力。
    现金流量表：权责发生制 VS 收付实现制。体现造血能力、竞争优势、议价能力。
"""

from jqdatasdk import *
import pandas as pd


account = '13795950539'
password = 'Yl13795950539@'
auth(account, password)

# 设置pandas行列不忽略
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 1000)

# 查询当日剩余可调用数据条数 {'total': 1000000,'spare': 996927}
avaiable_query_count = get_query_count()
print(f"今日剩余可调用数据条数：{avaiable_query_count}")

# 获取中国联通股票行情数据
# df = get_price('600050.XSHG', end_date='2022-01-19', count=10, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume', 'money'])
# print(df)

# 获取所有A股的行情数据
# stocks = list(get_all_securities(['stock']).index)
# print(stocks)
# df = get_price(['600050.XSHG', '601728.XSHG'], end_date='2022-01-19', count=10, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume', 'money'])
# print(df)

# resample函数
# 1. 日K转为周K
# df = get_price('600050.XSHG', end_date='2022-01-19', count=20, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume', 'money'])
# df['weekday'] = df.index.weekday
# print(df)
# df_week = pd.DataFrame()
# df_week['open'] = df['open'].resample('W').first()# 开盘价
# df_week['close'] = df['close'].resample('W').last()# 收盘价
# df_week['high'] = df['high'].resample('W').max()# 最高价
# df_week['low'] = df['low'].resample('W').min()# 最低价
# 2. 汇总统计：统计一下月成交量、成交额
# df_week['volume(sum)'] = df['volume'].resample('W').sum()
# df_week['money(sum)'] = df['money'].resample('W').sum()
# print(df_week)

# 获取财务指标:https://www.joinquant.com/help/api/help#Stock:%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE%E5%88%97%E8%A1%A8
df = get_fundamentals(query(indicator), statDate="2020")
# print(df[:4])
# df.to_csv(r'E:\PycharmProjects\funnyPython\quantitative_trading\finance_data\china_unicom_finance2020.csv')
# 基于盈利指标利用成长增速进行选股：eps、operating_profit、roe、inc_net_profit_year_on_year
df = df[(df['eps'] > 0) & (df['operating_profit'] > 927732400.49) &
        (df['roe'] > 4.151809687) & (df['inc_net_profit_year_on_year'] > -168.7111016)]
print(df)