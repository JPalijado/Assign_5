def InputThreeNumbers():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))
    return n1,n2, n3

def DisplayLowestNumber(n1, n2, n3):
    if (n1 < n2 and n2 < n3) or (n1 < n3 and n3 < n2):
        print("\nThe lowest number is:",n1)
    elif (n2 < n3 and n3 < n1) or (n2 < n1 and n1 < n3):
        print("\nThe lowest number is:",n2)
    else:
        print("\nThe lowest number is:",n3)

n1, n2, n3 = InputThreeNumbers()

DisplayLowestNumber(n1, n2, n3)