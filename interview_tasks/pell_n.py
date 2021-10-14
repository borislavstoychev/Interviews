def pell(n, temp1=1, temp2=2, temp3=0):
    if n <= 2:
        return temp3
    temp3 = temp1 + 2 * temp2
    # Swap the previous number for the previous number's predecessor (temp1 =temp2).
    # Swap the generated and previously generated numbers (temp2 = temp3)
    temp1, temp2 = temp2, temp3
    return pell(n - 1, temp1, temp2, temp3)


num = 10
print(pell(num))
