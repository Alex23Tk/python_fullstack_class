s:str= input("Введите цены:")
products_1= s.split()
print('Цены без скидки:', ' '.join(products_1[1:10:2]))