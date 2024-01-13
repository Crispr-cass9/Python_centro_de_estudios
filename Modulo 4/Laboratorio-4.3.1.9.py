def is_prime(num):
    verifications = num//2
    while verifications > 1:
        if num%verifications == 0:
            return False
        verifications -= 1
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
