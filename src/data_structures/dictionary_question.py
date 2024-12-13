# Initialize an empty dictionary to store product names and prices
products = {}


# Function to add products and their prices to the dictionary
def add_products():
    while True:
        # Ask user for product name and price
        product_name = input("Enter product name (or type 'done' to finish): ").strip()

        # Check if user is done entering products
        if product_name.lower() == 'done':
            break

        # Ask for the price of the product
        try:
            price = float(input(f"Enter price for {product_name}: ").strip())
            # Store the product and price in the dictionary
            products[product_name] = price
        except ValueError:
            print("Invalid price. Please enter a valid number.")


# Function to allow user to lookup product prices
def lookup_price():
    while True:
        # Ask user for product name to look up
        product_name = input("Enter product name to get its price (or type 'exit' to quit): ").strip()

        if product_name.lower() == 'exit':
            break

        # Check if the product is in the dictionary
        if product_name in products:
            print(f"The price of {product_name} is ${products[product_name]:.2f}")
        else:
            print(f"Product '{product_name}' not found in the dictionary.")


# Main program execution
print("Welcome to the Product Price Store!")

# Add products to the dictionary
add_products()

# Lookup product prices
lookup_price()

print("Thank you for using the Product Price Store!")