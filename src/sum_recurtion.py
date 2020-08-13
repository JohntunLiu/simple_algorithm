def sum(arr):
    total = 0
    if arr == []:
        return 0
    return arr[0]+sum(arr[1:])

print(sum([1,2,3]))