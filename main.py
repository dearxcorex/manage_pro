import pandas as pd
from quantiphy import Quantity
from datetime import datetime
import random as rd


class Pro:
    def __init__(self):
        self.df = pd.DataFrame()

    # detect frequency
    def process(self, freq):
        if freq is not None:
            freq = [i * 1e6 for i in freq]

            for v in freq:
                self.df.loc[self.df['Frequency (Hz)']
                            == v, 'Occupancy (%)'] = rd.randint(47, 67)
                self.df.loc[~self.df['Frequency (Hz)'].isin(
                    (freq)), 'Occupancy (%)'] = int(0)
        else:
            self.df["Occupancy (%)"] = 0

    def create_info(self, pro, date):
        # get info

        df_info = pd.read_csv("ref_data/pro_9.csv",
                              usecols=["File Info"], encoding="ISO-8859-1")

        # data
        df_info.loc[0,
                    'File Info'] = f"File Name:pro_{pro}_1_000002_{date}_0101_OC"
        # records
        records = len(self.df['Frequency (Hz)'])
        df_info.loc[3, 'File Info'] = f'Records:{records}'

        # date
        days_to_add = str(date)
        datetime_obj = datetime.strptime(days_to_add, "%y%m%d")
        df_info.loc[4,
                    'File Info'] = f"Created At:{datetime_obj.date()} 11:38:17"
        df_info.loc[5,
                    'File Info'] = f"Modified At:{datetime_obj.date()} 11:38:17"

        # fix min max  frequency
        set_min_freq = str(self.df['Frequency (Hz)'].min())
        set_max_freq = str(self.df['Frequency (Hz)'].max())

        min_freq = Quantity(f'{set_min_freq} Hz')
        max_freq = Quantity(f'{set_max_freq} Hz')

        df_info.loc[13, 'File Info'] = f"Minimum Frequency:{min_freq} "
        df_info.loc[14, 'File Info'] = f"Minimum Frequency:{max_freq} "

        # fix Measurement Result and   Measurement Unit
        df_info.loc[16,
                    'File Info'] = f"Measurement Result: pro_{pro}_1_000002_{date}_0101 "

        # min max convert to Hz
        df_info.loc[20, 'File Info'] = f" Minimum Frequency:{set_min_freq} Hz"
        df_info.loc[21, 'File Info'] = f" Minimum Frequency:{set_max_freq} Hz"

        return df_info

    def pro_1(self, date, **kwargs):

        # set data
        pro_1 = {"B1": [int(30 * 1e6), int(47 * 1e6), int(25 * 1e3)],
                 "B2": [int(47 * 1e6), int(68 * 1e6), int(12.5 * 1e3)],
                 "B3": [int(68 * 1e6), int(78 * 1e6), int(25 * 1e3)],
                 "B4": [int(79 * 1e6), int(87 * 1e6), int(25 * 1e3)],
                 "B5": [int(87 * 1e6), int(108 * 1e6), int(250 * 1e3)],
                 "B6": [int(474 * 1e6), int(690 * 1e6), int(8 * 1e6)]}

        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_1.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            # self.df['Frequency (Hz)'] = pd.Series(range(pro_1['start'],pro_1['stop']+ pro_1['step'],pro_1['step']))
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_1_{i}.csv", index=False)

        return True

    def pro_2(self, date, **kwargs):
        # set data
        pro_2 = {"B1": [int(108 * 1e6), int(118 * 1e6), int(50 * 1e3)],
                 "B2": [int(118 * 1e6), int(137 * 1e6), int(25 * 1e3)],
                 "B3": [int(137 * 1e6), int(156 * 1e6), int(12.5 * 1e3)],
                 "B4": [int(156 * 1e6), int(162.05 * 1e6), int(25 * 1e3)],
                 "B5": [int(162.05 * 1e6), int(174 * 1e6), int(12.5 * 1e3)],
                 "B6": [int(174.9280 * 1e6), int(176.6400 * 1e6), int(178.3520 * 1e6),
                        int(180.0640 * 1e6), int(181.9360 *
                                                 1e6), int(183.6480 * 1e6),
                        int(185.3600 * 1e6), int(187.0720 *
                                                 1e6), int(188.9280 * 1e6),
                        int(190.6400 * 1e6), int(192.3520 *
                                                 1e6), int(194.0640 * 1e6),
                        int(195.9360 * 1e6), int(197.6480 *
                                                 1e6), int(199.3600 * 1e6),
                        int(201.0720 * 1e6), int(202.9280 *
                                                 1e6), int(204.6400 * 1e6),
                        int(206.3520 * 1e6), int(208.0640 *
                                                 1e6), int(209.9360 * 1e6),
                        int(211.6480 * 1e6), int(213.3600 *
                                                 1e6), int(215.0720 * 1e6),
                        int(216.9280 * 1e6), int(218.6400 *
                                                 1e6), int(220.3520 * 1e6),
                        int(222.0640 * 1e6), int(223.9360 *
                                                 1e6), int(225.6480 * 1e6),
                        int(227.3600 * 1e6), int(229.0720 * 1e6)]}

        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_2.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1

            # add frequency_list
            if k == "B6":
                self.df['Frequency (Hz)'] = pro_2["B6"]
                self.process(freq)
                self.df['File Info'] = self.create_info(1, date)

                self.df.to_csv(f"pro_2_{i}.csv", index=False)

            else:
                self.df['Frequency (Hz)'] = pd.Series(
                    range(v[0], v[1] + v[2], v[2]))
                self.process(freq)
                self.df['File Info'] = self.create_info(1, date)

                self.df.to_csv(f"pro_2_{i}.csv", index=False)

        return True

    def pro_3(self, date, **kwargs):

        pro_3 = {"B1": [int(230 * 1e6), int(245 * 1e6), int(25 * 1e3)],
                 "B2": [int(247 * 1e6), int(300 * 1e6), int(25 * 1e3)],
                 "B3": [int(300 * 1e6), int(320.1 * 1e6), int(300 * 1e3)],
                 "B4": [int(300.15 * 1e6), int(319.95 * 1e6), int(300 * 1e3)],
                 "B5": [int(320.1 * 1e6), int(328.6 * 1e6), int(25 * 1e3)],
                 "B6": [int(328.7 * 1e6), int(335.3 * 1e6), int(150 * 1e3)],
                 "B7": [int(335.4 * 1e6), int(380 * 1e6), int(25 * 1e3)]}

        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_3.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_3{i}.csv", index=False)

        return True

    def pro_4(self, date, **kwargs):
        pro_4 = {"B1": [int(380.00625 * 1e6), int(430 * 1e6), int(12.5 * 1e3)]}
        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_4.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_4{i}.csv", index=False)

        return True

    def pro_5(self, date, **kwargs):
        pro_5 = {"B1": [int(430 * 1e6), int(470 * 1e6), int(25 * 1e3)]}
        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_5.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_5_5{i}.csv", index=False)

        return True

    def pro_6(self, date, **kwargs):
        pro_6 = {"B1": [int(705.5 * 1e6), int(800 * 1e6), int(5000 * 1e3)],
                 "B2": [int(826.5 * 1e6), int(831.5 * 1e6), int(836.5 * 1e6),
                        int(871.5*1e6), int(876.5*1e6), int(881.5*1e6)],
                 "B3": [int(892.5 * 1e6), int(897.5 * 1e6), int(902.5 * 1e6),
                        int(907.5*1e6), int(912.5*1e6), int(937.5*1e6),
                        int(942.5*1e6), int(947.5*1e6), int(952.5*1e6),
                        int(957.5*1e6)]}
        # set frequency

        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_6.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            if k == 'B2':
                self.df['Frequency (Hz)'] = pro_6["B2"]
                self.process(freq)
                self.df['File Info'] = self.create_info(6, date)
                self.df.to_csv(f"pro_6_6{i}.csv", index=False)
            elif k == 'B3':
                self.df['Frequency (Hz)'] = pro_6["B3"]
                self.process(freq)
                self.df['File Info'] = self.create_info(6, date)
                self.df.to_csv(f"pro_6_6{i}.csv", index=False)

            else:
                self.df['Frequency (Hz)'] = pd.Series(
                    range(v[0], v[1] + v[2], v[2]))
                self.process(freq)
                self.df['File Info'] = self.create_info(6, date)

                self.df.to_csv(f"pro_6_6{i}.csv", index=False)

        return True

    def pro_7(self, date, **kwargs):
        pro_7 = {"B1": [int(839 * 1e6), int(851 * 1e6), int(25 * 1e3)],
                 "B2": [int(884 * 1e6), int(890 * 1e6), int(25 * 1e3)],
                 "B4": [int(930 * 1e6), int(935 * 1e6), int(25 * 1e3)], }

        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_7.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            # self.df['Frequency (Hz)'] = pd.Series(range(pro_1['start'],pro_1['stop']+ pro_1['step'],pro_1['step']))
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_7_{i}.csv", index=False)

        return True

    def pro_8(self, date, **kwargs):
        pro_8 = {"B2": [int(1215 * 1e6), int(1427 * 1e6), int(250 * 1e3)],
                 }
        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_8.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            # self.df['Frequency (Hz)'] = pd.Series(range(pro_1['start'],pro_1['stop']+ pro_1['step'],pro_1['step']))
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_8_{i}.csv", index=False)

        return True

    def pro_9(self, date, **kwargs):
        pro_9 = {"B1": [int(1712.5 * 1e6), int(1842.5 * 1e6), int(5 * 1e6)],
                 "B3": [int(1922.5 * 1e6), int(2167.5 * 1e6), int(5 * 1e6)],
                 "B5": [int(2312.5 * 1e6), int(2687.5 * 1e6), int(5 * 1e6)],
                 }
        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_9.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            # self.df['Frequency (Hz)'] = pd.Series(range(pro_1['start'],pro_1['stop']+ pro_1['step'],pro_1['step']))
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_9_{i}.csv", index=False)

        return True

    def pro_10(self, date, **kwargs):
        pro_10 = {"B1": [int(1750 * 1e6), int(1805 * 1e6), int(250 * 1e3)],
                  "B3": [int(1845 * 1e6), int(1920 * 1e6), int(250 * 1e3)],
                  "B5": [int(1980 * 1e6), int(2025 * 1e6), int(250 * 1e3)],
                  "B7": [int(2300 * 1e6), int(2310 * 1e6), int(250 * 1e3)],
                  "B8": [int(2370 * 1e6), int(2400 * 1e6), int(250 * 1e3)],
                  }
        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_10.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            # self.df['Frequency (Hz)'] = pd.Series(range(pro_1['start'],pro_1['stop']+ pro_1['step'],pro_1['step']))
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_10_{i}.csv", index=False)

        return True

    def pro_11(self, date, **kwargs):
        pro_11 = {"B2": [int(2053.5 * 1e6), int(2060 * 1e6), int(250 * 1e3)],
                  "B6": [int(2170 * 1e6), int(2200.5 * 1e6), int(250 * 1e3)],
                  "B8": [int(2228.5 * 1e6), int(2230 * 1e6), int(250 * 1e3)],
                  "B9": [int(2240 * 1e6), int(2250 * 1e6), int(250 * 1e3)],
                  "B12": [int(2900 * 1e6), int(3000 * 1e6), int(250 * 1e3)],
                  }
        # set frequency
        freq = kwargs.get('freq', [])

        # process
        i = 0
        for k, v in pro_11.items():
            # create new dataFrame every time
            self.df = pd.DataFrame()
            i += 1
            # self.df['Frequency (Hz)'] = pd.Series(range(pro_1['start'],pro_1['stop']+ pro_1['step'],pro_1['step']))
            self.df['Frequency (Hz)'] = pd.Series(
                range(v[0], v[1] + v[2], v[2]))
            self.process(freq)
            self.df['File Info'] = self.create_info(1, date)

            self.df.to_csv(f"pro_11_{i}.csv", index=False)

        return True


