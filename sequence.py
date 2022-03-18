def look_and_say(x):
    prev = str(x)[0]
    res = ""
    count = 0

    for l in str(x):
        if l == prev:
            count += 1
        else:
            res += str(count) + prev
            count = 1
            prev = l
    else:
        res += str(count) + l

    return int(res)


number_sequence = int(input("Enter Number of Sequence: "))
initial_number = input("Enter Initial Number: ")
for i in range(number_sequence):
    print(initial_number)
    initial_number = look_and_say(initial_number)
