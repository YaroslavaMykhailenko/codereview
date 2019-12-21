'''
Перше січня першого року ношої ери було понеділком за сучасним грегоріанським календарем.
Користувач вводить дату у форматі "31-12-0001".Потрібно написати функцію,що повертає день тижня,на який припадає ця дата.
'''
import re
string_data = re.findall(r'[0-9]{2}-[0-9]{2}-[0-9]{4}',input('Enter the date/month/year:'))
print(string_data)
week = ["Понеділок","Вівторок","Середа","Четвер","П'ятниця","Субота","Неділя"]
for element in string_data:
    # print(element[3:5])
    # if element[0:2]==1:
        print(element)
def DateOftheWeek(week):
    for day in week:
        print(day)


DateOftheWeek(string_data)
DateOftheWeek(week)
