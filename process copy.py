import pandas as pd
import random as rd
from datetime import datetime
from quantiphy import Quantity


class Create:
    def __init__(self):
        self.df = pd.DataFrame()

    def make_occ(self, freq):
        self.df["Occupancy (%)"] = 0
        if freq:
            for f in freq:
                self.df.loc[self.df['Frequency (Hz)'] == f *
                            1e6, 'Occupancy (%)'] = rd.randint(23, 48)

    def create_info(self, pro, date):
        df_info = pd.read_csv("ref_data/pro_9.csv",
                              usecols=["File Info"], encoding="ISO-8859-1")
        date_str = datetime.strptime(str(date), "%y%m%d").date()
        file_name = f"pro_{pro}_1_000002_{date}_0101_OC"
        records = len(self.df['Frequency (Hz)'])

        df_info_dict = {
            0: f"File Name:{file_name}",
            3: f"Records:{records}",
            4: f"Created At:{date_str} 11:38:17",
            5: f"Modified At:{date_str} 11:38:17",
            13: f"Minimum Frequency:{Quantity(str(self.df['Frequency (Hz)'].min()))} Hz",
            14: f"Minimum Frequency:{Quantity(str(self.df['Frequency (Hz)'].max()))} Hz",
            16: f"Measurement Result: {file_name}",
            20: f"Minimum Frequency:{self.df['Frequency (Hz)'].min()} Hz",
            21: f"Minimum Frequency:{self.df['Frequency (Hz)'].max()} Hz",
        }

        for key, val in df_info_dict.items():
            df_info.loc[key, 'File Info'] = val

        return df_info

    def create_band_df(self, band, date, pro, freq):
        start, stop, step = band
        self.df['Frequency (Hz)'] = pd.Series(range(start, stop + step, step))
        self.make_occ(freq)
        self.df['File Info'] = self.create_info(pro, date)
    # automate\fco_data

    def save_df(self, pro_num, band_num):
        self.df.to_csv(
            f"automate/fco_data/pro_{pro_num}_{band_num}.csv", index=False)
    # automate\fco_data

    def pro(self, num, date, bands, **kwargs):
        freq = kwargs.get('freq', [])
        for i, band_key in enumerate(bands, start=1):
            self.df = pd.DataFrame()
            self.create_band_df(bands[band_key], date, num, freq)
            self.save_df(num, i)
        return True


    # Dictionary to hold band ranges (start, stop, step) for each pro_*
bands, = {
    "pro_1": {
        "B1": [int(30e6), int(47e6), int(25e3)],
        "B2": [int(47e6), int(68e6), int(12.5e3)],
        "B3": [int(68 * 1e6), int(78 * 1e6), int(25 * 1e3)],
        "B4": [int(79 * 1e6), int(87 * 1e6), int(25 * 1e3)],
        "B5": [int(87 * 1e6), int(108 * 1e6), int(250 * 1e3)],
        "B6": [int(474 * 1e6), int(690 * 1e6), int(8 * 1e6)]
    },

    "pro_2": {
        "B1": [int(108 * 1e6), int(118 * 1e6), int(50 * 1e3)],
        "B2": [int(118 * 1e6), int(137 * 1e6), int(25 * 1e3)],
        "B3": [int(137 * 1e6), int(156 * 1e6), int(12.5 * 1e3)],
        "B4": [int(156 * 1e6), int(162.05 * 1e6), int(25 * 1e3)],
        "B5": [int(162.05 * 1e6), int(174 * 1e6), int(12.5 * 1e3)],
        "B6": [int(174.9280 * 1e6), int(176.6400 * 1e6), int(178.3520 * 1e6),
               int(180.0640 * 1e6), int(181.9360 * 1e6), int(183.6480 * 1e6),
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
               int(227.3600 * 1e6), int(229.0720 * 1e6)]
    },

    "pro_3": {"B1": [int(230 * 1e6), int(245 * 1e6), int(25 * 1e3)],
              "B2": [int(247 * 1e6), int(300 * 1e6), int(25 * 1e3)],
              "B3": [int(300 * 1e6), int(320.1 * 1e6), int(300 * 1e3)],
              "B4": [int(300.15 * 1e6), int(319.95 * 1e6), int(300 * 1e3)],
              "B5": [int(320.1 * 1e6), int(328.6 * 1e6), int(25 * 1e3)],
              "B6": [int(328.7 * 1e6), int(335.3 * 1e6), int(150 * 1e3)],
              "B7": [int(335.4 * 1e6), int(380 * 1e6), int(25 * 1e3)]
              },

    "pro_4": {
        "B1": [int(380.00625 * 1e6), int(430 * 1e6), int(12.5 * 1e3)]
    },
    "pro_5": {
        "B1": [int(430 * 1e6), int(470 * 1e6), int(25 * 1e3)]
    },
    "pro_6": {"B1": [int(705.5 * 1e6), int(800 * 1e6), int(5000 * 1e3)],
              "B2": [int(826.5 * 1e6), int(831.5 * 1e6), int(836.5 * 1e6),
                     int(871.5*1e6), int(876.5*1e6), int(881.5*1e6)],
              "B3": [int(892.5 * 1e6), int(897.5 * 1e6), int(902.5 * 1e6),
                     int(907.5*1e6), int(912.5*1e6), int(937.5*1e6),
                     int(942.5*1e6), int(947.5*1e6), int(952.5*1e6),
                     int(957.5*1e6)]},

    "pro_7": {"B1": [int(839 * 1e6), int(851 * 1e6), int(25 * 1e3)],
              "B2": [int(884 * 1e6), int(890 * 1e6), int(25 * 1e3)],
              "B4": [int(930 * 1e6), int(935 * 1e6), int(25 * 1e3)],

              },

    "pro_8": {
        "B2": [int(1215 * 1e6), int(1427 * 1e6), int(250 * 1e3)]
    },
    "pro_9": {"B1": [int(1712.5 * 1e6), int(1842.5 * 1e6), int(5 * 1e6)],
              "B3": [int(1922.5 * 1e6), int(2167.5 * 1e6), int(5 * 1e6)],
              "B5": [int(2312.5 * 1e6), int(2687.5 * 1e6), int(5 * 1e6)],
              },
    "pro_10": {"B1": [int(1750 * 1e6), int(1805 * 1e6), int(250 * 1e3)],
               "B3": [int(1845 * 1e6), int(1920 * 1e6), int(250 * 1e3)],
               "B5": [int(1980 * 1e6), int(2025 * 1e6), int(250 * 1e3)],
               "B7": [int(2300 * 1e6), int(2310 * 1e6), int(250 * 1e3)],
               "B8": [int(2370 * 1e6), int(2400 * 1e6), int(250 * 1e3)],
               },

    "pro_11": {"B2": [int(2053.5 * 1e6), int(2060 * 1e6), int(250 * 1e3)],
               "B6": [int(2170 * 1e6), int(2200.5 * 1e6), int(250 * 1e3)],
               "B8": [int(2228.5 * 1e6), int(2230 * 1e6), int(250 * 1e3)],
               "B9": [int(2240 * 1e6), int(2250 * 1e6), int(250 * 1e3)],
               "B12": [int(2900 * 1e6), int(3000 * 1e6), int(250 * 1e3)],
               },


},


