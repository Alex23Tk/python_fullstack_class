s:str= input("Введите цены:")
products_1= s.split()
print('Новые цены:', ' '.join(products_1[-1:-10:-1]))