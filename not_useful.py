# Fill missing cabin data

# Added a column with Cabin Letter
cabin_letter = []
cabin_sub = ''
for cabin in df.Cabin:
    i = 0
    if type(cabin) == str:
        sub_string = cabin.split(' ')
        if len(sub_string) == 1:
            cabin_letter.append(cabin[0][0])
        else:
            for c in sub_string:
                cabin_sub += ',' + c[0]
                if c[0] == cabin_sub[i+1] and i != 0:
                    cabin_sub = cabin_sub[1:len(cabin_sub)-2]
                i += 1
            cabin_letter.append(cabin_sub[1:])
            cabin_sub = ''
    else:
        cabin_letter.append('z')

