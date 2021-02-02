#%%
#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %%
xlsx = pd.ExcelFile('EPL_Possession.xlsx')
# %%
df_1415 = pd.read_excel(xlsx, '14-15')
df_1516 = pd.read_excel(xlsx, '15-16')
df_1617 = pd.read_excel(xlsx, '16-17')
df_1718 = pd.read_excel(xlsx, '17-18')
df_1819 = pd.read_excel(xlsx, '18-19')
df_1920 = pd.read_excel(xlsx, '19-20')
# %%
# 2014-2015
%matplotlib inline

x = df_1415.Poss
y = df_1415.Rk

plt.scatter(x,y)
plt.axis([35, 65, 20, 1])
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.xlabel("Average Possesion (%)")
plt.ylabel("Finishing Position")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='yellow')
#ax = plt.gca()
#ax.set_ylim(ax.get_ylim()[::-1])
print(np.corrcoef(x, y))

# %%
# 2015-2016
%matplotlib inline

x = df_1516.Poss
y = df_1516.Rk

plt.scatter(x,y)
plt.axis([35, 65, 20, 1])
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.xlabel("Average Possesion (%)")
plt.ylabel("Finishing Position")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='yellow')
#ax = plt.gca()
#ax.set_ylim(ax.get_ylim()[::-1])
print(np.corrcoef(x, y))

# %%
# 2016-2017
%matplotlib inline

x = df_1617.Poss
y = df_1617.Rk

plt.scatter(x,y)
plt.axis([35, 65, 20, 1])
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.xlabel("Average Possesion (%)")
plt.ylabel("Finishing Position")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='yellow')
#ax = plt.gca()
#ax.set_ylim(ax.get_ylim()[::-1])
print(np.corrcoef(x, y))

# %%
# 2017-2018
%matplotlib inline

x = df_1718.Poss
y = df_1718.Rk

plt.scatter(x,y)
plt.axis([35, 65, 20, 1])
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.xlabel("Average Possesion (%)")
plt.ylabel("Finishing Position")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='yellow')
#ax = plt.gca()
#ax.set_ylim(ax.get_ylim()[::-1])
print(np.corrcoef(x, y))

# %%
# 2018-2019
%matplotlib inline

x = df_1819.Poss
y = df_1819.Rk

plt.scatter(x,y)
plt.axis([35, 65, 20, 1])
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.xlabel("Average Possesion (%)")
plt.ylabel("Finishing Position")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='yellow')
#ax = plt.gca()
#ax.set_ylim(ax.get_ylim()[::-1])
print(np.corrcoef(x, y))

# %%
# 2019-2020
%matplotlib inline

x = df_1920.Poss
y = df_1920.Rk

plt.scatter(x,y)
plt.axis([35, 65, 20, 1])
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
plt.xlabel("Average Possesion (%)")
plt.ylabel("Finishing Position")
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='yellow')
#ax = plt.gca()
#ax.set_ylim(ax.get_ylim()[::-1])
print(np.corrcoef(x, y))
# %%
