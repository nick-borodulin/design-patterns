"""
SRP or Single Responsibility Principle states that a class should be doing one thing. 

For example, if an API endpoint validates inputs, saves them to the database, sends email, 
the non-SPR-compliant code would look like this:

class OrderHandler:
    def process_order_request(self, request_data):
        # Responsibility 1: Validate input data
        if not self._validate_data(request_data):
            return {"error": "Invalid data"}, 400 # Return error response

        # Responsibility 2: Process order logic
        order = self._create_order(request_data)
        order.calculate_total()

        # Responsibility 3: Save to database
        self._save_order_to_db(order)

        # Responsibility 4: Send confirmation email
        self._send_confirmation_email(order)

        # Responsibility 5: Format and return success response
        response_data = self._format_response(order)
        return response_data, 201

    def _validate_data(self, data):
        # Validation logic here
        pass # returns True or False

    def _create_order(self, data):
        # Order creation logic here
        pass # returns Order object

    def _save_order_to_db(self, order):
        # Database saving logic here
        pass

    def _send_confirmation_email(self, order):
        # Email sending logic here
        pass

    def _format_response(self, order):
        # Response formatting logic here
        pass
        
An SRP-compliant code is shown below.
"""

from typing import Any


class OrderValidator:
    def validate(self, data) -> bool:
        # Validation logic here
        print("Validating order data...")
        return bool(data)


class OrderProcessor:
    def create_and_calculate(self, data) -> Any:
        # Order creation and calculation logic
        print("Processing order...")
        # Returns Order object


class OrderRepository:  # Handles database interactions
    def save(self, order) -> None:
        # Database saving logic
        print("Saving order to DB...")


class EmailService:  # Handles email sending
    def send_confirmation(self, order) -> None:
        # Email sending logic
        print("Sending confirmation email...")


class OrderPresenter:  # Handles response formatting
    def format_success_response(self, order) -> tuple[dict[str, str], int]:
        # Response formatting logic
        print("Formatting response...")
        return {"message": "Order processed successfully"}, 201


# Our handler now orchestrates, but doesn't do the work itself
class OrderHandlerSRP:
    def __init__(self):
        self.validator = OrderValidator()
        self.processor = OrderProcessor()
        self.repository = OrderRepository()
        self.email_service = EmailService()
        self.presenter = OrderPresenter()

    def process_order_request(self, request_data) -> tuple[dict[str, str], int]:
        if not self.validator.validate(request_data):
            return {"error": "Invalid data"}, 400

        order = self.processor.create_and_calculate(request_data)
        self.repository.save(order)
        self.email_service.send_confirmation(order)

        return self.presenter.format_success_response(order)
