def get_principle():
    return float(input("Enter the initial_principle: "))

def get_interest_rate():
    return float(input("Enter the the interest_rates: "))

def get_interest_change_per_period():
    return float(input("Enter the interest_change_per_period "))

def get_time_period_elapsed():
    return float(input("Enter the time_period_elapsed: "))

error_point=""
while(True):
    try:
        initial_principle = get_principle()
        if (initial_principle>0 and initial_principle<10000000000):
            interest_rate = get_interest_rate()
            if (interest_rate >=0 and interest_rate <=100):
                interest_change_per_period = get_interest_change_per_period()
                if (interest_change_per_period>=0 and interest_change_per_period<=100):
                    time_period_elapsed = get_time_period_elapsed()
                    if (time_period_elapsed>=0 and time_period_elapsed<=1000):
                        compound_interest_final_amount= initial_principle * pow((1 + interest_rate/interest_change_per_period),interest_change_per_period*time_period_elapsed)
                        print(compound_interest_final_amount)
                    else:
                        print ("invalid time_period_elasped")
                        error_point="INVALID_TIME_ELAPSED"
                else:
                    print("invalid interest_change_period")
                    error_point="INVALID_INTEREST_CHANGE_PERIOD"
            else:
                print ("invalid interest rate")
                error_point="INTEREST_RATE"
        else:
            print ("invalid principle")
            error_point="INVALID_PRINCIPLE"
    except:
        print("Wrong input")
