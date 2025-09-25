from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = Order(alice, latte, 4.5)
order2 = Order(alice, espresso, 3.0)
order3 = Order(bob, latte, 4.0)

# Access properties
print(order1.customer)  # Customer(Alice)
print(order1.coffee)    # Coffee(Latte)
print(order1.price)     # 4.5

# Access all orders
print(Order.all())
