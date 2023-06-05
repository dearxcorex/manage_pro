import pandas as pd 
from quantiphy import Quantity
from datetime import datetime



from tabulate import tabulate

class Pro:
    def __init__(self):
        self.df = pd.DataFrame() 
       

    def process(self,freq):
        if freq is not None:
            freq = [ i * 1e6 for i in freq]
            
            for v in freq:
                self.df.loc[self.df['Frequency (Hz)'] == v, 'Occupancy (%)'] =  50
                self.df.loc[~self.df['Frequency (Hz)'].isin((freq)), 'Occupancy (%)'] = int(0)
        else:
            self.df["Occupancy (%)"]  = 0
    


    def create_info(self,pro,date):
        #get info

        df_info = pd.read_csv("ref_data/pro_9.csv",usecols=["File Info"],encoding = "ISO-8859-1")

        #data
        df_info.loc[0,'File Info'] = f"File Name:pro_{pro}_1_000002_{date}_0101_OC"
        #records
        records = len(self.df['Frequency (Hz)'])
        df_info.loc[3,'File Info'] = f'Records:{records}'


        #date   
        days_to_add = str(date)
        datetime_obj = datetime.strptime(days_to_add,"%y%m%d")
        df_info.loc[4,'File Info'] = f"Created At:{datetime_obj.date()} 11:38:17"
        df_info.loc[5,'File Info'] = f"Modified At:{datetime_obj.date()} 11:38:17"

        # fix min max  frequency
        set_min_freq = str(self.df['Frequency (Hz)'].min())
        set_max_freq = str(self.df['Frequency (Hz)'].max())

        min_freq = Quantity(f'{set_min_freq} Hz')
        max_freq = Quantity(f'{set_max_freq} Hz')


        df_info.loc[13,'File Info'] = f"Minimum Frequency:{min_freq} "
        df_info.loc[14,'File Info'] = f"Minimum Frequency:{max_freq} "


        # fix Measurement Result and   Measurement Unit 
        df_info.loc[16,'File Info'] = f"Measurement Result: pro_{pro}_1_000002_{date}_0101 "


        #min max convert to Hz 
        df_info.loc[20,'File Info'] = f" Minimum Frequency:{set_min_freq} Hz"
        df_info.loc[21,'File Info'] = f" Minimum Frequency:{set_max_freq} Hz"


        return df_info

    
    def pro_1(self,date,**kwargs):
        
        #set data 
        pro_1 = {"B1":[int(30 * 1e6),int(47 * 1e6),int(25 * 1e3)],
                "B2":[int(47 * 1e6),int(68 * 1e6),int(12.5 * 1e3)],
                "B3":[int(68 * 1e6),int(78 * 1e6),int(25 * 1e3)],
                "B4":[int(79 * 1e6),int(87 * 1e6),int(25 * 1e3)],
                "B5":[int(87 * 1e6),int(108 * 1e6),int(250 * 1e3)],
                "B6":[int(474 * 1e6),int(690 * 1e6),int(8 * 1e6)]}
   
     
        #set frequency 
        freq = kwargs.get('freq',[])

        #process
        i = 0
        for k,v in pro_1.items():
            #create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            #self.df['Frequency (Hz)'] = pd.Series(range(pro_1['start'],pro_1['stop']+ pro_1['step'],pro_1['step']))
            self.df['Frequency (Hz)'] = pd.Series(range(v[0], v[1] + v[2], v[2]))            
            self.process(freq)
            self.df['File Info'] = self.create_info(1,date)

            self.df.to_csv(f"test{i}.csv",index=False)


        return True









pro = Pro()
print(pro.pro_1(230501,freq = None))