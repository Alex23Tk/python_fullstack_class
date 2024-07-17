products= input("Введите товары через запятую:")
products_1= products.split()
position_1= int(input("Позиция для нового товара:"))-1
new_product= input("Наименование товара:")
products_1.insert(position_1, new_product)
print('Новые цены:', ' ,'.join(products_1))