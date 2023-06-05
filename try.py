import pandas as pd 
import time



pro_1 = { "start":[int(30 * 1e6),int(47 * 1e6),int(25 * 1e3)],
          "start_1":[int(47 * 1e6),int(68 * 1e6),int(12.5 * 1e3)]
        }


i = 0
for k,v in pro_1.items():
     
     df = pd.DataFrame()
    #  df['Frequency (Hz)'] = pd.Series(range(pro_1[k][0],pro_1[k][1]+ pro_1[k][2],pro_1[k][2]))
     df['Frequency (Hz)'] = pd.Series(range(v[0], v[1] + v[2], v[2]))
     df.to_csv(f"test{i}.csv",index=False)
  
     i = i+1

     




