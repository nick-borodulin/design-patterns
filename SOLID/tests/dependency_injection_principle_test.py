from SOLID.dependency_inversion_principle import (
    UserServiceDIP,
    MySQLDatabase,
    MongoDBDatabase,
)

# filepath: /Users/nick/src/design-patterns/SOLID/test_dependency_inversion_principle.py


def test_user_service_with_mysql():
    # Arrange
    mysql_db = MySQLDatabase()
    user_service = UserServiceDIP(mysql_db)
    test_user_data = {"name": "John Doe", "email": "john@example.com"}

    # Act
    result = user_service.register_user(test_user_data)

    # Assert
    assert isinstance(result, dict)
    assert result["db_id"] == 456
    assert result["status"] == "saved_mysql"


def test_user_service_with_mongodb():
    # Arrange
    mongo_db = MongoDBDatabase()
    user_service = UserServiceDIP(mongo_db)
    test_user_data = {"name": "Jane Doe", "email": "jane@example.com"}

    # Act
    result = user_service.register_user(test_user_data)

    # Assert
    assert isinstance(result, dict)
    assert result["db_id"] == "mongo_abc"
    assert result["status"] == "saved_mongodb"


def test_user_service_initialization():
    # Arrange
    mysql_db = MySQLDatabase()
    mongo_db = MongoDBDatabase()

    # Act
    user_service_mysql = UserServiceDIP(mysql_db)
    user_service_mongo = UserServiceDIP(mongo_db)

    # Assert
    assert user_service_mysql.db == mysql_db
    assert user_service_mongo.db == mongo_db


def test_user_service_with_empty_data():
    # Arrange
    mysql_db = MySQLDatabase()
    user_service = UserServiceDIP(mysql_db)
    empty_user_data = {}

    # Act
    result = user_service.register_user(empty_user_data)

    # Assert
    assert isinstance(result, dict)
    assert "db_id" in result
    assert "status" in result
