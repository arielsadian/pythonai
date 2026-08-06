product_code = "   book-582"
clean_code = product_code.strip()

name = clean_code[0:4]
number = clean_code[5:]


is_name_valid = name.isalpha()


is_number_valid = number.isdigit()


print("product:",name.upper())
print("number:",number.zfill(6))
print("valid name:",is_name_valid)
print("valid number:",is_number_valid)
