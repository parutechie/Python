from distutils.log import error
from reprlib import recursive_repr
from webbrowser import get

def get_principle():
    initial_principle = float(input("Enter the initial_principle: "))
    while (initial_principle <=0 or initial_principle >= 10000000000):
        initial_principle = get_principle()
    return initial_principle

def get_interest_rate():
    interest_rate = float(input("Enter the the interest_rates: "))
    while(interest_rate <=0 or interest_rate > 100):
            interest_rate = get_interest_rate()
    return interest_rate

def get_interest_change_per_period():
    interest_change_per_period =  float(input("Enter the interest_change_per_period "))
    while(interest_change_per_period<0 or interest_change_per_period>100):
            interest_change_per_period = get_interest_change_per_period()
    return interest_change_per_period

def get_time_period_elapsed():
    time_period_elapsed = float(input("Enter the time_period_elapsed: "))
    while(time_period_elapsed<0 or time_period_elapsed>1000):
            time_period_elapsed = get_time_period_elapsed()
    return time_period_elapsed

while(True):
    try:

        initial_principle = get_principle()
        interest_rate = get_interest_rate()
        interest_change_per_period = get_interest_change_per_period()
        time_period_elapsed = get_time_period_elapsed()

        compound_interest_final_amount= initial_principle * pow((1 + interest_rate/interest_change_per_period),interest_change_per_period*time_period_elapsed)
        print(compound_interest_final_amount)

    except:
        print("Wrong input")
        

    finally:
        print("finally")



