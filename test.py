from TailCallDecorator import tailcall

@tailcall
def add_one(n):
  return n + 1

@tailcall
def add_three(n):
  return ("@add_one", n + 2)


@tailcall
def factorial(n, acc=1):
  if n <= 1:
    return acc
  return ("@factorial", n - 1, n * acc)

print(add_three(3))
print(factorial(10))
print(factorial(100))
print(factorial(1000))
