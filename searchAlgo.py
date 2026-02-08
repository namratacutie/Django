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


linearSearch()