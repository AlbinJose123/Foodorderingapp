a = {
        1000: 
            {'name': 'Helo', 'quantity': '10', 'price': '120', 'discount': '12', 'stock': '2'},
        1001:
            {'name': 'Hj', 'quantity': 'sdf', 'price': '100', 'discount': '10', 'stock': '2'}
    }
# Food ID: 1000
# Name: Name
# Quantity: 
# Price: 
# Discount: 
# Discounted Price:
# Stock: 

for key, value in a.items():
    print('Food ID', key)
    discounted_price = (1-(int(a[key]['discount']))/100)*int(a[key]['price'])
    for field_name, filed_value in value.items():
        print(field_name.capitalize(), filed_value)
    print('Discounted Price: Rs', discounted_price)
    print('\n')