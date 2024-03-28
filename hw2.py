def get_integer(prompt):
 exchange = int(input(prompt))
 return exchange

money, n500, n100, n50, n10 =0,0,0,0,0
exchange = int(input("동전으로 교환하고자 하는금액은?: "))
money=exchange


n500=money//500
print('500원 동전의 개수: ', n500)
money %= 500
n100=money//100
print('100원 동전의 개수: ', n100)
money %= 100
n50=money//50
print('50원 동전의 개수: ', n50)
money %= 50
n10=money//10
print('10원 동전의 개수: ', n10)
money %= 10
