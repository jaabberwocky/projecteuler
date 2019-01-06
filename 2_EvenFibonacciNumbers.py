first_value = 1
second_value = 2
value = second_value
sum = 2

while value <= 4000000:
    value = first_value + second_value
    if value % 2 == 0:
        sum += value
    first_value, second_value = second_value, value

print(sum)