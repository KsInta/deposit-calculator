contribution = input('Введите размер вклада')

money = int(contribution)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit_list = list(per_cent.values())
deposit = list(map(lambda x: int(x * money / 100), deposit_list))

print('Размер вашего вклада - ' + contribution, '\n')
print('Накопленные средства за год вклада в каждом банке - ', deposit, '\n')

deposit.sort(reverse=True)

banks = list(per_cent.keys())
bank = banks[list(per_cent.values()).index(deposit_list[0])]

print('Максимальная сумма, которую вы можете заработать - ' + str(deposit[0]) + '. Банк ' + bank)
