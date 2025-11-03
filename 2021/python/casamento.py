n1, n2 = input(), input()

if len(n1) < len(n2):
    n1 = "0" * (len(n2) - len(n1)) + n1
elif len(n1) > len(n2):
    n2 = "0" * (len(n1) - len(n2)) + n2

n1_final, n2_final = "", ""
for i in range(len(n1)):
    if n1[i] <= n2[i]:
        n2_final += n2[i]
    if n1[i] >= n2[i]:
        n1_final += n1[i]

n1_final = int(n1_final) if n1_final != "" else -1
n2_final = int(n2_final) if n2_final != "" else -1
print(f"{min(n1_final, n2_final)} {max(n1_final, n2_final)}")