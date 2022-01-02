def extract(data):
    for i in data:
        if "." in i:
            file_name, ext = i.split(".")
            print(f"File name: {file_name}\nFile extension: {ext}")


extract(input().split("\\"))
