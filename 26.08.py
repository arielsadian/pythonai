

tables = {
   2:  {2**i: f"yes 2 power {i} " for  i in range (33)},
   3:  {3**i: f"yes 3 power {i} " for i in range(33)},
   5: {5** i: f"yes 5 power {i} " for i in range(33)}}
while True:
    user_input = input("enter a number:")
    if user_input.lower() == 'q':
        break
    n = int(user_input)
    found = False
    for base, table in tables.items():
        if n in table:
            print(table [n])
            found = True
            break
    if not found:
            print("no")