pro = Pro()
# print(pro.pro_1(230501,freq = None))
'''
pro.pro_2(230802, freq=[120.95, 121.1, 124.35, 131.5, 133.1, 122.35, 128.1, 128.95, 135.5, 123.4, 123.6, 124.5, 125.2, 126.5, 144.3875,
                        144.4625,
                        144.625,
                        145.0875,
                        145.1,
                        145.275,
                        145.375,
                        145.6875,
                        145.7,
                        146.25,
                        144.825,
                        144.875,
                        144.975,
                        144.525,
                        144.675,
                        145.225,
                        145.2625,
                        145.45,
                        144.55,
                        144.65,
                        144.7,
                        144.75,
                        144.85,
                        145.2,
                        145.325,
                        145.475,
                        145.75,
                        144.5875,
                        144.775,
                        145.3,
                        144.5375,
                        145.7125,
                        145.05,
                        144.05,
                        144.95,
                        145.0375,
                        145.075,
                        145.35,
                        145.675,
                        151.8,
                        155.775,
                        152.625,
                        151.7,
                        152.85,
                        154.45,
                        154.575,
                        155.15,
                        155.725,
                        159.3,
                        148.45,
                        152.475,
                        153.475,
                        154.425,
                        159.3125,
                        152.6,
                        153.2,
                        147.15,
                        152.65,
                        154.6375,
                        154.925,
                        155.4,
                        155.825,
                        155.975,
                        159.325,
                        147.825,
                        147.975,
                        149.775,
                        151.7125,
                        153.55,
                        154.5375,
                        154.5625,
                        154.7,
                        154.75,
                        154.775,
                        159.2875,
                        168.475,
                        168.875,
                        173.475,
                        171,
                        171.35,
                        171.375,
                        172.8,
                        173.025,
                        170,
                        162.75,
                        165.4,
                        161.225,
                        162.225,
                        162.125,
                        165.35,
                        171.3625,
                        168.775,
                        168.8875,
                        168.95,
                        171.0125,
                        171.1875,
                        171.3,
                        171.5625,
                        171.7125,
                        172.0125,
                        172.5125,
                        172.5375,
                        173.2125,
                        173.7375,])
'''
# pro.pro_3(230803, freq=[245,
#                         238.875,
#                         240.5,
#                         324,
#                         340.5,
#                         348.84])

