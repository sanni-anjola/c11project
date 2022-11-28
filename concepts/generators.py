def generate_up_to(num):
    start = 1
    while start <= num:
        yield start
        start += 1
        yield "poof"


gen = generate_up_to(10)

gen_exp = (num for num in range(1, 11))
print("Gen exp", gen_exp)

print(next(gen))
print(next(gen))
print(next(gen))

print(list(gen))
