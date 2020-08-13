def max(arr):
    total = 0
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    sub_max = max(arr[1:])
    if arr[0] > sub_max:
        return arr[0]
    else:
        return sub_max

print(max([1,2,3,4]))