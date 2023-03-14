keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]

zipped_dict = zip(keys, values)

for k, v in zipped_dict:
    print(F"key: {k}, value: {v}")


print(type(zipped_dict))
