#   Construct a dictionary containing four product names and their prices. Prompt the user to enter a product name. Use the in keyword to check if it exists; if so, display its price. Otherwise, inform the user "Product not found.
def product_price(dct, product):
    if product in dct:
        return dct[product]
    else:
        return 'product not found'

products = {'mini bag': 150, 'key chain': 62, 'hair clip': 230, 'crochet rose bouquet': 1726}
print(product_price(products, 'crochet rose bouquet'))
print(product_price(products, 'mobile'))