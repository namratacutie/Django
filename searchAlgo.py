#Linear Search
def linearSearch():
    arr = [123,312,12,233,54,32,55,65,764,345,566,]
    target = int(input("Enter which number you want to search : "))
    found = False 

    for i in range(len(arr)):
        if arr[i] == target:
            print(f"The targeted value of {target} found in index {i}")
            found = True
            break

    if not found:
        print(f"The entered number not found in the array.")


#Binary Search
def binarySearch():
    arr = [213,1,334,23,54,67,34,767,3434,342,12323,43,11,566,76,5]
    found = False
    target = int(input("Enter the number you want to search : "))

    #In Binary Search we need to sort the array first, now using bubble sort
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if(arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    low = 0
    high = len(arr) - 1

    while(high >= low):
        mid = low + (high - low) // 2

        if target == arr[mid]:
            print(f"The targeted value of {target} found in index {mid}")
            found = True
            break

        elif target < arr[mid]:
            high = mid - 1

        elif target > arr[mid]:
            low = mid + 1

linearSearch()
binarySearch()