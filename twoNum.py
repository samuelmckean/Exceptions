def twoNum():
    try:
        n1, n2 = eval(input("Enter two numbers separated by a comma: "))
    except NameError:
        print("Error!")
        n1, n2 = eval(input("Enter two numbers separated by a comma: "))
    finally:
        return n1 / n2
