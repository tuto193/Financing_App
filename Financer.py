import Worker
import pickle
from pathlib import Path

MIN_WAGE: float = 8.84
"""
This financing program is meant to be run manually every monday to keep track of earnings
and make sure that the hours are being paid accordingly
"""
def exists( fileName:str ) -> bool:
    """
    Check whether the given fileName exists
    """
    fname = fileName + ".pkl"
    my_file = Path(fname)
    return my_file.exists()

def get_worker_from_file( fileName:str ) -> Worker.Worker:
    """
    Returns a Worker Object
    from the given fileName
    """
    if not exists(fileName):
        print("The FileName given does not exist")
        return None
    with open( fileName+".pkl", "rb") as file:
        return pickle.load(file)

def write_worker_to_file( worker:Worker.Worker ):
    """
    Write a Worker Object to a file with a Name.txt
    """
    name = fill_spaces(worker.name)
    if exists(name):
        with open(name + ".pkl", "wb") as file:
            pickle.dump(worker, file, pickle.HIGHEST_PROTOCOL)
    else:
        with open(name+".pkl", "xb") as file:
            pickle.dump(worker, file, pickle.HIGHEST_PROTOCOL )

def assign_job( worker: Worker.Worker(), jobDesc:list ):
    """
    Set the Job of a worker to the description provided 
    in a jobDesc. If no second element was provided, give
    the worker a Minimum Wage job, with the given name
    """
    length = len(jobDesc)
    if length == 2:
        worker.set_job(jobDesc[0], float(jobDesc[1]))
    elif length == 1:
        worker.set_job(jobDesc[0], MIN_WAGE)
    else:
        print("Error: the given description was too long/short")

def print_hours_pretty( worker: Worker.Worker, m:int=0 ):
    """
    Show a table with the dates and hours worked by the worked
    """
    month:dict = worker.get_hours_month(m)
    print("+========+========+")
    print("|{Date:8>}|{Hours:8>}|".format(Date='DATE',Hours="HOURS"))
    print("+--------+--------+")
    for key in month:
        print('|{key:8>}|{hours:8>}|'.format(key=key,hours=month[key]))
        print("+--------+--------+")
    print()

def longest_in_list( l:list ) ->str:
    """
    Returns the longest item's string inside a list
    """
    longest :str = ''
    for i in range( len(l) ):
        if len( str(l[i]) ) > len(longest):
            longest = l[i]
    return longest

def longest_in_dict( d:dict ) -> str:
    """
    Returns longest item's string insde a dict
    """
    longest:str = ''
    for i in d:
        if len(str(i)) > len(longest):
            longest=i
    return longest

def print_dict_pretty( d:dict, titleL='Date',titleR='Hours' ) -> None:
    """
    Show a table with a top left title and a top right title, and the contents of a dict underneath them
    """
    #Padding: Make sure that it looks nice
    #p:int = len(longest_in_dict(d)) + 4
    print('+'+ '='*15 +'|' + '='*15 + '+')
    print('|{left:<15}|{right:<15}|'.format(left=titleL,right=titleR) )
    print('+'+ '-'*15 +'+' +'-'*15 +'+')
    for k in d:
        print('|{l:<15}|{r:<15}|'.format(l=k,r=d[k]) )
        print('+'+ '-'*15 +'+' +'-'*15 +'+')
    print()

def list_to_dict(l:list) -> dict:
    """
    Returns a (dict) d from an l list
    The list must have an even number of elements.
    For it to work, the elements should be Sorted as:
    Uneven: keys
    Even: values
    """
    if len(l) <= 1:
        print('''Error: the list give is too short''')
    elif len(l)%2 != 0:
        print("Error: the list used does not have an even number of elements")
    else:
        d :dict = {}
        for key in range(0,len(l),2):
            d[l[key]] = float(l[key+1])
        
        return d

def merge_lists( l1:list, l2:list ) ->dict:
    """
    Returns a dictionary
    It is made out of a l1 with keys and a l2 with values
    """
    if len(l1)==0 or len(l2)==0:
        print("Error: none of the give lists can be empty")
    elif len(l1) != len(l2):
        print("Error: both lists must have the same size")
    else:
        d :dict = {}
        for i in range( len(l1) ):
            d[ l1[i] ] = float(l2[i]) 
        return d

def fill_spaces( s:str ) ->str:
    """
    Returns a (str) name
    Takes a (str)name
    """
    newS: list = s.split(' ')
    if len(newS) == 1:
        return s
    else:
        s2:str = newS[0]
        for i in range(1,len(newS)-1):
            s2 += "_" + newS[i]
        return s2

