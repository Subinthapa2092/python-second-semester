while True:
    try:
        name = int(input("Enter the your name :: "))
        print(name)
        break
    except ValueError:
        print(f"The num ois of different types")
    finally:
        print("i always executed")