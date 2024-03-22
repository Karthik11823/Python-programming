import array

def linear_search(arr, x):
    for i in range(0,len(arr),1):
        if(arr[i]==x):
            return i
    return -1

def binary_search(arr, x):
    first=0
    last=len(arr)-1
    while first<=last:
        mid=(first+last)//2
        if (arr[mid]==x):
            return mid
        elif (arr[mid]<x):
            first=mid+1
        else:
            last=mid-1
    return -1

while True:
    search_type=input("Enter 'l' for linear or 'b' for binary for the search type, or 'q' to quit: ")
    if search_type=='q':
        break

    a=input("Enter the elements separated by spaces: ")
    arr=list(map(int, a.split()))

    search=int(input("Enter the element to search: "))

    if search_type=='l':
        result = linear_search(arr, search)
    elif search_type =='b':
        arr.sort()
        print(arr)
        result = binary_search(arr, search)
    else:
        print("Invalid search type. Please enter 'linear' or 'binary'.")
        continue

    if result!=-1:
        print("Element found at position", result)
    else:
        print("Element not found.")
