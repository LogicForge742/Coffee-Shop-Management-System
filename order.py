from coffee import Coffee
from customer import Customer

class Order:
    _all_orders = []  # Class list to keep track of all orders made.

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        """
        Initialize a new order that links a Customer to a Coffee at a given price.

        Args:
            customer (Customer): The customer placing the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the coffee in this order (must be 1.0–10.0).
        """
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")

        self._customer = customer   # private: can't be changed directly
        self._coffee = coffee       # private: can't be changed directly
        self._price = float(price)  # private: immutable after creation

        Order._all_orders.append(self)  # add to class list

    # ---- Properties ----
    @property
    def customer(self) -> Customer:
        """Return the customer who made the order."""
        return self._customer

    @property
    def coffee(self) -> Coffee:
        """Return the coffee associated with this order."""
        return self._coffee

    @property
    def price(self) -> float:
        """Return the price paid for this order."""
        return self._price

    # ---- Class methods ----
    @classmethod
    def all(cls):
        """Return all orders ever created."""
        return cls._all_orders

    # ---- Representation ----
    def __repr__(self):
        return f"Order({self.customer.name} -> {self.coffee.name} @ ${self.price:.2f})"
