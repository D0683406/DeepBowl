#%%
import pandas as pd
import re
UserBenchmarks = pd.read_csv('./DATA/CPU_UserBenchmarks.csv')
cpu_list = pd.read_csv('./DATA/cpu_list.csv')

#%%
templist=[]
for i in range(0, len(UserBenchmarks)):
    temp=re.sub("Core ","",UserBenchmarks.iloc[i]["Model"])
    temp=re.sub("Pentium Gold G5400","Pentium G5400",temp)
    temp=re.sub("Pentium Gold G5500","Pentium G5500",temp)
    temp=re.sub("Pentium Gold G5600","Pentium G5600",temp)
    temp=re.sub("v5","V5",temp)
    temp=re.sub("v4","V4",temp)
    temp=re.sub("Pentium G3430","Celeron G4920",temp)
    temp=re.sub(" APU (2016 D.BR)","",temp)
    temp=re.sub(" APU (2016 D.BR)","",temp)
    temp=re.sub("Xeon E5-1650 v3","Xeon E5-2630 V4",temp)
    temp=re.sub("Xeon E3-1230 V2","Xeon E5-2620 V4",temp)
    temp=re.sub(" APU (2016 D.BR)","",temp)
    temp=re.sub("TR 2920X","TR2 2920X",temp)
    temp=re.sub("TR 2950X","TR2 2950X",temp)
    temp=re.sub("TR 2970WX","TR2 2970WX",temp)
    temp=re.sub("TR 2990WX","TR2 2990WX",temp)
    temp=re.sub("Ryzen 7","R7",temp)
    temp=re.sub("Ryzen 5","R5",temp)
    temp=re.sub("Ryzen 3","R3",temp)

    templist.append(temp)
for i in range(0, len(templist)):
    for u in range(0, len(cpu_list)):
        if templist[i]==cpu_list.iloc[u]["model"]:
            print("Model:"+UserBenchmarks.iloc[i]["Model"]+"  Rank:"+str(UserBenchmarks.iloc[i]["Rank"])+"    Benchmark:"+str(UserBenchmarks.iloc[i]["Benchmark"]))
            cpu_list.iloc[u,7]=UserBenchmarks.iloc[i]["Rank"]
            cpu_list.iloc[u,6]=UserBenchmarks.iloc[i]["Benchmark"]

cpu_list.iloc[48,7]=644
cpu_list.iloc[48,6]=31.9
cpu_list.iloc[49,7]=411
cpu_list.iloc[49,6]=45.1
cpu_list.to_csv("./DATA/cpu_list.csv", encoding="utf_8_sig")         
            






#%%
#cpu_list.to_csv("./DATA/cpu_list2.csv", encoding="utf_8_sig")
print(cpu_list.iloc[52,7])

#%%
