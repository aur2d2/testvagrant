target = int(input("Enter the weekly budget for newspaper subscriptions = "))
# Initialize matrix a
a = [
    [3, 3, 3, 3, 3, 5, 6],
    [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
    [4, 4, 4, 4, 4, 4, 10],
    [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
    [2, 2, 2, 2, 2, 4, 4],
]

# Calculates number of rows and columns present in given matrix
rows = len(a)
cols = len(a[0])

compute = []
# Calculates sum of each row of given matrix
for i in range(0, rows):
    sumRow = 0
    for j in range(0, cols):
        sumRow = sumRow + a[i][j]
    print("Sum of " + str(i + 1) + " row: " + str(sumRow))
    compute.append(sumRow)

print(compute)

def subset_sum(compute, target, partial=[]):
    s = sum(partial)
    if s <= target:
        print("Combination can consist of (%s)" % (partial))
    if s >= target:
        return

    for i in range(len(compute)):
        n = compute[i]
        remaining = compute[i + 1:]
        subset_sum(remaining, target, partial + [n])
subset_sum(compute,target)