class colors:
    GREEN = '\033[92m'
    ENDC = '\033[0m'


def main():
    from time import sleep

    num = input("Choose the number (1 to 5): ")

    if num == "1":
        first()
    elif num == "2":
        second()
    elif num == "3":
        third()
    elif num == "4":
        forth()
    elif num == "5":
        fifth()
    elif num == "0":
        exit()
    elif num == "bug":
        print()

        line1 = "A bug is never just a mistake."
        line2 = "It represents something bigger."
        line3 = "An error of thinking that makes you who you are."

        counter = 0
        for _ in range(len(line1) - 1):
            print(f"{colors.GREEN}{line1[0:counter]}", end='\r')
            sleep(0.05)
            counter += 1
        print(f"{colors.GREEN}{line1}")
        sleep(0.5)
        
        counter = 0
        for _ in range(len(line2) - 1):
            print(f"{colors.GREEN}{line2[0:counter]}", end='\r')
            sleep(0.05)
            counter += 1
        print(f"{colors.GREEN}{line2}")
        sleep(0.5)
        
        counter = 0
        for _ in range(len(line3) - 1):
            print(f"{colors.GREEN}{line3[0:counter]}", end='\r')
            sleep(0.05)
            counter += 1
        print(f"{colors.GREEN}{line3}")
        sleep(0.5)

        print()

        line4 = "You thought you've found a bug?"
        line5 = "But you've found just an easter egg."

        counter = 0
        for _ in range(len(line4) - 1):
            print(f"{colors.GREEN}{line4[0:counter]}", end='\r')
            sleep(0.05)
            counter += 1
        print(f"{colors.GREEN}{line4}")
        sleep(0.5)
        
        counter = 0
        for _ in range(len(line5) - 1):
            print(f"{colors.GREEN}{line5[0:counter]}", end='\r')
            sleep(0.05)
            counter += 1
        print(f"{colors.GREEN}{line5}")

        print(f"{colors.ENDC}")
        main()
    else:
        print(f"{num} is not from 1 to 5...")
        print("Try again.")
        print()
        main()


def first():
    print()

    number = int(input("Enter the number: "))
    print("Yes!") if number > 0 and number % 5 == 0 and len(str(number)) == 3 else print("No(((")
    
    print()
    main()


def second():
    print()

    nums = []
    for _ in range(3):
        nums.append(int(input("Enter the num: ")))
    
    odds = 0

    for num in nums:
        if num & 1:
            odds += 1
    
    print("Yes!") if odds <= 1 else print("No(((")
    
    print()
    main()


def third():
    print()

    x, y = float(input("Enter x: ")), float(input("Enter y: "))
    print("Yes!") if x >= 0 and x**2 + y**2 <= 1 and y <= 1 and y >= x - 1 else print("No(((")
    
    print()
    main()


def forth():
    import math as m

    print()

    x, y = float(input("Enter x: ")), float(input("Enter y: "))
    print("Yes!") if x >= 0 and x <= m.pi and y >= 0 and y <= m.sin(x) else print("No(((")
    
    print()
    main()


def fifth():
    print()

    x, y = float(input("Enter x: ")), float(input("Enter y: "))
    print("Yes!") if (x <= 0 and x**2 + y**2 <= 1) or (y >= x and x**2 + y**2 <= 1) else print("No(((")
    
    print()
    main()


main()
