MIN_WAGE : float = 8.84

months: list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

class Job(object):
    """
    Represents a Job, which has an hourly rate and paid at the end of the month
    """

    def __init__(self,name='A Job',hourly=MIN_WAGE,holiday=0,night=0):
        self.name = name
        #The rates
        self.rate:float = float(hourly)
        self.rate_holiday:float = float(holiday)
        self.rate_night:float = float(night)

        self.night_hours:float = 0.0
        self.holy_hours:float = 0.0

        self.shift_night:bool = False
        self.shift_holy:bool = False
        self.special_pay:bool = False
        """
        Month:
        Date: hours
        """
        self.restart_year()
        self.__income = 0.0
        self.actual_month: int = 0


    def set_act_month(self, month:str="jan"):
        """
        Set the current month of the Job. Throws Error, when the entered month isn't on the months list
        """
        check:str = month.lower()
        for m in range(len(months)):
            if check.startswith(months[m]):
                self.actual_month = m
                break
            if m == len(months) - 1:
                print('''Error: The entered month does't exist. Please try on of the following:
                Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec''')
            
    def advance_month(self):
        """
        Add 1 to the actual_month, and reset its values to
        make sure that we are dealing with an empty month
        """
        self.actual_month += 1 % 12
        self.reset_curr_month()

    def reset_curr_month(self) ->None:
        """
        Reset all the values inside this month's dict
        """
        self.__year[ months[self.actual_month] ] = {}

    def restart_year(self) ->None:
        """
        Restart the values of the of this job
        """
        self.__year = { "jan":{}, "feb":{}, "mar":{}, "apr":{}, "may":{}, "jun":{}, "jul":{}, "aug":{}, "sep":{}, "oct":{}, "nov":{}, "dec":{} }

    def get_monthly(self, m:int=0) -> float:
        """
        Returns: a (float) total
        Get an approximation of what one would have earned this month.
        It is just an approximation and it's also innaccurate, because
        it takes (if any) the first 2 days of the month as special (either as night shifts
        or as holiday shifts)
        """
        total = 0
        nights = self.night_hours
        holyday = self.holy_hours
        subtract = 0
        month = self.get_hours_month(m)
        for i in range(len(month)):
            hours = float(month[i])
            #account for unpaid breaks
            if hours >= 10:
                hours -= 1
            elif hours >= 6:
                hours -= 0.5
            #account for special hours (inaccurate)
            if nights > 0:
                total += (nights*self.rate_night)
                hours -= nights
                nights = 0
            elif holyday > 0:
                total += (holyday*self.rate_holiday)
                hours -= holyday
                holyday = 0
            # We don't work negative hours, but we do need to account for the negative hours
            hours += subtract
            if hours >= 0:
                total += (hours*self.rate)
                subtract = 0
            else:
                subtract = hours
        return total

    def get_hours_month(self, m:int=0) -> dict:
        """
        Return the Dictionary with the dates and hours of this month (what's been recorded so far)
        """
        return self.__year[ months[self.actual_month - m] ]

    def set__income(self, income) ->None:
        """
        Try to set a new value (income) to __income. Prompt if __income != 0
        """
        income = float(income)
        if income < 0:
            print("Error: Job cannot make negative income")
        else:
            if self.__income == 0:
                self.__income = income
            elif self.__income != income:
                decide = input('''__income already has a value of %s, do you want to replace it
                with the new value of %s? [y/n]''' %(self.__income, income) ).lower()
                if decide.startswith('y'):
                    self.__income = income

    def get_income(self) ->float:
        """
        Get the actual income of this month
        """
        return self.__income

    def get_balance(self) -> float:
        """
        Return the expected income minus the actual income (of this month)
        """
        return self.get_monthly() - self.__income

    def add_workday(self, date='DD-MM-YYYY', hours=0.0) ->None:
        """
        Add another work day (and hours) to __month
        """
        m = self.get_hours_month()
        m[date] = float(hours)
    
    def set_holyPay(self, rate):
        """
        Set a value for rate_holiday
        """
        self.rate_holiday = float(rate)

    def add_holyday(self, hours):
        """
        Add hours to the actual holy_hours
        """
        self.holy_hours += float(hours)

    def add_night(self, hours):
        """
        Add hours to the actual night_hours
        """
        self.night_hours += float(hours)

    def set_nightPay(self, rate):
        """
        Set a value for rate_night
        """
        self.rate_night = rate
    
    def reset_month(self):
        """
        Reset the actual __month, holy_hours, night_hours and __income
        """
        self.holy_hours = 0
        self.night_hours = 0
        self.__income = 0

    def start_new_month(self):
        """
        Reset the values of the monthly figures and advance a month
        """
        self.advance_month()
        self.reset_month()

