products= input("Введите товары через запятую:")
products_1= products.split()
position_1= int(input("Позиция для удаления товара:"))-1
products_1.pop(position_1)
print('Товары на полке:', ', '.join(products_1))