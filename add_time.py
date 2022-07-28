'''
a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive

'''



def add_time(time, time_add, day=None):

    #variables
    
    if day:
        day = day.lower()
        day = day.capitalize()
        day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = day_list.index(day)
    final_string = ""

    #actual time
    hour = int(time.split(":")[0]) 
    min = int(time.split(":")[1].split(" ")[0])
    day_time = time.split(":")[1].split(" ")[1]

    #added time
    hour_add = int(time_add.split(":")[0])
    min_add = int(time_add.split(":")[1])
    


    total_min_day_time = min + min_add
    total_min = min + min_add
    
    
    
    if day_time.upper()=="PM":
        hour += 12
    
    #add time
    total_hour = hour + hour_add
    
    #calculate minutes if more than 59
    if total_min>59:
        total_hour +=1
        total_min -= 60
    
    
    
    #if total_hour>24:
    real_hour = total_hour%24
    # else:
    #     real_hour = total_hour
    
    
    
    #after 12 its pm, after 24 its AM
    if real_hour>12:
        real_hour -=12
        total_day_time = " PM"
    
    elif real_hour > 12 and hour == 24:
        total_day_time = " AM"

    elif hour == 11 and day_time == "AM" and total_min_day_time>59:
        total_day_time = " PM"
        
    else:
        total_day_time = " AM"
        
    
    #count days added
    amount_days_add = round(total_hour//24)

    #string formatter
    if total_min < 10:
        total_min = "0"+str(total_min)

    if real_hour== 0:
        real_hour = 12
    
    


    if day == None:
        if amount_days_add==1:
            final_string = str(real_hour)+ ":" + str(total_min) + total_day_time + ' (next day)'
            return final_string
        elif amount_days_add>1:
            final_string = str(real_hour)+ ":" + str(total_min) + total_day_time + f' ({amount_days_add} days later)'
            return final_string
        else:
            final_string = str(real_hour)+ ":" + str(total_min) + total_day_time
            return final_string
        
        
    elif day:
        day_index += amount_days_add
        day_index = day_index%7

        if amount_days_add==1:
            final_string = str(real_hour)+ ":" + str(total_min) + total_day_time + f', {day_list[day_index]} (next day)'
            return final_string
        if amount_days_add==0:
            final_string = str(real_hour)+ ":" + str(total_min) + total_day_time + f', {day_list[day_index]}'
            return final_string

        else:
            final_string = str(real_hour)+ ":" + str(total_min) + total_day_time + f', {day_list[day_index]} ({amount_days_add} days later)'
            return final_string
    
    
        

    






print(add_time("11:40 AM", "0:25"))
