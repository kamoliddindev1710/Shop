file = open("SALOM.txt", "w")

# maktab = 20
# file.write(f"{maktab}-Maktab")

# x = int(input(">>> "))
# y = int(input(">>> "))

# file.write(f"{x}+{y}={x+y}")

# lst = [1,4,2,3,2,5,4,2,2,5]
# for i in lst:
#     if i%2==0:
#         file.write(f"{i} ")

# lst = ["salomlar", "kiim", "chiii", "chelsea"]
# for i in lst:
#     file.write(f"{''.join(set(i))}\n")


lst = [1,4,2,3,2,5,4,2,2,5]
# lst.sort()
# for i in lst:
#     file.write(f"{i} ")

file.write(f'{" ".join([str(i) for i in sorted(lst)])}')


file.close()