def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# Interactive input
if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter numbers separated by space: ").strip().split()))
        sorted_arr = insertion_sort_desc(arr)
        print("Sorted (descending):", sorted_arr)
    except ValueError:
        print("Please enter only integers separated by spaces then press ENTER when done.")
