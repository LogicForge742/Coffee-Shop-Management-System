# Defining the Coffee class
class Coffee:
    """
    Represents a coffee in the coffee shop system.
    
    Rules:
      - Coffee must have a name (string, at least 3 characters).
      - Once set, the name cannot be changed (immutable).
    """

    def __init__(self, name: str):
        """
        Initialize a Coffee with a validated name.
        
        Args:
            name (str): The name of the coffee.
        """
        self._name = None   # backing attribute to enforce immutability
        self.name = name    # validation goes through setter

    # ---- Property (immutable after first assignment) ----
    @property
    def name(self) -> str:
        """Getter: Return the coffee's name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """
        Setter: Validate and set the coffee's name.
        Rules:
          - Name can only be set once (immutable).
          - Must be a string of at least 3 characters.
        """
        if self._name is not None:
            raise AttributeError("Coffee name cannot be changed after creation.")
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    # ---- Relationship methods ----
    def orders(self):
        """
        Return all orders placed for this coffee.
        Looks through Order.all() and filters by self.
        """
        from order import Order
        return [order for order in Order.all() if order.coffee == self]

    def customers(self):
        """
        Return a unique list of customers who purchased this coffee.
        Uses a set to avoid duplicates.
        """
        return list({order.customer for order in self.orders()})

    # ---- Aggregate methods ----
    def num_orders(self) -> int:
        """Return the total number of orders for this coffee."""
        return len(self.orders())

    def average_price(self) -> float:
        """
        Return the average price paid for this coffee across all orders.
        Returns 0.0 if there are no orders.
        """
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)

    # ---- Representation ----
    def __repr__(self):
        """Readable string representation of the Coffee object."""
        return f"Coffee({self.name})"

