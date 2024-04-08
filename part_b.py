import re

def is_valid_price(price: str) -> bool:
    VALID_PATTERN = r"^RM(\d{1,3},)*\d+(\.\d{2})?$"
    return bool(re.match(VALID_PATTERN, price))

def is_valid_address(address: str) -> bool:
    VALID_PATTERN = r"^\d+ ([A-Z][a-zA-Z]+\.? )*([a-zA-Z]+\.? )*[a-zA-Z]+\.?$"
    return bool(re.match(VALID_PATTERN, address))

if __name__ == "__main__":
    valid_prices = ["RM23", "RM23.00", "RM6000.99", "RM6,000.99", "RM6,888,222.99"]
    invalid_prices = ["RM23.0", "RM23,66.5", "$6000.9"]

    for price in valid_prices:
        assert is_valid_price(price), f"{price} should be valid"
    for price in invalid_prices:
        assert not is_valid_price(price), f"{price} should be invalid"

    valid_addresses = ["56 Jalan Mas Merah", "33 Kota tinggi", "77 J. Sungai Luas"]
    invalid_addresses = ["Lot 8 Kampung Lapan, 8-A", "23 12 Taman baru", "13.8 Jalan Hang Tuah"]

    for address in valid_addresses:
        assert is_valid_address(address), f"{address} should be valid"
    for address in invalid_addresses:
        assert not is_valid_address(address), f"{address} should be invalid"
