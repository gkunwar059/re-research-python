import datetime

# current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# current date
today = datetime.date.today()
print("Today's date:", today)


# specific date  formatter the date
specific_date = datetime.date(2020, 2, 22)
print(specific_date)


# specific time formatter

time_specific = datetime.time(1, 22, 30)
print(time_specific)


# creating datetime object is :
obj_datetime = datetime.datetime(2020, 3, 12, 1, 30, 34)
print("set_yourself", obj_datetime)



#-----------------------IMPORTANT DATETIME SETUP -------------------------
'''
YO FORMATTER CHAI HAMLE SCHEMAS HARU MA LAGAUANXAU , YO CASE MA CHAI FORMATTING GARNU PARXA VANERA 
CHAI HAMLE SET GARNE GARXCAU TESKO LAGHI CHAI OVERALL YO CHIA BEST HUNXA , YO FORMAT MA YO DATA SET GARNE VANERA CHAI HAMLE GARNU PARNE HUNXA 

'''

# Formatting Dates and Times

# formatting date and time 

''''
HOW IT IS FORMATTED LETS SEE :
'''

'''
%Y,
%m
%d
%H
%S


'''

now=datetime.datetime.now()
print(type(now))

format_now=now.strftime("%d%M%Y%H%M%s")   #afno hisab le set garna milne rahexa yeha chai 
print(type(format_now))
'''
'''




date_string = "2022-12-25 12:30:45"
date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(type(date_object))  # Example: 2022-12-25 12:30:45



'''

use the time delta 
'''

delta_time=datetime.timedelta(5)

noew_date=datetime.datetime.now()

c=delta_time+noew_date

print("final-time",c)


comp_time1=datetime.datetime.now()
print("utc-1",comp_time1)

comp_time2=datetime.datetime.now(datetime.timezone.utc)
print("utc-2",comp_time2)
