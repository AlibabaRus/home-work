duration = int(input())
if duration < 60:
    print(duration,"���")
elif duration < 3600:
    print(duration // 60,"���", duration % 60,"���")
elif duration < 86400:
    print(duration // 3600, "���", duration % 3600 // 60, "���", duration % 3600 % 60,"���")
else:
    print(duration // 86400, "��", duration % 86400 // 3600, "���", duration % 86400 % 3600 // 60, "���", duration % 86400 % 3600 % 60,"���")    