file_name = input("Enter file name: ")


def read_file(file_name):
    content = []
    with open(f"../files/input{file_name}.txt", "r") as f:
        for line in f:
            content.append(line.replace("\n", ""))
    return content


s = read_file(file_name)[0]
x = read_file(file_name)[1]
y = read_file(file_name)[2]


def valid_length(s, x, y):
    return False if len(x) + len(y) > len(s) else True


def ignore_chars(s, x, y):
    start = 0
    i = 0
    while i < len(s):
        if s[i] == "0" or s[i] == "1":
            start = i
            break
        i += 1
    end = 0
    j = len(s) - 1
    while j >= 0:
        if s[j] == "0" or s[j] == "1":
            end = j
            break
        j -= 1
    new_s = []
    for i in range(start, end + 1, 1):
        if s[i] == "0" or s[i] == "1":
            valid = True
            new_s.append(s[i])
        else:
            valid = False
            break
    return new_s if valid else valid


# print(ignore_chars(s, x, y))


def canInterweave(s, x, y):
    if valid_length(s, x, y) == False:
        return f"not possible"
    if ignore_chars(s, x, y) == False:
        return f"not possible"
    else:
        s = ignore_chars(s, x, y)
    table = [False for i in range(len(s) + 1)]
    table[0] = True
    x_table = []
    x_rep = ""
    y_table = []
    y_rep = ""
    x_itr = 0
    y_itr = 0
    i = 0
    while i < len(s):
        if table[i] == True:
            if x[x_itr] == s[i]:
                table[i + len(s[i])] = True
                x_table.append(i)
                x_rep += s[i]
                if x_itr < len(x) - 1:
                    x_itr += 1
                elif x_itr == len(x) - 1:
                    x_itr = 0
            elif y[y_itr] == s[i]:
                table[i + len(s[i])] = True
                y_table.append(i)
                y_rep += s[i]
                if y_itr < len(y) - 1:
                    y_itr += 1
                elif y_itr == len(y) - 1:
                    y_itr = 0
            i += 1
        else:
            break
    is_valid = False
    if x_itr == 0 and y_itr == 0:
        is_valid = True
    if table[len(s)]:
        if is_valid:
            return f"s is interweaving\nx: {x_table}\ny: {y_table}\nrepitition of x: {x_rep}\nrepitition of y: {y_rep}"
        else:
            return f"s is partially interweaving\nx: {x_table}\ny: {y_table}\nrepitition of x: {x_rep}\nrepitition of y: {y_rep}"
    else:
        return f"not possible"


print(canInterweave(s, x, y))
