# Pattern_13

# Output
#        A
#       B B
#      C C C
#     D D D D
#    E E E E E


n = 5
k = 2 * n - 2
x = 65
for i in range(0, n):
    ch = chr(x)
    x += 1
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print(ch, end=" ")
    print("\r")