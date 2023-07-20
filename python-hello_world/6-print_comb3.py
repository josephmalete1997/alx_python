num = []

for i in range(0,100):
    if i < 10:
        print(end = "0{}, ".format(i))
    else:
        if i%10 == 0:
            continue
        print(i, end = ", ")
