# Q7: Tower of Hanoi
def hanoi(n, source, target, spare):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
    else:
        hanoi(n-1, source, spare, target)
        print("Move disk", n, "from", source, "to", target)
        hanoi(n-1, spare, target, source)

n = int(input("Number of disks: "))
hanoi(n, "A", "C", "B")

# Q8: Recursive binary search (list must be sorted)
def binary_search(a, key, low, high):
    if low > high: return -1
    mid = (low + high) // 2
    if a[mid] == key: return mid
    if key < a[mid]: return binary_search(a, key, low, mid-1)
    return binary_search(a, key, mid+1, high)

nums = list(map(int, input("Enter sorted numbers: ").split()))
key = int(input("Search value: "))
print("Index:", binary_search(nums, key, 0, len(nums)-1))
