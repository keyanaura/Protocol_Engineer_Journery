mylist = [14, 7, 2, 10] 

# for i in range(len(mylist)-1):
#     for j in range(len(mylist)-1):
#         if(mylist[i]>mylist[j]):
#             mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
## Bubble Sort
flag = 0
for j in range(len(mylist)-1):
    swap = False
    print(j)
    for i in range(len(mylist)-1-j):
        print(mylist)
        if(mylist[i]>mylist[i+1]):
            mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
            swap = True
    if swap == False:
        break
print(mylist)