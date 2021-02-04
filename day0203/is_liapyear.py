def is_leapyear(year):
    if year%400==0 or(year%4==0 and year%100 != 0):
        return True
    else:
        return False

year=int(input('西暦>>'))

if is_leapyear(year):
    print('西暦{}年は、うるう年です'.format(year))
else:
    print('西暦{}年は、うるう年ではありません'.format(year))