creator = Create()
# creator.pro(1, 231011, bands["pro_1"], freq=[87.5,
#                                              88,
#                                              88.25,
#                                              89,
#                                              89.25,
#                                              89.75,
#                                              90,
#                                              90.25,
#                                              90.5,
#                                              91,
#                                              91.5,
#                                              91.75,
#                                              92,
#                                              92.25,
#                                              93,
#                                              93.75,
#                                              94.25,
#                                              94.5,
#                                              94.75,
#                                              95,
#                                              95.25,
#                                              95.75, 522, 546, 570, 602, 634])

creator.pro(1, 230802, bands["pro_2"], freq=[120.95, 121.1, 124.35, 131.5, 133.1, 122.35, 128.1, 128.95, 135.5, 123.4, 123.6, 124.5, 125.2, 126.5, 144.3875,
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


# creator.pro(3, 230803, bands["pro_3"], freq=[245,
#                                              238.875,
#                                              240.5,
#                                              324,
#                                              340.5,
#                                              348.84])
# creator.pro(4, 230804, bands["pro_4"], freq=[390.45,
#                                              390.7,
#                                              391.45,
#                                              430.225,
#                                              440.6125,
#                                              440.625,
#                                              440.6375,
#                                              440.65,
#                                              440.6625,
#                                              440.675,
#                                              440.6875,
#                                              440.7,
#                                              440.7125,
#                                              440.7375,
#                                              440.75,
#                                              440.7625,
#                                              440.775,
#                                              440.7875,
#                                              440.8,
#                                              440.8125,
#                                              440.825,
#                                              440.8375,
#                                              440.85,
#                                              440.8625,
#                                              440.875,
#                                              440.8875,
#                                              440.9,
#                                              445.6125,
#                                              445.625,
#                                              445.6375,
#                                              445.65,
#                                              445.6625,
#                                              445.675,
#                                              445.6875,
#                                              445.7,
#                                              445.7125,
#                                              445.725,
#                                              445.7375,
#                                              445.75,
#                                              445.7625,
#                                              445.775,
#                                              445.7875,
#                                              445.8,
#                                              440.725,
#                                              ])
# creator.pro(5, 230804, bands["pro_5"], freq=[430.225,
#                                              440.6125,
#                                              440.625,
#                                              440.6375,
#                                              440.65,
#                                              440.6625,
#                                              440.675,
#                                              440.6875,
#                                              440.7,
#                                              440.7125,
#                                              440.7375,
#                                              440.75,
#                                              440.7625,
#                                              440.775,
#                                              440.7875,
#                                              440.8,
#                                              440.8125,
#                                              440.825,
#                                              440.8375,
#                                              440.85,
#                                              440.8625,
#                                              440.875,
#                                              440.8875,
#                                              440.9,
#                                              445.6125,
#                                              445.625,
#                                              445.6375,
#                                              445.65,
#                                              445.6625,
#                                              445.675,
#                                              445.6875,
#                                              445.7,
#                                              445.7125,
#                                              445.725,
#                                              445.7375,
#                                              445.75,
#                                              445.7625,
#                                              445.775,
#                                              445.7875,
#                                              445.8,
#                                              440.725,])

# creator.pro(6, 230804, bands["pro_6"], freq=[770.5,
#                                              775.5,
#                                              760.5,
#                                              765.5,
#                                              770.5,
#                                              775.5,
#                                              780.5,
#                                              785.5,
#                                              790.5,
#                                              861.5,
#                                              859,
#                                              864,
#                                              869,
#                                              ])


# creator.pro(11,)
