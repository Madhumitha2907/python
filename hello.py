# LEAP YEAR
year=int(input())
if year%100==0 and year%400==0:
    print("Leap year ",str(year))
elif year%4==0 and year%100!=0:
    print("Leap Year",str(year)) 
else :
    print("Not a Leap Year",str(year))       