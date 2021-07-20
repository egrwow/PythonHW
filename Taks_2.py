list_of_numbers = []
all_sum = 0

for i in range(1, 1001, 2):
    list_of_numbers.append(i ** 3)

for ind, val in enumerate(list_of_numbers):
    sum_digits = 0
    while val:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_numbers[ind]
    list_of_numbers[ind] += 17

print(all_sum)

all_sum = 0

for ind, val in enumerate(list_of_numbers):
    sum_digits = 0
    while val:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_numbers[ind]

print(all_sum)
