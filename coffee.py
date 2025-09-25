

class Coffee:
    def __init__(self, name: str):
        """
        Initialize a Coffee with a validated name.
        Name must be a string with at least 3 characters.
        Once set, the name is immutable (cannot be changed).
        """
        self._name = None   # backing attribute
        self.name = name    # goes through the setter

    # ---- Property (immutable after first assignment) ----
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if self._name is not None:  # prevent re-assignment
            raise AttributeError("Coffee name cannot be changed after creation.")
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    # ---- Relationship methods ----
    def orders(self):
        """Return all orders for this coffee."""
        from order import Order
        return [order for order in Order.all() if order.coffee == self]

    def customers(self):
        """Return a unique list of customers who bought this coffee."""
        return list({order.customer for order in self.orders()})

    # ---- Aggregate methods ----
    def num_orders(self) -> int:
        """Return the total number of orders for this coffee."""
        return len(self.orders())

    def average_price(self) -> float:
        """Return the average price paid for this coffee across all orders."""
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)

    # ---- Representation ----
    def __repr__(self):
        return f"Coffee({self.name})"
