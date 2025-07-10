def calculator_for_total(price,quantity,discount):
    total = price*quantity
    final_total = total-discount
    return final_total

def main():
    price = 100
    quantity = 2
    discount = 50
    
    total_amount = calculator_for_total(price,quantity,discount)
    print(f"final amount to pay {total_amount}")
    
if __name__ == "__main__":
    main()
