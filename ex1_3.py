"""
h=int(input('身長(cm)は?>>'))/100
w=int(input('体重(kg)は?>>'))
bmi=w/h/h
print(f'BMIは{bmi:.1f}です')
"""

h,w=int(input('身長(cm)は?>>'))/100,int(input('体重(kg)は?>>'))
print(f'BMIは{w/h**2 : .1f}です')


