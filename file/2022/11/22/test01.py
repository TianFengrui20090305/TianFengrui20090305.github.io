sin = int(input("请输入一个正整数："))
for i in range(0, sin+1, 10):
    for j in range(i, i+10):
        if j > sin:
            break
        print(j, " ", end="")
    print()
