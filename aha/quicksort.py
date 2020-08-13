list = [6,5,2,7,4,1,9,8,3,10]

# j = len(list)-1
# print(j)

def quicksort():
    for i in range(int(len(list)/2)+1):
        num = list[0]
        if list[i] < num:
            for j in range(-1,-int(len(list)/2),-1):
                print(j)
                


quicksort()
print(list[-1])