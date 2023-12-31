var = pow(10, 8)
print(var)
var+=1
sum=0

for i in range(1,var):
    sum1 = 0
    while i > 0:
        digit = i % 10
        sum1 += digit
        i //= 10
    sum+=sum1
print(sum)