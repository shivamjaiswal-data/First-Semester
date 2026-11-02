orders = [
{
'id': 101,
'customer': 'Asha',
'status': 'DELIVERED',
'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]
},
{
'id': 102,
'customer': 'Ravi',
'status': 'CANCELLED',
'items': [('monitor', 1, 10999.0)]
},
{
'id': 103,
'customer': 'Asha',
'status': 'DELIVERED',
'items': [('cable', 5, 199.0)]
},
{
'id': 104,
'customer': 'Meera',
'status': 'SHIPPED',
'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]
},
{
'id': 105,
'customer': 'Ravi',
'status': 'DELIVERED',
'items': [('mouse', 3, 599.0)]
}
]



def E_commerse(orders):
    revenue = {}
    for order in orders :
        if order["status"]== "CANCELLED":
            continue
        customer = order["customer"]
        for item in order["items"]:
            quantity = item[1]
            price = item[2]
            amount =quantity*price
            revenue[customer] = revenue.get(customer,0)+amount
    return revenue

print(E_commerse(orders))
