import Job

MIN_WAGE : float = 8.84

class Worker(object):
    """
    The representation of a Person with
    a job, hobbies and needs, and with a

    """
    def __init__(self,name:str="A Person"):
        """
        The public vars are what everyone can see about this worker
        """
        self.name = name
        self.set_job()
        """
        The rest is personal stuff, that noone else should be able to access
        """
        # Basic things that everyone could have
        self.expenses:dict = { 'rent':233.0, 'food':80.0,
        'gym':23.22, 'rundfunk':17.98, 'insurance':89.90,
        'petrol':0.0, 'phone':7.99}
        self.earnings:dict = {'donating':120.0, 'kindergeld':0.0, 'wohngeld':80.0,
        'bafoeg':0.0, 'scholarship':0.0 }
    
    def set_job(self,name='A Job',rate=MIN_WAGE):
        """
        Give a Job to Worker.
        """
        self.job = Job.Job(name,rate)
    
    def add_earnings(self, items:dict):
        """
        Adds a list(dictionary) of earnings to self.earnings
        """
        self.earnings.update(items)
    
    def add_expenses(self, items:dict):
        """
        Adds a list(dictionary) of expenses to self.expenses
        """
        self.expenses.update(items)
    
    def get_hours_month(self) -> dict:
        """
        Get the Dictionary with the dates and hours that have been worked so far
        """
        return self.job.get_hours_month()

    def get_income(self) -> float:
        """
        Get the actual income from this month
        """
        return self.job.get_income()

    def set_income(self, income) ->None:
        """
        Set the value of this month's income
        """
        self.job.set__income(income)

    def get_balance(self) ->float:
        """
        Returns the difference between expected income and actual income (of this month)
        """
        return self.job.get_balance()
    
    def ideal_mini_hours(self) -> float:
        """
        Returns hours the ideal amount of hours for a 450€ Month 
        """
        return self.ideal_hours(450.0)
    
    def ideal_hours(self, wanted) ->float:
        """
        Returns an ideal amount of hours for a given income(per month)
        """
        return float(wanted)/self.job.rate

    def expected_moneys(self, hours:float) ->float:
        """
        Give a quick expected amount of money for a worked
        amount of hours
        """
        return self.job.rate * hours

    def get_monthly_expected(self) -> float:
        """
        Returns the expected income for this month
        """
        return self.job.get_monthly()

    def add_night(self, hours:float):
        """
        Add hours to the nights worked
        """
        self.job.add_night(hours)
    
    def add_holiday(self, hours:float):
        """
        Add hours to the nights worked
        """
        self.job.add_holyday(hours)
    
    def add_workday(self, date='DD/MM/YYYY', hours=0.0):
        """
        Add a workday to this month
        """
        self.job.add_workday(date, hours)

    def set_holyPay(self, rate:float):
        """
        Set the rate at which this Worker gets paid on holidays
        """
        self.job.set_holyPay(rate)

    def set_nightPay(self, rate:float):
        """
        Set the rate at which this Worker gets paid on nights
        """
        self.job.set_nightPay(rate)

    def reset_month(self):
        """
        Reset the values for the month in the Worker's Job
        """
        self.job.reset_month()

    def set_act_month(self, m:str="jan") ->None:
        """
        Set the actual month for the Job
        """
        self.job.set_act_month(m)
    
    def restart_year(self) ->None:
        """
        Restart the actual year to empty values
        """
        self.job.restart_year()

    def start_new_month(self) ->None:
        """
        Advance the actual month by 1 and reset all monthly values
        """
        self.job.start_new_month()

