amount = int(input())

by_20 = amount//20
amount -= by_20*20
by_10 = amount//10
amount -= by_10*10
by_5 = amount//5
amount -= by_5*5
by_1 = amount

print(f"{by_20} - банкноти по 20 лв.\n"
      f"{by_10} - банкноти по 10 лв.\n"
      f"{by_5} - банкноти по 5 лв.\n"
      f"{by_1} - банкноти по 1 лв.")
