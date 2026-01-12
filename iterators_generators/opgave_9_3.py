def first_1000_primes():
    num = 2 # start with the smallest prime
    primes = 0 # initialise primes at 0
    while primes < 1000: # loop until we got 1000 primes
        is_prime = True # assume number is a prime number
        for divider in range(2,int(num**0.5) + 1): # check until square root of num (including square root of num)
            # check whether there are any divisors other than 1 and itself
            if num % divider == 0: # if divisor found set flag to false and break
                is_prime = False
                break
        if is_prime: # if didn't break out of the loop (is_prime is still True)
            primes += 1 # number is a prime, so increment primes by 1
            yield num # yield or keep track of that num
        num += 1 # increase num by one to keep the search going

# loop over the generator which is iterable, and print the prime along with the number x that represents the x"th" prime
count = 0
for prime in first_1000_primes():
    print(f"prime: {prime}, number {count + 1}")
    count += 1