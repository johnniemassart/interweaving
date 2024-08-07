# user input file name, number only
file_name = input("Enter file number (1-5 only): ")


# function to read file, store in list
def read_file(file_name):
    content = []
    with open(f"../files/input{file_name}.txt", "r") as f:
        for line in f:
            content.append(line.replace("\n", ""))
    return content


# index location of s, x, y values from read_file function
s = read_file(file_name)[0]
x = read_file(file_name)[1]
y = read_file(file_name)[2]


# determine if s is long enough
def valid_length(s, x, y):
    return False if len(x) + len(y) > len(s) else True


# characters present in x, y
def present_x_y_characters(s, x, y):
    present_chars = set()
    entire_string = x + y
    for char in entire_string:
        if char not in present_chars:
            present_chars.add(char)
    return present_chars


# ignore characters not present in x, y at start, end of s
# return new_s list if no invalid characters in between string s, else false
def ignore_characters(s, x, y):
    chars = present_x_y_characters(s, x, y)
    start = 0
    i = 0
    while i < len(s):
        if s[i] in chars:
            start = i
            break
        i += 1
    end = 0
    j = len(s) - 1
    while j >= 0:
        if s[j] in chars:
            end = j
            break
        j -= 1
    new_s = []
    for i in range(start, end + 1, 1):
        if s[i] in chars:
            valid = True
            new_s.append(s[i])
        else:
            valid = False
            break
    return new_s if valid else valid


# determine if interweaving is possible by utilizing dynamic programming - tabulation
def canInterweave(s, x, y):
    if valid_length(s, x, y) == False:
        return f"not possible"
    if ignore_characters(s, x, y) == False:
        return f"not possible"
    else:
        s = ignore_characters(s, x, y)
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
