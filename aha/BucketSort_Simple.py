# 首先我们需要申请一个大小为11的数组int a[11]。OK，现在你已经有了11个变量，编号从a[0]~a[10]。刚开始的时候，我们将a[0]~a[10]都初始化为0，表示这些分数还都没有人得过。例如a[0]等于0就表示目前还没有人得过0分，同理a[1]等于0就表示目前还没有人得过1分......a[10]等于0就表示目前还没有人得过10分

arr = [0 for i in range(1001)]

for i in range(5):
    j = int(input("input number:"))
    arr[j]+=1

for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)

