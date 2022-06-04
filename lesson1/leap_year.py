#O(1) program doing sam all the time no for and while loops. it ir constant time.

year = int(input('Input a year to check: '))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print(f'{year} is a leap year')
        else:
            print(f'{year} is Not a leap year')
else:
    print(f'{year} is Not a leap year')


