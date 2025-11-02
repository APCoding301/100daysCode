# print(f"6.00 is greater than or equal to 5.00 {6.00 >= 5.00}")
# print(f"-6.00 is lesser than or equal to -5.00 {-6.00 <= -5.00}")

yday = 97.75
day_before = 105.00

percent_change = ((yday - day_before)/day_before) * 100

if (percent_change >= 5.00) or (percent_change <= -5.00):
    print("Get NEWS!!")
else:
    print('No NEWS to get, less than plus/minus 5.00 percent!')