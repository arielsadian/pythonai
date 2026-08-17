prices: list[int] = [120,45, 300,89,210,15,74,]
doubled = [p * 2 for p in prices]
print(f"doubled: {doubled}")
expensive = [p for p in prices if p > 100]
print(f"Expensive: {expensive}")
on_sale = [p-50 for p in prices if p > 100]
print(f"on sale: {on_sale}")
labels = ['pricey' if p > 100 else 'cheap' for p  in prices]
print (f"labels: {labels}")
as_text = [f"{p} NIS" for p in prices]
print (f" as text: {as_text}:)")


# targil 2

battery: list[int] = [78,92,45,61,88,30]
all_above_20 = all(b > 20 for b in battery)
print(f"all above 20: {all_above_20}")
any_below_40 = any(b < 40 for b in battery)
print(f"any below 40 :{any_below_40}")
all_full = all(b==100 for b in battery)
print(f" all_full: {all_full}")
ordered = sorted(battery)
print(f"ordered:{ordered}")
print(f"orginal:{battery}")
battery.sort(reverse=True)
print(f"sorted desc: {battery}")
top_three = battery[:3]
print(f"top three:{top_three}")



#targil 3
words = ["HELLO","WORLD", "PYHTON","CODE","DEVELOPER","AI"]
all_uppercase = all(w.isupper()for w in words)
print(f"all uppercase:{all_uppercase}")
has_long_word = any(len (w) > 5 for w in words)
print(f"has a long word:{has_long_word}")
by_lenght = sorted(words, key=len)
print(f"by lenght:{by_lenght}")