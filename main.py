#fizzbuzz Program
#if divisible by 3 then fizz
#if divisible by 4 then buzz
#if divisible by both 3 and 5 then fizzbuzz

for number in range(1,101):
  if number % 3 ==0 and number%5==0:
    print("FizzBuzz")
  elif number%3==0:
    print("Fizz")
  elif number%5==0:
    print("Buzz")
  else:
    print(number)