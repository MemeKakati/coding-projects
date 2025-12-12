def tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)

result = tip(50, 20)
print(result)  # Example usage: should return 10.0  

def total_with_tip(bill_amount, tip_percentage):
    return bill_amount + tip(bill_amount, tip_percentage)
result2 = total_with_tip(50,20)
print(result2)