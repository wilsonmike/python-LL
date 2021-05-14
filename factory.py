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



if __name__ == "__main__":
    main()