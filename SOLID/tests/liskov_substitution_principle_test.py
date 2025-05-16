from SOLID.liskov_substitution_principle import UserLSP, GuestUserLSP


def test_regular_user_can_receive_messages():
    # Arrange
    user = UserLSP()

    # Act & Assert
    assert user.can_receive_message() is True


def test_guest_user_cannot_receive_messages():
    # Arrange
    guest = GuestUserLSP()

    # Act & Assert
    assert guest.can_receive_message() is False


def test_send_message_to_regular_user():
    # Arrange
    user = UserLSP()
    message = "Test message"

    # Act
    user.send_message(message)  # Should print message sending confirmation

    # Assert - No exception should be raised


def test_send_message_to_guest_user():
    # Arrange
    guest = GuestUserLSP()
    message = "Test message"

    # Act
    guest.send_message(message)  # Should print skipping message

    # Assert - No exception should be raised
