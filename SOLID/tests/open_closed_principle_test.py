from SOLID.open_closed_principle import (
    OrderProcessorOCP,
    CreditCardPayment,
    PayPalPayment,
    BitcoinPayment,
)


def test_credit_card_payment():
    # Arrange
    processor = OrderProcessorOCP()
    payment = CreditCardPayment()
    amount = 100
    details = {"card_number": "1234-5678-9012-3456"}

    # Act
    result = processor.process_order_payment(payment, amount, details)

    # Assert
    assert isinstance(result, dict)
    assert result["status"] == "success"
    assert result["transaction_id"].startswith("cc_")


def test_paypal_payment():
    # Arrange
    processor = OrderProcessorOCP()
    payment = PayPalPayment()
    amount = 50
    details = {"email": "test@example.com"}

    # Act
    result = processor.process_order_payment(payment, amount, details)

    # Assert
    assert isinstance(result, dict)
    assert result["status"] == "success"
    assert result["transaction_id"].startswith("pp_")


def test_bitcoin_payment():
    # Arrange
    processor = OrderProcessorOCP()
    payment = BitcoinPayment()
    amount = 75
    details = {"wallet_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}

    # Act
    result = processor.process_order_payment(payment, amount, details)

    # Assert
    assert isinstance(result, dict)
    assert result["status"] == "success"
    assert result["transaction_id"].startswith("btc_")
