# Shaking off some cobwebs

def countdown(num):
    """This function takes a number as an argument and counts down to zero."""
    while num >= 0:
        print(num)
        num -= 1
    else:
        print("BOOM! goes the dynamite")



def main():
    countdown(20)




if __name__ == "__main__":
    main()