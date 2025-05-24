# --- Absolute import ---
# from ecom.utils.calculator import add_item

# --- Relative import ---
from utils.calculator import add_item

def main():
    cart = []
    cart= input("Enter items to add to the cart (comma separated): ").split(",")
    cart = add_item(cart, "Laptop")
    cart = add_item(cart, "Mouse")
    print("Cart Contents:", cart)

if __name__ == "__main__":
    main()
