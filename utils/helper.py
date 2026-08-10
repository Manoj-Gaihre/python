def calculate_total(quantity:int, price:float, discount:float = 0):
  total_amount = (quantity * price)
  discount_amount = (discount/100)*total_amount
  total_amount = total_amount-discount_amount
  return total_amount

def math(number):
  return min(number), max(number), sum(number)