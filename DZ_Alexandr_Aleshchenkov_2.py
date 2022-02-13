mas = []
ans_1,ans_2 = 0,0
for i in range(1,1000,2):
    mas.append(i**3)
for l,k in enumerate(mas):
    a = k
    sum_a = 0
    while a != 0:
        sum_a += a % 10
        a //= 10
    if sum_a % 7 == 0:
        ans_1 += k
    mas[l] += 17
for k in mas:
    a = k
    sum_a = 0
    while a != 0:
        sum_a += a % 10
        a //= 10
    if sum_a % 7 == 0:
        ans_2 += k
print(ans_1 , ans_2)