name = "amit kamaraj"
result = ""

replacements = {0: '2', 6: '5', 8: '7', 10: '9'}

for i in range(len(name)):
    if i in replacements:
        result += replacements[i]
    else:
        result += name[i]

print(result)
