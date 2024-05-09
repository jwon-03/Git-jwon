shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명?')
    if item == '':
        break
    quantity = int(input('수량?'))
    if item in shopping_bag:
        shopping_bag[item] += quantity
    else:
        shopping_bag[item] = quantity
    print(f'장바구니에{item} {quantity}개가 담겼습니다.\n')

print('\n>>> 장바구니 보기:')
for item, quantity in shopping_bag.items():
    print(f'{item}:{quantity}')
