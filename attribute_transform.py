# -*- coding: utf-8 -*-
# 时间    : 2018/10/14 22:36
# 作者    : xcl

#属性变换
import pandas as pd

#参数初始化
discfile = 'C:\\Users\\Administrator\\Desktop\\DiskCapacityPrediction\\data\\discdata.xls' #磁盘原始数据
transformeddata = 'C:\\Users\\Administrator\\Desktop\\discdata_processed.xls' #变换后的数据

data = pd.read_excel(discfile)
data = data[data['TARGET_ID'] == 184].copy() #只保留TARGET_ID为184的数据

data_group = data.groupby('COLLECTTIME') #以时间分组

def attr_trans(x): #定义属性变换函数
  result = pd.Series(index = ['SYS_NAME', 'CWXT_DB:184:C:\\', 'CWXT_DB:184:D:\\',	'COLLECTTIME'])
  result['SYS_NAME'] = x['SYS_NAME'].iloc[0]
  result['COLLECTTIME'] = x['COLLECTTIME'].iloc[0]
  result['CWXT_DB:184:C:\\'] = x['VALUE'].iloc[0]
  result['CWXT_DB:184:D:\\'] = x['VALUE'].iloc[1]
  return result

data_processed = data_group.apply(attr_trans) #逐组处理
data_processed.to_excel(transformeddata, index = False)