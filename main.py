from process import run
from datetime import datetime, timedelta




def select_pro(date, pro,num1=0,num2=0):
    if pro == 1:
        run.pro_1(date,num1,num2, freq=found_freq["pro1"])
    elif pro == 2:
        run.pro_2(date,num1,num2, freq=found_freq["pro2"])
    elif pro == 3:
        run.pro_3(date,num1,num2, freq=found_freq["pro3"])
    elif pro == 4:
        run.pro_4(date,num1,num2, freq=found_freq["pro4"])
    elif pro == 5:
        run.pro_5(date,num1,num2, freq=found_freq["pro5"])
    elif pro == 6:
        run.pro_6(date,num1,num2, freq=found_freq["pro6"])
    elif pro == 7:
        run.pro_7(date,num1,num2, freq=None)
    elif pro == 8:
        run.pro_8(date,num1,num2, freq=None)
    elif pro == 9:
        run.pro_9(date,num1,num2, freq=found_freq["pro9"])
    elif pro == 10:
        run.pro_10(date,num1,num2, freq=None)

    elif pro == 11:
        run.pro_11(date,num1,num2, freq=None)


def all_pro(date):
    date_format = '%y%m%d'
    current_date = datetime.strptime(date, date_format)

    run.pro_1(current_date.strftime(date_format),freq=found_freq["pro1"])
    current_date += timedelta(days=1)

    run.pro_2(current_date.strftime(date_format), freq=found_freq["pro2"])
    
    current_date += timedelta(days=1)
    run.pro_3(current_date.strftime(date_format), freq=found_freq["pro3"])
    
    current_date += timedelta(days=1)
    run.pro_4(current_date.strftime(date_format), freq=found_freq["pro4"])
    
    current_date += timedelta(days=1)
    run.pro_5(current_date.strftime(date_format), freq=found_freq["pro5"])
    
    current_date += timedelta(days=1)
    run.pro_6(current_date.strftime(date_format), freq=found_freq["pro6"])

    current_date += timedelta(days=1)
    run.pro_7(current_date.strftime(date_format), freq=found_freq["pro7"])

    current_date += timedelta(days=1)
    run.pro_8(current_date.strftime(date_format), freq=found_freq["pro8"])

    current_date += timedelta(days=1)
    run.pro_9(current_date.strftime(date_format), freq=found_freq["pro9"])
   
    current_date += timedelta(days=1)
    run.pro_10(current_date.strftime(date_format), freq=found_freq["pro10"])

    current_date += timedelta(days=1)
    run.pro_11(current_date.strftime(date_format), freq=found_freq["pro11"])



found_freq = {
    
                "pro1":None,
                "pro2":[120.95, 121.1, 124.35, 131.5, 133.1, 122.35, 128.1, 128.95, 135.5, 123.4, 123.6, 124.5, 125.2, 126.5, 144.3875,

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
                        154.5375,
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
                        168.95,
                        171.0125,
                        173.7375,],
                "pro3":[
                        245,
                        340.5,
                        348.84],
                "pro4":[390.45,
                        390.7,
                        391.7,
                        391.45,
                        ],
                "pro5":[430.225,                 
                        440.6125,
                        440.625,
                        440.6375,
                        440.65,
                        440.6625,
                        440.675,
                        440.6875,
                        440.7,
                        440.7125,
                        440.7375,
                        440.75,
                        440.7625,
                        440.775,
                        440.7875,
                        440.8,
                        440.8125,
                        440.825,
                        440.8375,
                        440.85,
                        440.8625,
                        440.875,
                        440.8875,
                        440.9,
                        445.6125,
                        445.625,
                        445.6375,
                        445.65,
                        445.6625,
                        445.675,
                        445.6875,
                        445.7,
                        445.7125,
                        445.725,
                        445.7375,
                        445.75,
                        445.7625,
                        445.775,
                        445.7875,
                        445.8,
                        440.725,],
                "pro6":[770.5,
                        775.5,
                        760.5,
                        765.5,
                        770.5,
                        775.5,
                        780.5,
                        785.5,
                        790.5,
                        831.5,
                        836.5,
                        871.5,
                        876.5,
                        881.5,
                        892.5,
                        897.5,
                        902.5,
                        907.5,
                        912.5,
                        937.5,
                        942.5,
                        947.5,
                        952.5,
                        957.5,
                            ],
                "pro7":None,
                "pro8":None,
                "pro9":[1712.5, 1747, 5, 1807.5, 1812.5, 1827.5, 1832.5, 1837.5, 1922.5, 1927.5, 1937.5,
                        2112.5, 2117.5, 2122.5, 2127.5, 2142.5, 2152.5, 2322.5, 2332.5, 2342.5, 2362.5, 2532.5, 2557.5],
            
                "pro10":None,
                "pro11":None,
            
            }


# all_pro("210101")

select_pro("210101", 5,50,80)