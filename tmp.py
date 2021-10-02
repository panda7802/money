import tushare as ts

ts.set_token('your token here')
# pro = ts.pro_api()
tu_token = 'fba0f69c02f5e4399b8dd63ae895ca69b7a55122a545c6f0f2c2bef3'
pro = ts.pro_api(tu_token)
#查询当前所有正常上市交易的股票列表
# data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# 东财
ts_code='601208.SH'
df = ts.pro_bar(ts_code=ts_code, asset='I',start_date='20210801',freq=60)
print(df.head(28))
