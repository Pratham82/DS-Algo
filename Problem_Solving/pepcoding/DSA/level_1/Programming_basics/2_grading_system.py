marks=int(input())

#write your code here
if marks >= 90:
    print('excellent')
elif marks > 80 and marks <= 90:
    print('good')
elif marks > 70 and marks <= 80:
    print('fair')
elif marks > 60 and marks <= 70:
    print('meets expectations')
elif marks <= 60:
    print('below par')