'''
По данному натуральном n вычислите сумму 1! + 2! + 3! + ... + n!.
В решении этой задачи можно использовать только один цикл.
'''
n = int(input())
fact = 1
summ = 0
for i in range(1, n + 1):
    fact *= i
    summ += fact
print(summ)