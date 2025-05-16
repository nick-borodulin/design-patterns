from SOLID.interface_segregation_principle import UserManager, Notifier, UserRepository


def test_user_manager():
    # Arrange
    manager = UserManager()
    user_data = {"name": "Test User"}
    user_id = "123"

    # Act & Assert - Should not raise exceptions
    manager.create_user(user_data)
    manager.delete_user(user_id)


def test_notifier():
    # Arrange
    notifier = Notifier()
    user_id = "123"
    message = "Test notification"

    # Act & Assert - Should not raise exceptions
    notifier.send_email_notification(user_id, message)
    notifier.send_sms_notification(user_id, message)


def test_user_repository():
    # Arrange
    repository = UserRepository()

    # Act
    csv_result = repository.generate_user_report_csv()
    pdf_result = repository.generate_user_report_pdf()

    # Assert
    assert isinstance(csv_result, str)
    assert csv_result.startswith("csv,data")
    assert isinstance(pdf_result, bytes)
    assert pdf_result.startswith(b"%PDF")
