with open("output.txt", "w") as f:
    print("Hello world!", file=f)
    print("This line will also go to the file.", file=f)