def recover_spaces( s:str ) -> str:
    """
    Replace all underscores ('_') in a string with spaces
    """
    s2 :str= '' 
    for letter in s:
        if letter != '_':
            s2 += letter
        else:
            s2 += ' '
    return s2

def show_instructions() ->None:
    """
    Show the instructions, so all data can be read
    safely and without errors
    """
    print('''
    To answer yes or no questions [y/n], just write 
    "y" or "n" and then press the [ENTER] key.

    To answer questions where a word/number is needed, just write the whole thing out WITHOUT spaces and
    press then the [ENTER] key. 
    Example: aVeryLongName 69.69

    If you are asked questions where you need to answer
    with a word and then a number, write them in pairs,
    but still all separated just by spaces. 
    Example (When answering about my costs):
        gym 19.90 gas 50.0 food 80.0 rundfunk 16.50

    If you made any mistakes, you can delete what you wrote.

    More particular instructions will be asked along the
    way, if needed.''')
    print()

def yes_or_no() ->bool:
    decision:str = input('Yes or no?[y/n]').lower()
    if decision.startswith('y'):
        return True
    return False

def prompt_new_job( w:Worker.Worker) ->None:
    """
    Prompt and assign a new job to a Worker
    """
    job = input('''
        [Enter the name of the place where you work at,
        and how much you earn per hour](Should you not
        specify your pay, it will be assumed that you 
        are working a minimum wage job)
        ''').split()
    assign_job(workingPerson, job)
    
    print('''Do you get special pay at night or on
    holidays?''')
    #Check whether he has special pay
    special_pay = yes_or_no()
    w.job.special_pay = special_pay
    if special_pay:
        s_rates = input('''How much do you earn at nights
        and on holidays(in that order)?
        [Put a 0 for the one that doesn't apply, if any]''').split()
        w.job.rate_night = float(s_rates[0])
        w.job.shift_night:bool = (w.job.rate_night!=0)
        w.job.rate_holiday = float(s_rates[1])
        w.job.shift_holy:bool = (w.job.rate_holiday!=0)
    print()
    prompt_act_month(w)

def prompt_act_month( w:Worker.Worker ) ->None:
    """
    Set the actual month the worker is starting on
    """
    m:str = input('''What month is it?[jan, feb, apr, etc...]''')
    w.set_act_month(m)
    print()

def prompt_new_month( w:Worker.Worker ) ->None:
    """
    Prompt the worker if he wants to begin a new month
    """
    #Decide whether to do it or not
    d:bool = False
    print('''Do you want to start a NEW month?''')
    d = yes_or_no()
    if d:
        old_m:dict = w.get_hours_month()
        if not old_m:
            print('''Do you want to see how your this last month looked like?''')
            e:bool = yes_or_no()
            if e:
                prompt_month_pretty(w)
        #Start a new month no matter the previous outcome
        w.start_new_month()
    print()

def prompt_month_pretty( w:Worker.Worker ) ->None:
    """
    Print an overview of this month
    """
    print('''Do you want to see your current month?''')
    d:bool = yes_or_no()
    if d:
        #Hours worked
        print('These are your hours worked:')
        print_dict_pretty(w.get_hours_month())
        #Income, Expected and Balance
        exp:float = w.get_monthly_expected()
        plus:float = add_values_dict(w.earnings)
        minus:float = add_values_dict(w.expenses)
        bal:float = exp+plus-minus
        print()
        print('''
        You Expect to earn:         +{expected:>10}€
        Plus your other earnings:   +{plus:>10}€
        Minus your expenses:        -{minus:>10}
        That makes it a balance of : {balance:>10}€'''.format(expected=exp,plus=plus,minus=minus,balance=bal)
        )
    print()

def modify_earnings( w:Worker.Worker ) ->None:
    """
    Prompt the user and modify recursively his earnings
    """
    read:list = input("Enter the values to replace/add here:").lower().split()
    rdict = list_to_dict(read)
    w.add_earnings(rdict)
    print("Do you want to modify something else?")
    d = yes_or_no()
    if d:
        modify_earnings(w)

def prompt_earnings( w:Worker.Worker ) ->None:
    """
    Prompt the worker about his earnings. 
    Give examples beforehand. Show his actual earnings already
    """
    print('''These are your actual Earnings:''')
    print_dict_pretty(w.earnings, "Source", "Amount")
    print('''Do you want to add/modify something?''')
    d = yes_or_no()
    if d:
        modify_earnings(w)
    print_dict_pretty(w.earnings, "Source", "Amount")

def modify_expenses( w:Worker.Worker ) ->None:
    """
    Prompt the user and modify recursively his expenses
    """
    read:list = input("Enter the values to replace/add here:").lower().split()
    rdict = list_to_dict(read)
    w.add_expenses(rdict)
    print("Do you want to modify something else?")
    d = yes_or_no()
    if d:
        modify_expenses(w)

