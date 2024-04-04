def get_fixed_price(discount_rate, discounted_price):
    fixed_price = discounted_price / (1 - discount_rate/100)
    return fixed_price

discount_rate = float(input('할인율은? '))
discounted_price_A = float(input('A 상품의 할인된 가격은? '))
discounted_price_B = float(input('B 상품의 할인된 가격은? '))

price_A = get_fixed_price(discount_rate, discounted_price_A)
price_B = get_fixed_price(discount_rate, discounted_price_B)

print('A 상품의 정가는', {price_A},'원')
print('B 상품의 정가는', {price_B},'원')
