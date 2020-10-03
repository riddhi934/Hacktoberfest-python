#performing y/x using long division :
y = list(map(int,input().split()))
x = list(map(int,input().split()))

div = ""
for i in x:
    div += str(i)
div = int(div)

ans = 0
dn = ""
for i in y:
    