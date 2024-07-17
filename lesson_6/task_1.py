s:str= input("Введите товары через запятую:")
products_1= s.split()
print('Товары с нечетными индексами:', ' '.join(products_1[1:10:2]))