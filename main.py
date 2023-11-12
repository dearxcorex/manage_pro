from process import run
from datetime import datetime, timedelta
from automate.automate import NBTC_Automation
from frequencies import found_freq


#interect with user
def start():
    while True:
        try:
            choice = int(input("Enter 1 to select pro or 2 to run all pro or 3 for automation OPER[1,2,3] : "))
            if choice not in [1,2,3]:
                raise ValueError("Please enter 1 or 2, 3")    
            if choice == 1:
                handle_select_pro()
            elif choice == 2:
                handle_all_pro()
            else:
                easy_oper()
                break

            if  ask_for_automation():
                easy_oper()
            break

        except ValueError as e :
            print(e)
    
def handle_select_pro():
        input_date = get_valid_date("Enter date (YYMMDD): ")
        input_pro = get_valid_pro("Enter pro  : ",range(1,14))
        input_percent_occunpancy_min = int(input("Enter Min_percent_occunpancy: "))
        input_percent_occunpancy_max = int(input("Enter Max_percent_occunpancy: "))
        select_pro(input_date, input_pro, input_percent_occunpancy_min, input_percent_occunpancy_max)


def handle_all_pro():
    input_date = input("Enter date (YYMMDD): ")
    all_pro(input_date)


def get_valid_date(prompt):
    while True:
        try:
            input_date = input(prompt)
            return datetime.strptime(input_date, '%y%m%d').strftime('%y%m%d')
        except ValueError:
            print("Please enter correct date format (YYMMDD)")

def get_valid_pro(prompt,value_range=None):
    while True:
        try:
            value = int(input(prompt))
            if value_range and value not in value_range:
                raise ValueError("Please enter correct pro (1-13)")
            return value
        except ValueError as e :
            print(e)


def ask_for_automation():
    return input("Do you want to automate? (y/n): ").lower() == "y"


def easy_oper():
    automation = NBTC_Automation("tossakun.y", "022135Bon!")
    automation.run()
    automation.close()

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
    elif pro == 12:
        run.pro_12(date,num1,num2, freq=found_freq["pro12"])
    elif pro == 13:
        run.pro_13(date,num1,num2, freq=found_freq["pro13"])
        


def all_pro(date,):
    date_format = '%y%m%d'
    current_date = datetime.strptime(date, date_format)

    run.pro_1(current_date.strftime(date_format),0,0,freq=found_freq["pro1"])
    current_date += timedelta(days=1)

    run.pro_2(current_date.strftime(date_format),20,55, freq=found_freq["pro2"])
    
    current_date += timedelta(days=1)
    run.pro_3(current_date.strftime(date_format),20,55, freq=found_freq["pro3"])
    
    current_date += timedelta(days=1)
    run.pro_4(current_date.strftime(date_format),30,45 ,freq=found_freq["pro4"])
    
    current_date += timedelta(days=1)
    run.pro_5(current_date.strftime(date_format),30,45 , freq=found_freq["pro5"])
    
    current_date += timedelta(days=1)
    run.pro_6(current_date.strftime(date_format),45,55 , freq=found_freq["pro6"])

    current_date += timedelta(days=1)
    run.pro_7(current_date.strftime(date_format),0,0, freq=found_freq["pro7"])

    current_date += timedelta(days=1)
    run.pro_8(current_date.strftime(date_format),0,0, freq=found_freq["pro8"])

    current_date += timedelta(days=1)
    run.pro_9(current_date.strftime(date_format),0,0, freq=found_freq["pro9"])
   
    current_date += timedelta(days=1)
    run.pro_10(current_date.strftime(date_format),0,0, freq=found_freq["pro10"])

    current_date += timedelta(days=1)
    run.pro_11(current_date.strftime(date_format),0,0, freq=found_freq["pro11"])

   

if __name__ == "__main__":  
    start()