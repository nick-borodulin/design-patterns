"""
OCP or Open/Closed Principle states that classes should open for EXTENSION and closed for MODIFICATION.
What that means is that when a new functionality needs to be added, a new subclass should be added instead of
opting to mofify existing code by adding another if-else condition. An interface class and a new child class is the 
way to go.

For example, non-compliant code should look like this:

class PaymentProcessor:
    def process(self, payment_type, amount, details):
        if payment_type == 'credit_card':
            # Process credit card payment logic
            print(f"Processing credit card payment of ${amount}...")
            # ... API calls, validation, etc.
            return {"status": "success", "transaction_id": "cc_12345"}
        elif payment_type == 'paypal':
            # Process PayPal payment logic
            print(f"Processing PayPal payment of ${amount}...")
            # ... PayPal specific API calls, etc.
            return {"status": "success", "transaction_id": "pp_67890"}
        # ... imagine more elif blocks for other payment types ...
        else:
            raise ValueError(f"Unsupported payment type: {payment_type}")

OCP-compliant code is below.

Note: the if-else logic that decideds which type of payment to process needs to be somewhere,
and it needs to be modified when a new payment type is added. It's typically placed into a factory method or a builder.
That doesn't violate OCP.
"""

from abc import ABC, abstractmethod


# Define the common interface (Abstract Base Class)
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount, details) -> dict[str, str]:
        """Process the payment and return a result."""
        ...


# Implementations for different payment types (Extensions)
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount, details) -> dict[str, str]:
        print(f"Processing credit card payment of ${amount}...")
        # ... Credit card specific logic ...
        return {"status": "success", "transaction_id": "cc_abcde"}


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount, details) -> dict[str, str]:
        print(f"Processing PayPal payment of ${amount}...")
        # ... PayPal specific logic ...
        return {"status": "success", "transaction_id": "pp_fghij"}


class BitcoinPayment(PaymentMethod):  # Easy to add new types!
    def process_payment(self, amount, details) -> dict[str, str]:
        print(f"Processing Bitcoin payment of ${amount}...")
        # ... Bitcoin specific logic ...
        return {"status": "success", "transaction_id": "btc_klmno"}


# The processing logic now depends on the abstraction (PaymentMethod)
class OrderProcessorOCP:
    def process_order_payment(
        self, payment_method: PaymentMethod, amount, details
    ) -> dict[str, str]:
        # This method is CLOSED FOR MODIFICATION
        # It doesn't care *what* type of payment method it is,
        # as long as it adheres to the PaymentMethod interface.
        print("Starting general payment processing...")
        result = payment_method.process_payment(amount, details)
        print("General payment processing finished.")
        return result
