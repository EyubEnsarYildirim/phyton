def fıbonacciler(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fıbonacciler(n-1)+fıbonacciler(n-2)
for i in range(1,21):
        print(fıbonacciler(i),end=" ")
print()