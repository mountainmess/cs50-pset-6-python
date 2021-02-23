def main():
    n = 0
    # ask for an integer
    while True:
        try:
            n = int(input("height of pyramid: "))
        # ask again if not an int
        except ValueError:
            continue
        # break out of loop once number between one and eight entered
        else:
            if n > 0 and n < 9:
                break

    for i in range(n):
        # print spaces
        for j in range(n - (i + 1)):
            print(" ", end="")
        # print first hashes
        for h in range(n - (n - (i + 1))):
            print("#", end="")
        # print mid spaces
        print("  ", end="")
        # print last hashes
        for l in range(n - (n - (i + 1))):
            print("#", end="")
        print()


main()

