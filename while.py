#mrs jide account balance in gtb is 10k a bank as balanceto be adding
#  1000 to accout this action should continue while her is less
#  than 50k

def jide():
    b=50000
    while b<80000:
        b=b+10000
        print(b)

jide() 

#mr phillip has alot of money 200k in his account, a boy needs help
#mr phillip has intructed his account officer to be dictuting 5k from his acount
#this action should continue while his balance is less than 150
def phillip():
    b=200000
    while b>150000:
        b=b-5000
        print(b)

phillip() 

#Mr jide account balance is 100, the bank management 
#has decided to multiply his money by 2 while his account balance 
# is < 10000.Write a python function code that will show 
#the transaction details


def john():
    b=150
    while b<10000:
        b=(b*5)+1000
        print(b)
john()