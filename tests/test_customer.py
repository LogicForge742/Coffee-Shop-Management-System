import sys
import types
import unittest
from unittest import mock

# Ensure the 'coffee' module exists before importing Customer
if 'coffee' not in sys.modules:
    coffee_module = types.ModuleType('coffee')
    class Coffee:
        pass
    coffee_module.Coffee = Coffee
    sys.modules['coffee'] = coffee_module

from customer import Customer


class TestCustomer(unittest.TestCase):
    def test_initialization_sets_valid_name_via_setter(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_create_order_links_customer_coffee_and_price(self):
        c = Customer("Jane")
        coffee_obj = object()
        price = 3.5

        order_module = types.ModuleType('order')
        order_mock = mock.MagicMock(name='Order')
        expected_order_instance = object()
        order_mock.return_value = expected_order_instance
        order_module.Order = order_mock

        with mock.patch.dict(sys.modules, {'order': order_module}):
            result = c.create_order(coffee_obj, price)

        order_mock.assert_called_once_with(c, coffee_obj, price)
        self.assertIs(result, expected_order_instance)

    def test_coffees_returns_unique_purchased_coffees(self):
        c1 = Customer("Amy")
        c2 = Customer("Bob")

        coffee1 = object()
        coffee2 = object()

        order1 = types.SimpleNamespace(customer=c1, coffee=coffee1)
        order2 = types.SimpleNamespace(customer=c1, coffee=coffee1)  # duplicate coffee
        order3 = types.SimpleNamespace(customer=c1, coffee=coffee2)
        order4 = types.SimpleNamespace(customer=c2, coffee=coffee2)  # other customer's order

        order_module = types.ModuleType('order')
        order_mock = mock.MagicMock(name='Order')
        order_mock.all.return_value = [order1, order2, order3, order4]
        order_module.Order = order_mock

        with mock.patch.dict(sys.modules, {'order': order_module}):
            coffees = c1.coffees()

        self.assertEqual(set(coffees), {coffee1, coffee2})
        self.assertEqual(len(coffees), 2)

    def test_init_with_invalid_name_leaves_default_empty(self):
        c = Customer(None)
        self.assertEqual(c.name, "")

    def test_setter_rejects_out_of_bounds_name_retains_previous(self):
        c = Customer("ValidName")
        c.name = ""  # too short
        self.assertEqual(c.name, "ValidName")
        c.name = "x" * 16  # too long
        self.assertEqual(c.name, "ValidName")
        # valid change still works
        c.name = "NewName"
        self.assertEqual(c.name, "NewName")

    def test_orders_filters_by_customer_and_handles_no_orders(self):
        c1 = Customer("Carl")
        c2 = Customer("Dana")

        order_a = types.SimpleNamespace(customer=c1, coffee=object())
        order_b = types.SimpleNamespace(customer=c1, coffee=object())
        order_c = types.SimpleNamespace(customer=c2, coffee=object())

        # Case 1: Filters only this customer's orders
        order_module = types.ModuleType('order')
        order_mock = mock.MagicMock(name='Order')
        order_mock.all.return_value = [order_a, order_b, order_c]
        order_module.Order = order_mock

        with mock.patch.dict(sys.modules, {'order': order_module}):
            c1_orders = c1.orders()

        self.assertEqual(c1_orders, [order_a, order_b])

        # Case 2: No orders exist
        order_module_empty = types.ModuleType('order')
        order_mock_empty = mock.MagicMock(name='Order')
        order_mock_empty.all.return_value = []
        order_module_empty.Order = order_mock_empty

        with mock.patch.dict(sys.modules, {'order': order_module_empty}):
            c3 = Customer("Eli")
            self.assertEqual(c3.orders(), [])


if __name__ == '__main__':
    unittest.main()