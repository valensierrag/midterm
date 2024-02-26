import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
    for j in random_numbers:
        if j > 80:
            random_numbers.remove(j)
            random_numbers.append(-j)

print(random_numbers)
