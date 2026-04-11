
smallest = None
largest = None

while True:
    numb = input("enter a number: ")
    if numb == "done":
        break
    try:
        numb = float(numb)
    except ValueError:
        print("invalid input")
        continue
    if smallest is None:
        smallest = numb
    elif largest is None:
        largest = numb
    elif numb < smallest:
        smallest = numb
    elif numb > largest:
        largest = numb

print("maximum is", largest)
print("minimum is", smallest)