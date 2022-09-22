# pay_rate = input("What is your pay rate per hour? ");
# #assuming a work week is 40 hours 
# hours_worked = input("How many hours have you worked this pay period (Biweekly)? ");
# overtime_biweek = (int(hours_worked) - 80);
# overtime = int(pay_rate) * 1.5 * (overtime_biweek);
# #assuming tax is 20%
# gross_income = (pay_rate*80) + 
# gross_income = int(pay_rate*overtime_biweek) + int(float(overtime));
# taxed = int(gross_income) * 0.8;
# print(f"Your paycheck this pay period is ${taxed}.")
# print(pay_rate, hours_worked, overtime_biweek, overtime, gross_income, taxed)



pay_rate = input("What is your pay rate per hour? ");
hours_worked = input("How many hours have you worked this pay period (Biweekly)? ");
if (int(hours_worked) - 80) > 0:
    overtime_hours = int(hours_worked) - 80
else: overtime_hours = 0
tax = 0.80
if (int(hours_worked) < 80):
    underworked = True;
else: underworked = False;

if underworked == True:
    taxed = int(hours_worked) * int(pay_rate) * tax
    print(f"your paycheck this pay period is ${taxed}")
else: 
    taxed = tax*(float(int(pay_rate)*80) + ((overtime_hours)*float(pay_rate)*1.5))
    # print(float(int(pay_rate)*80))
    # print(((overtime_hours)*float(pay_rate)*1.5))
    print(f"your paycheck this pay period is ${taxed}")    