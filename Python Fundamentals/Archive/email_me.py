data = input()

index = data.find("@")
before = sum(ord(d) for d in data[:index])
after = sum(ord(d) for d in data[index+1:])
if (before - after) >= 0:
    print("Call her!")
else:
    print("She is not the one.")
