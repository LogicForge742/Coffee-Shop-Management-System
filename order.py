# Defining the Order class
from coffee import Coffee
from customer import Customer

class Order:
    """
    Represents a single order placed by a customer for a specific coffee.

    Rules:
      - Each order links exactly one Customer to one Coffee.
      - Price must be a number between 1.0 and 10.0 (inclusive).
      - Once created, an order’s customer, coffee, and price cannot be changed.
    """

    # ---- Class-level attribute ----
    _all_orders = []  # stores every Order instance created

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        """
        Create a new Order.

        Args:
            customer (Customer): The customer placing the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the coffee in this order (1.0–10.0).
        """
        # --- Validate price ---
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number.")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")

        # --- Assign private attributes (immutable after creation) ---
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        # --- Track this order in the class list ---
        Order._all_orders.append(self)

    # ---- Properties ----
    @property
    def customer(self) -> Customer:
        """Return the customer who made this order."""
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
        """Return a list of all orders ever created."""
        return cls._all_orders

    # ---- Representation ----
    def __repr__(self):
        """Readable string representation of an Order."""
        return f"Order({self.customer.name} -> {self.coffee.name} @ ${self.price:.2f})"