# pro.pro_4(230804, freq=[390.45,
#                         390.7,
#                         391.45,
#                         430.225,
#                         440.6125,
#                         440.625,
#                         440.6375,
#                         440.65,
#                         440.6625,
#                         440.675,
#                         440.6875,
#                         440.7,
#                         440.7125,
#                         440.7375,
#                         440.75,
#                         440.7625,
#                         440.775,
#                         440.7875,
#                         440.8,
#                         440.8125,
#                         440.825,
#                         440.8375,
#                         440.85,
#                         440.8625,
#                         440.875,
#                         440.8875,
#                         440.9,
#                         445.6125,
#                         445.625,
#                         445.6375,
#                         445.65,
#                         445.6625,
#                         445.675,
#                         445.6875,
#                         445.7,
#                         445.7125,
#                         445.725,
#                         445.7375,
#                         445.75,
#                         445.7625,
#                         445.775,
#                         445.7875,
#                         445.8,
#                         440.725,
#                         ])
# pro.pro_5(230805, freq=[430.225,
#                         440.6125,
#                         440.625,
#                         440.6375,
#                         440.65,
#                         440.6625,
#                         440.675,
#                         440.6875,
#                         440.7,
#                         440.7125,
#                         440.7375,
#                         440.75,
#                         440.7625,
#                         440.775,
#                         440.7875,
#                         440.8,
#                         440.8125,
#                         440.825,
#                         440.8375,
#                         440.85,
#                         440.8625,
#                         440.875,
#                         440.8875,
#                         440.9,
#                         445.6125,
#                         445.625,
#                         445.6375,
#                         445.65,
#                         445.6625,
#                         445.675,
#                         445.6875,
#                         445.7,
#                         445.7125,
#                         445.725,
#                         445.7375,
#                         445.75,
#                         445.7625,
#                         445.775,
#                         445.7875,
#                         445.8,
#                         440.725,])

pro.pro_6(230806, freq=[770.5,
                        775.5,
                        760.5,
                        765.5,
                        770.5,
                        775.5,
                        780.5,
                        785.5,
                        790.5,
                        861.5,
                        859,
                        864,
                        869,
                        ])
