def add(a,b):
    result = a+b
    return result

#this use to check current file without imported into main it called as name equal main construct
if __name__ == "__main__":
    print("This code runs when the script is executed directly")
    print(add(3, 4))
