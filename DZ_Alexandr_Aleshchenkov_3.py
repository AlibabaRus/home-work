for i in range(1,101):
    if i % 10 == 1 and i // 10 != 1:
        print(i, "�������")
    elif i % 10 >= 2 and i % 10 <= 4 and i // 10 != 1:
        print(i, '��������')
    else:
        print(i, '���������')