"""
5.	Multiples of 3 and 5. Find the best algorithm.
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 100000000.
source: https://projecteuler.net/problem=1
"""
import time

# Fastest solution - generator
start = time.time()

total = sum(i for i in range(100000000) if i % 3 == 0 or i % 5 == 0)

end = time.time()
print("Generator")
print(f"Sum: {total}. Time: {end - start}")             # Time: 7.598452806472778


"""
# Other options
## List comprehension
start = time.time()
total = sum([i for i in range(100000000) if i % 3 == 0 or i % 5 == 0])
end = time.time()
print("List comprehension")
print(f"Sum: {total}. Time: {end - start}")             # Time: 8.142762660980225


## For Loop and Sum
start = time.time()

total = 0
for i in range(100000000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

end = time.time()
print("For Loop and Sum")
print(f"Sum: {total}. Time: {end - start}")             # Time: 10.234657287597656


## Generator Func
def my_gen(n):
    num = 0
    while num < n:
        if num % 3 == 0 or num % 5 == 0:
            yield num
        num += 1


start = time.time()
total = sum(my_gen(100000000))
end = time.time()
print("Generator Func")
print(f"Sum: {total}. Time: {end - start}")             # Time: 12.171011924743652
"""