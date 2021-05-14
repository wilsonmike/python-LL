def main():
    x, y = 1000, 1000

    if (x < y):
        st = 'x is less than y'
    elif (x == y):
        st = 'x is equal to y'
    else:
        st = 'x is greater than y'

    print(st)

    # ternary operator
    st = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(st)
    
    for num in range(0,100):
       if num % 3 == 0 and num % 5 == 0:
           print("FizzBuzz")
       elif num % 3 == 0:
           print("Fizz")
       elif num % 5 == 0:
            print("Buzz")
       else:
            print(num)
    




if __name__ == "__main__":
    main()