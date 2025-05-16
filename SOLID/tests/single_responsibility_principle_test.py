from SOLID.single_responsibiliy_principle import OrderHandlerSRP


def test_successful_order_processing():
    # Arrange
    handler = OrderHandlerSRP()
    request_data = {"item": "test_item", "quantity": 1}

    # Act
    response, status_code = handler.process_order_request(request_data)

    # Assert
    assert isinstance(response, dict)
    assert status_code == 201
    assert response["message"] == "Order processed successfully"


def test_invalid_order_data():
    # Arrange
    handler = OrderHandlerSRP()
    invalid_data = {}

    # Act
    response, status_code = handler.process_order_request(invalid_data)

    # Assert
    assert isinstance(response, dict)
    assert status_code == 400
    assert response["error"] == "Invalid data"
