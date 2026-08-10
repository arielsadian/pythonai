temps : list[int] = [21, 30, -999, 26, -999, 17, 33, -999 ,28]
print("count:", len(temps))
print("first three:", temps[ :3])
print("last three:", temps[-3: ])
print("Every second:",temps[::2])
while -999in temps:
    temps.remove(-999)
    print("cleaned:",temps)
    print("dropped the first reading:",temps.pop(0))
    temps.append(31)
    print("after append:" ,temps)
max_val = max(temps)
min_val = min(temps)
total_sum = sum(temps)
avg = total_sum / len(temps)
print(f"max: [max_val] min:[min_val] sum: [total_val] avg:{avg:.2f}")
for t in temps:
    if t > avg:
        print("above average:",t)