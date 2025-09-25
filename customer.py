#defining a class


class Customer:
    def __init__(self, name):
        self._name = "" # backing attribute
        self.name = name # uses the setter function

     #getter function
    @property
    def name(self):
        return self._name
    
    #setter function
    @name.setter
    def name(self , value):
        if isinstance(value ,str) and (1 <= len(value) <= 15 ):
            self._name = value

     # ---- Relationship methods ----
    def orders(self):
        """Return all orders placed by this customer."""
        from order import Order
        return [order for order in Order.all() if order.customer == self]
    
    def coffees(self):
        """Return a unique list of coffees this customer has purchased."""
        return list({order.coffee for order in self.orders()})
    
    #Behavioral method
    from coffee import Coffee
    def create_order(self , coffee:Coffee , price:float):
        # Create a new Order linking this customer to a coffee at a specific price.
        from order import Order
        return Order(self, coffee, price)
    
    # ---- Representation ----
    def __repr__(self):
        return f"Customer({self.name})"
