def FileHandle(filename):
    try:
        with open(filename,"r+") as f:
            f.write("helow evyeorne how are you")
            f.seek(0)
            fcontent = f.read()
            print(fcontent)
    except IOError:
        print("Something wrong in file operations")
    else:
        print("okay")
fname = input("Give a File name: ")
FileHandle(fname)