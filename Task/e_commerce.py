def calculate_total(items,tax_rate):
    if tax_rate<0 and tax_rate>1:
        raise ValueError("Invalid tax rate")
    total=0
    for price in items:
        if price<0:
            raise ValueError("Negative price not allowed")
        total+=price
    return total+(total*tax_rate)
    