"""
ISP or Interface Segregation Principle states that interfaces should be thin rather than thick.
What it means that, similarly to SRP, but applied to interfaces, you shouldn't cram every possible 
method into an interface, but create separate interfaces instead, each one service one distinct purpose.

Analogy: Imagine a giant, all-in-one printer/scanner/copier/fax machine. 
It has one huge control panel with buttons and options for everything. 
If you only ever want to print, you're still faced with the complexity of the entire panel, 
and the software controlling it has to depend on libraries and drivers for scanning, copying, and faxing, 
even if you don't use them.

Bad design:
class UserManagerAndMore:
    def create_user(self, user_data):
        print("UserManager: Creating user...")
        # ... user creation logic ...

    def delete_user(self, user_id):
        print(f"UserManager: Deleting user {user_id}...")
        # ... user deletion logic ...

    def send_email_notification(self, user_id, message):
        print(f"Notifier: Sending email to user {user_id}...")
        # ... email sending logic ...

    def send_sms_notification(self, user_id, message):
        print(f"Notifier: Sending SMS to user {user_id}...")
        # ... SMS sending logic ...

    def generate_user_report_csv(self):
        print("Reporter: Generating user report CSV...")
        # ... CSV generation logic ...
        return "csv,data\nuser1,..."

    def generate_user_report_pdf(self):
        print("Reporter: Generating user report PDF...")
        # ... PDF generation logic ...
        return b"%PDF-..." # Returns bytes

ISP-compliant design is below.
"""

from abc import ABC, abstractmethod


# Define smaller, client-specific "interfaces" using ABCs (Optional but helpful)
# Represents clients that need to manage users
class IUserManager(ABC):
    @abstractmethod
    def create_user(self, user_data) -> None: ...

    @abstractmethod
    def delete_user(self, user_id) -> None: ...


# Represents clients that need to send notifications
class INotifier(ABC):
    @abstractmethod
    def send_email_notification(self, user_id, message) -> None: ...

    @abstractmethod
    def send_sms_notification(self, user_id, message) -> None: ...


# Represents clients that need to generate reports
class IUserRepository(ABC):  # Renamed as it focuses on data access/reporting
    @abstractmethod
    def generate_user_report_csv(self) -> str: ...

    @abstractmethod
    def generate_user_report_pdf(self) -> bytes: ...


# Implementations (can now inherit from specific interfaces if desired)
class UserManager(IUserManager):
    def create_user(self, user_data) -> None:
        print("UserManager (ISP): Creating user...")
        # ... user creation logic ...

    def delete_user(self, user_id) -> None:
        print(f"UserManager (ISP): Deleting user {user_id}...")
        # ... user deletion logic ...


class Notifier(INotifier):
    def send_email_notification(self, user_id, message) -> None:
        print(f"Notifier (ISP): Sending email to user {user_id}...")
        # ... email sending logic ...

    def send_sms_notification(self, user_id, message) -> None:
        print(f"Notifier (ISP): Sending SMS to user {user_id}...")
        # ... SMS sending logic ...


class UserRepository(IUserRepository):  # Handles data retrieval for reports
    def generate_user_report_csv(self) -> str:
        print("UserRepository (ISP): Generating user report CSV...")
        # ... CSV generation logic ...
        return "csv,data,separated\nuser1,data1,data2\n"

    def generate_user_report_pdf(self) -> bytes:
        print("UserRepository (ISP): Generating user report PDF...")
        # ... PDF generation logic ...
        return b"%PDF-compliant bytes..."
