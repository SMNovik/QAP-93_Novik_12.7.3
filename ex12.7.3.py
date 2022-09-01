import numpy as np
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Сумма депозита ="))
deposit = [money * per_cent.get('ТКБ')/100, money * per_cent.get('СКБ')/100, money * per_cent.get('ВТБ')/100, money * per_cent.get('СБЕР')/100]
deposit = list(np.around(deposit, decimals=2))
print('deposit=', deposit)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))