def prompt_expenses( w:Worker.Worker ) ->None:
    """
    Prompt the worker about his expenses. 
    Give examples beforehand. Show his actual earnings already
    """
    print('''These are your actual Expenses:''')
    print_dict_pretty(w.expenses, "Expense", "Amount")
    print('''Do you want to add/modify something?''')
    d = yes_or_no()
    if d:
        modify_expenses(w)
    print_dict_pretty(w.expenses, "Expense", "Amount")

def add_values_dict( d:dict ) ->float:
    """
    Returns a float.
    Add all the values inside a dict.
    """
    total:float = 0.0
    for k in d:
        total += d[k]
    return total

def see_overall_balance( w:Worker.Worker ) ->None:
    """
    Show the worker a calculation of his livelihood and
    give recommendations accordingly
    """
    plus:float = add_values_dict(w.earnings)
    minus:float = add_values_dict(w.expenses)
    income:float = w.get_income()
    worked:float = w.ideal_hours(income)
    bal:float = w.get_balance()
    exp:float = w.get_monthly_expected()
    exph:float = w.ideal_hours(exp)
    final_b:float = income + plus - minus
    final_hours:float = w.ideal_hours(-final_b)
    print('''
    Your income is:+{income:>10}€
    Your earnings: +{earnings:>10}€
    Your expenses: -{expenses:>10}€
    Your balance is:{fbalance:>10}€
    Which means you need(ed) to work another...
                    {final_hours:>10}h
    
    According to your pay, you worked: {workedh:>10}h
    You expected to earn:              {exp:>10}€
    Which are these hours:             {exph:>10}h
    You balance says then:             {bal:>10}'''.format(
        income=income,earnings=plus,expenses=minus,
        workedh=worked,exp=exp,exph=exph,bal=bal,
        fbalance=final_b,final_hours=final_hours
    ))
    print()
        
def prompt_new_day( w:Worker.Worker ) ->None:
    """
    Ask the worker if he wants to add a new day to his month
    """
    print('''Do you want to add a NEW (worked) day to your MONTH(%s)?''' %( w.job.get_curr_month() ) )

    d:bool = yes_or_no()
    if d:
        day = input("Enter the date and amount of hours: [DD-MM-YYYY hh]").split()
        hours:float = float(day[1])
        date:str = day[0]
        w.job.add_workday(date,hours)
        if w.job.special_pay():
            hourN = float(input("How many hours at night?"))
            hourH = float( input( "How many hours on a holiday?" ) )
            w.job.add_night(hourN)
            w.job.add_holyday(hourH)

if __name__ == "__main__":
    new_month:bool = False
    entered_income:bool = False
    print("Welcome to your Financing App!")
    inputName :str = input('''What's your name?''')
    workerName:str = fill_spaces(inputName)
    workingPerson = None
    e:bool = exists( workerName )
    if e:
        print('''Welcome back %s! It's nice to see you again.''' %inputName)

        workingPerson = get_worker_from_file(workerName)
        print('''Are you still working at %s?''' %(workingPerson.job.name) )
        more = yes_or_no()
        if not more:
            prompt_new_job( workingPerson)
            new_month = True
    else:
        print("Nice to meet you, %s. I will manage your finances" %inputName)
        print('''
        Since it's your first time here, we'll show you
         the instructions!
         Then, we'll need some infos about you.
         ''')
        
        show_instructions()

        workingPerson = Worker.Worker(workerName)

        prompt_new_job(workingPerson)
        
    while True:
        inc:float = workingPerson.get_income

        #See current month before starting
        prompt_month_pretty(workingPerson)
        #Add another day to the month?
        prompt_new_day(workingPerson)
        #Start a new Month?
        prompt_new_month(workingPerson)
        #Show the current month?

        #Show income
        if not inc:
            print("You got %s€ this month")
        elif not entered_income:
            print("Did you get paid this month already?")
            d:bool = yes_or_no()
            if d:
                i = input("How much?")
                workingPerson.set_income(i)
            entered_income = True
        
        #Show earnings
        prompt_earnings(workingPerson)
        #Show costs
        prompt_expenses(workingPerson)
        #Calculate a balance based on income + earnings - expenses
        print('''Do you want to see your balance?''')
        see_balance:bool = yes_or_no()
        if see_balance:
            see_overall_balance(workingPerson)
        #promt review of program
        print('''Do you want to save and exit?''')
        end:bool = yes_or_no()
        if end:
            print("See you later!...")
            write_worker_to_file(workingPerson)
            break
        #Save the File (worker again) if ending
        #Say Goodbye
        

#Add statistics in the future, based on calculations of other months