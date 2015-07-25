a = int(raw_input("Enter the number: "))
divisors = [1]
max_divisor = a
i = 2

while (i <= max_divisor):
	if (a % i == 0):
		if (max_divisor == a):
			max_divisor = a / i
		divisors.append(i)
	i += 1

if (max_divisor not in divisors): 
	divisors.append(a)

print divisors