import json

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

products = {}
# Открываем файл и загружаем данные
with open('products.json', 'r') as file:
    products = json.load(file)
    print(products)

daily_products = {}
for product in products:
    dict_product = product
    for key in list(dict_product.keys()):
        if key not in daily_products:
            daily_products[key] = dict_product[key]
        else:
            daily_products[key] = daily_products[key] + dict_product[key]

max_product_sum = max(daily_products.values())
total_sum_daily = sum(daily_products.values())
count_products_daily = len(daily_products)

print("Общая выручка магазина за день", total_sum_daily)
print("Выручка магазина по каждому виду товара: ", {x for x in daily_products.items()})
print("Тип товара, проданный на самую большую сумму: ", get_key(daily_products, max_product_sum))
print("Количество различных видов товаров, проданных за день: ", count_products_daily)
