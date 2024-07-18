products= input("Введите товары через запятую:")
products_1= products.split()
position_1= int(input("Первая позиция для удаления товара:"))-1
position_2= int(input("Вторая позиция для удаления товара:"))-1
products_1[position_1],products_1[position_2] = products_1[position_2],products_1[position_1]
print('Товары на полке:', ', '.join(products_1))