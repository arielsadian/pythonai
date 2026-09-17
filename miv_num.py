ranks = []
while True:
    user_input = input("enter rank:")
    if user_input =="-999":
        if len(ranks) >= 10:
            break
        else:
            print("need at least 10 valid ranks. keep entering.")
            continue
    try:
        val = float(user_input)
        if 1 <= val <= 5:
            ranks.append(val)
        else:
            print("not in range,skip")
    except ValueError:
        print("Invalid input,skip")
if ranks:
    avg_rank = sum(ranks) / len(ranks)
    max_rank = max(ranks)
    total_valid = len(ranks)
    print(f"average rank:{avg_rank}")
    print(f"Highest rank:{max_rank}")
    print(f"total valid ranks entered:{total_valid}")
  





