import re

def is_valid_price(price: str) -> bool:
    VALID_PATTERN = r"RM(\d{1,3},)*\d+(\.\d{2})?$"
    return bool(re.match(VALID_PATTERN, price))

if __name__ == "__main__":
    valid_prices = ["RM23", "RM23.00", "RM6000.99", "RM6,000.99", "RM6,888,222.99"]
    invalid_prices = ["RM23.0", "RM23,66.5", "$6000.9"]

    for price in valid_prices:
        assert is_valid_price(price), f"{price} should be valid"
    for price in invalid_prices:
        assert not is_valid_price(price), f"{price} should not be valid"
