def linear_search(arr, search):
    for i in range(len(arr)):
        if arr[i] == search:
            return i
    return -1

def binary_search(arr, search):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == search:
            return mid
        elif arr[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    return -1

a = input("Enter a list: ").split()
print("Original list:", a)

search_type = input("Enter the search type ('l' or 'b'): ")

if search_type == 'l':
    search_func = linear_search
elif search_type == 'b':
    x=a.sort()
    print("Sorted list:", x)
    search_func = binary_search
else:
    print("Invalid search type")
    exit()

search = input("Enter an element to search (or 'q' to quit): ")

while search != 'q':
    target = search_func(a, search)
    if target != -1:
        print("Element found at ", target)
    else:
        print("Element not found")
    search = input("Enter an element to search (or 'q' to quit): ")
