def age_assignment(*args, **kwags):
    storage = {}
    for x in args:
        for k, v in kwags.items():
            if x[0] == k:
                storage[x] = v
    return storage


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
