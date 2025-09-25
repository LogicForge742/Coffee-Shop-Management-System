# Defining the Customer class
class Customer:
    def __init__(self, name):
        # Initialize with a backing attribute for validation
        self._name = ""  
        # This calls the setter method for validation
        self.name = name  

    # ---- Property: name ----
    @property
    def name(self):
        """Getter: Return the customer's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Setter: Validate and set the customer's name.
        Rules:
          - Must be a string
          - Length between 1 and 15 characters
        """
        if isinstance(value, str) and (1 <= len(value) <= 15):
            self._name = value

    # ---- Relationship methods ----
    def orders(self):
        """
        Return all orders placed by this customer.
        Looks through Order.all() and filters by self.
        """
        from order import Order
        return [order for order in Order.all() if order.customer == self]
    
    def coffees(self):
        """
        Return a unique list of coffees this customer has purchased.
        Uses a set comprehension to avoid duplicates.
        """
        return list({order.coffee for order in self.orders()})
    
    # ---- Behavioral methods ----
    from coffee import Coffee
    def create_order(self, coffee: Coffee, price: float):
        """
        Create and return a new Order linking this customer 
        to a coffee at a given price.
        """
        from order import Order
        return Order(self, coffee, price)
    
    # ---- Representation ----
    def __repr__(self):
        """Readable string representation of the Customer."""
        return f"Customer({self.name})"

