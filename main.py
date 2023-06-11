import pandas as pd 
from quantiphy import Quantity
from datetime import datetime





class Pro:
    def __init__(self):
        self.df = pd.DataFrame() 
       
    #detect frequency
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
    

    def pro_2(self,date,**kwargs):
                #set data 
        pro_2 = {"B1":[int(108 * 1e6),int(118 * 1e6),int(50 * 1e3)],
                "B2":[int(118 * 1e6),int(137 * 1e6),int(25 * 1e3)],
                "B3":[int(137 * 1e6),int(156 * 1e6),int(12.5 * 1e3)],
                "B4":[int(156 * 1e6),int(162.05 * 1e6),int(25 * 1e6)],
                "B5":[int(162.05 * 1e6),int(174 * 1e6),int(12.5 * 1e6)],
                "B6":[int(174.9280 * 1e6),int(176.6400 * 1e6),int(178.3520 * 1e6),
                      int(180.0640* 1e6),int(181.9360 * 1e6),int(183.6480 * 1e6),
                      int(185.3600 * 1e6),int(187.0720 * 1e6),int(188.9280 * 1e6),
                      int(190.6400 * 1e6),int(192.3520 * 1e6),int(194.0640 * 1e6),
                      int(195.9360 * 1e6),int(197.6480 * 1e6),int(199.3600 * 1e6),
                      int(201.0720 * 1e6),int(202.9280 * 1e6),int(204.6400 * 1e6),
                      int(206.3520 * 1e6),int(208.0640 * 1e6),int(209.9360 * 1e6),
                      int(211.6480 * 1e6),int(213.3600 * 1e6),int(215.0720 * 1e6),
                      int(216.9280* 1e6),int(218.6400 * 1e6),int(220.3520 * 1e6),
                      int(222.0640 * 1e6),int(223.9360 * 1e6),int(225.6480 * 1e6),
                      int(227.3600 * 1e6),int(229.0720 * 1e6)]}
        
        freq = kwargs.get('freq',[])

        #process
        i = 0
        for k,v in pro_2.items():
            #create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            
            #add frequency_list
            if k == "B8":
                self.df['Frequency (Hz)'] = pro_2["B6"]
                self.process(freq)
                self.df['File Info'] = self.create_info(1,date)

                self.df.to_csv(f"test{i}.csv",index=False)


            else:
                self.df['Frequency (Hz)'] = pd.Series(range(v[0], v[1] + v[2], v[2]))            
                self.process(freq)
                self.df['File Info'] = self.create_info(1,date)

                self.df.to_csv(f"test{i}.csv",index=False)
            
                

    def pro_3(self,date,**kwargs):
        
        pro_3 = {"B1":[int(230 * 1e6),int(245 * 1e6),int(25 * 1e3)],
                 "B2":[int(247 * 1e6),int(300 * 1e6),int(25 * 1e3)],
                 "B3":[int(300 * 1e6),int(320.1 * 1e6),int(300 * 1e3)],
                 "B4":[int(300.15 * 1e6),int(319.95 * 1e6),int(300 * 1e6)],
                 "B5":[int(320.1 * 1e6),int(328.6 * 1e6),int(25 * 1e6)],
                 "B6":[int(328.7 * 1e6),int(335.3 * 1e6),int(150 * 1e3),]}
        

          #set frequency 
        freq = kwargs.get('freq',[])

        #process
        i = 0
        for k,v in pro_3.items():
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
#print(pro.pro_1(230501,freq = None))

pro.pro_2(230501,freq=None)