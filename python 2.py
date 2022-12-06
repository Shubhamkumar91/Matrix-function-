'''A basket is given to you in the shape of a matrix. If the size of the matrix is N x N then the range of number of eggs you can put in each slot of the basket is 1 to N2 .
Your task is to arrange the eggs in the basket such that the sum of each row, column and the diagonal of the matrix remain same.

Test case for your reference:
Input by the user dimension of the basket i.e., N = 3
So, number of eggs you can put at each slot are in the range of 1 to 32 (1 to 9)

Input:
6 3 6
5 5 5
4 7 4

Explanation: Now the value of the sum of any row or column as well as diagonal is 15 Note: 2 < = N <= 100

(Student is free to decide the input and output layout for this mini project)'''

def forEvenNumber(n):
    arr = [[(n * y) + x + 1 for x in range(n)] for y in range(n)]
    for i in range(0, n // 4):
        for j in range(0, n // 4):
            arr[i][j] = (n * n + 1) - arr[i][j];
    for i in range(0, n // 4):
        for j in range(3 * (n // 4), n):
            arr[i][j] = (n * n + 1) - arr[i][j];
    for i in range(3 * (n // 4), n):
        for j in range(0, n // 4):
            arr[i][j] = (n * n + 1) - arr[i][j];
    for i in range(3 * (n // 4), n):
        for j in range(3 * (n // 4), n):
            arr[i][j] = (n * n + 1) - arr[i][j];
    for i in range(n // 4, 3 * (n // 4)):
        for j in range(n // 4, 3 * (n // 4)):
            arr[i][j] = (n * n + 1) - arr[i][j];
    print("\nSum of all row, column and diagonals = ",
          n * (n * n + 1) // 2, "\n")
    for i in range(n):
        for j in range(n):
            print('%2d ' % (arr[i][j]), end=" ")
        print()
def forOddNumber(n):
    mgsqr = [[0 for x in range(n)]
             for y in range(n)]
    r = n // 2
    c = n - 1
    num = 1
    while num <= (n * n):
        if r == -1 and c == n:
            c = n - 2
            r = 0
        else:
            if c == n:
                c = 0
            if r < 0:
                r = n - 1
        if mgsqr[int(r)][int(c)]:
            c = c - 2
            r = r + 1
            continue
        else:
            mgsqr[int(r)][int(c)] = num
            num = num + 1
        c = c + 1
        r = r - 1
    print("\nSum of all row, column and diagonals = ",
          n * (n * n + 1) // 2, "\n")
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (mgsqr[i][j]), end='')
        print()
print("\nWELCOME:)\n")
n = int(input("Please Enter Number of Rows and Column (n*n): "))
if n%2==0:
    forEvenNumber(n)
else:
    forOddNumber(n)
print("\nThank You :)")