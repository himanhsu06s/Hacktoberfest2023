def heapify(arr, n, i):
    """
    A function to heapify the array.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    """
    Function to perform heapsort on the array.
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)


if __name__ == "__main__":
    try:
        n = int(input("Enter the number of elements: "))
        arr = []
        for i in range(n):
            arr.append(int(input(f"Enter element {i + 1}: ")))

        heapSort(arr)
        print("Sorted array is:")
        for num in arr:
            print(num, end=" ")
        print()
    except ValueError as e:
        print("Invalid input. Please enter valid integers.")
