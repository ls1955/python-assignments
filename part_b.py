import re

def check_valid_price(user_input):
    pattern = r'^RM\s?(\d{1,3}(?:,\d{3})*|\d+)(\.\d{2})?$'
    if re.match(pattern, user_input):
        return "Valid price."
    else:
        return "Invalid price."

def check_valid_address(user_input):
    pattern = r'^\d+\s[A-Z][a-z]*(?:\s[A-Z][a-z]*\.?)*$'
    if re.match(pattern, user_input):
        return "Valid address."
    else:
        return "Invalid address."

if __name__ == "__main__":
    # Prompt user for a price input
    user_price_input = input("Enter a price (e.g., RM23, RM6,000.99): ")
    print(check_valid_price(user_price_input))
    
    # Prompt user for an address input
    user_address_input = input("Enter an address (e.g., 56 Jalan Mas Merah): ")
    print(check_valid_address(user_address_input))
