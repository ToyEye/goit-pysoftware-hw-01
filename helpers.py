import datetime 

def get_upcoming_birthdays(user=None):
    
    
    tdate=datetime.datetime.today().date()# беремо сьогоднішню дату   
    
    bdate=user["birthday"] 
    
    
    bdate=bdate[:6] + str(tdate.year) # Замінюємо рік на поточний
    
    
    bdate=datetime.datetime.strptime(bdate, "%d.%m.%Y").date() # перетворюємо дату народження в об’єкт date
    week_day=bdate.isoweekday() # Отримуємо день тижня (1-7)
    days_between=(bdate-tdate).days 
    
    if 0<=days_between<7:
        if(week_day<6):
            return f'{user["name"]}s congratulation date {bdate.strftime("%d.%m.%Y")}' # Додаємо вітання у список, якщо списко випадає на робочі дні
        else:
            if(bdate+datetime.timedelta(days=1)).weekday()==0:
               return f"{user['name']}s congratulation date {(bdate+datetime.timedelta(days=1)).strftime("%d.%m.%Y")}"# Додаємо вітання у список, якщо списко випадає на неділю 
            elif(bdate+datetime.timedelta(days=2)).weekday()==0:
               return f"{user['name']}s congratulation date {(bdate+datetime.timedelta(days=2)).strftime('%d.%m.%Y')}" # Додаємо вітання у список, якщо списко випадає на суботу            
       

    