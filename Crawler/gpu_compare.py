#%%
import pandas as pd
import re
gpu_list = pd.read_csv('./DATA/gpu_list.csv')
for i in range(0,len(gpu_list)):
    if gpu_list.iloc[i,2]=='GT 210':
        gpu_list.iloc[i,10]='502'
        gpu_list.iloc[i,11]='1.25'
    if gpu_list.iloc[i,2]=='GT 710':
        gpu_list.iloc[i,10]='347'
        gpu_list.iloc[i,11]='4.55'
    if gpu_list.iloc[i,2]=='GT 730':
        gpu_list.iloc[i,10]='298'
        gpu_list.iloc[i,11]='6.21'
    if gpu_list.iloc[i,2]=='GT 1030':
        gpu_list.iloc[i,10]='140'
        gpu_list.iloc[i,11]='18.3'
    if gpu_list.iloc[i,2]=='GTX 1050':
        gpu_list.iloc[i,10]='82'
        gpu_list.iloc[i,11]='33.9'
    if gpu_list.iloc[i,2]=='GTX 1050 Ti':
        gpu_list.iloc[i,10]='72'
        gpu_list.iloc[i,11]='38.3'
    if gpu_list.iloc[i,2]=='GTX 1060':
        gpu_list.iloc[i,10]='34'
        gpu_list.iloc[i,11]='70.9'
    if gpu_list.iloc[i,2]=='GTX 1070':
        gpu_list.iloc[i,10]='19'
        gpu_list.iloc[i,11]='98'
    if gpu_list.iloc[i,2]=='GTX 1070 Ti':
        gpu_list.iloc[i,10]='14'
        gpu_list.iloc[i,11]='116'
    if gpu_list.iloc[i,2]=='GTX 1080':
        gpu_list.iloc[i,10]='11'
        gpu_list.iloc[i,11]='124'
    if gpu_list.iloc[i,2]=='GTX 1080 Ti':
        gpu_list.iloc[i,10]='6'
        gpu_list.iloc[i,11]='150'
    if gpu_list.iloc[i,2]=='RTX 2070':
        gpu_list.iloc[i,10]='9'
        gpu_list.iloc[i,11]='134'
    if gpu_list.iloc[i,2]=='RTX 2080':
        gpu_list.iloc[i,10]='7'
        gpu_list.iloc[i,11]='149'
    if gpu_list.iloc[i,2]=='RTX 2080 Ti':
        gpu_list.iloc[i,10]='2'
        gpu_list.iloc[i,11]='193'
    if gpu_list.iloc[i,2]=='RX 550':
        gpu_list.iloc[i,10]='125'
        gpu_list.iloc[i,11]='20.9'
    if gpu_list.iloc[i,2]=='RX 560':
        gpu_list.iloc[i,10]='86'
        gpu_list.iloc[i,11]='31'
    if gpu_list.iloc[i,2]=='RX 570':
        gpu_list.iloc[i,10]='47'
        gpu_list.iloc[i,11]='61.2'
    if gpu_list.iloc[i,2]=='RX 580':
        gpu_list.iloc[i,10]='36'
        gpu_list.iloc[i,11]='70'
    if gpu_list.iloc[i,2]=='RX 580 XTR':
        gpu_list.iloc[i,10]='36'
        gpu_list.iloc[i,11]='70'
    if gpu_list.iloc[i,2]=='RX 590':
        gpu_list.iloc[i,10]='28'
        gpu_list.iloc[i,11]='79'
    
gpu_list.to_csv('./DATA/gpu_list.csv', encoding='utf_8_sig')

#%%
print(gpu_list)

#%%
