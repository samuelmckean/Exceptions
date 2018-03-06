def askName():
    try:
        name = input("Enter your name: ")
    finally:
        if name.title() != name:
            raise SyntaxError
        return name
