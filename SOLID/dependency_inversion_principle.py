"""
DIP or Depenceny Inversion Principle states that higer-level modules should not call lower-level modules directly.
Instead, lower-level code should be abstracted using an interface and a reference to that interface should be 
passed into the higer-level module's constructor. That way, dependency is inverted, from
Higher -> Lower to Higher -> Interface, Lower -> Interface.

Bad design:
# DIP Violation Example

# Low-level module / Detail
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL Database...")
        # ... connection logic ...

    def save_user(self, user_data):
        print(f"Saving user data to MySQL: {user_data}")
        # ... SQL insert statement ...
        return {"db_id": 123, "status": "saved"}

# High-level module
class UserService:
    def __init__(self):
        # The high-level UserService is DIRECTLY creating
        # and depending on the concrete low-level MySQLDatabase.
        self.db = MySQLDatabase() # Tight coupling!

    def register_user(self, user_data):
        print("UserService: Registering new user...")
        self.db.connect() # UserService knows about MySQL connection details
        result = self.db.save_user(user_data) # UserService knows about MySQL save method
        print("UserService: User registration complete.")
        return result

DIP-compliant design is below.
"""

from abc import ABC, abstractmethod


# Abstraction (Interface) - High-level depends on this
class IDatabase(ABC):
    @abstractmethod
    def save_user(self, user_data) -> dict[str, int | str]:
        """Saves user data to the database."""
        ...


# Low-level Detail - Depends on the Abstraction by implementing it
class MySQLDatabase(IDatabase):
    def connect(self) -> None:
        print("Connecting to MySQL Database...")
        # ... connection logic ...

    def save_user(self, user_data) -> dict[str, int | str]:
        print(f"Saving user data to MySQL: {user_data}")
        # ... SQL insert statement ...
        # In a real app, connection would happen elsewhere or be managed
        # self.connect() # connect logic moved/managed outside this specific method
        return {"db_id": 456, "status": "saved_mysql"}


# Another Low-level Detail - Also depends on the same Abstraction
class MongoDBDatabase(IDatabase):
    def connect(self) -> None:
        print("Connecting to MongoDB Database...")
        # ... connection logic ...

    def save_user(self, user_data) -> dict[str, int | str]:
        print(f"Saving user data to MongoDB: {user_data}")
        # ... MongoDB insert logic ...
        # self.connect() # connect logic managed elsewhere
        return {"db_id": "mongo_abc", "status": "saved_mongodb"}


# High-level module - Now depends on the Abstraction (IDatabase)
class UserServiceDIP:
    # The UserService now depends on an object that fulfills the IDatabase contract.
    # It doesn't care *what* concrete database it is.
    def __init__(self, database: IDatabase) -> None:  # <-- Dependency Injection!
        self.db = database

    def register_user(self, user_data) -> dict[str, int | str]:
        print("UserServiceDIP: Registering new user...")
        # UserServiceDIP calls save_user through the IDatabase abstraction.
        # It doesn't know or care if it's talking to MySQL or MongoDB.
        result = self.db.save_user(user_data)
        print("UserServiceDIP: User registration complete.")
        return result
