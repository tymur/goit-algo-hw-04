import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def tim_sort(arr):
    return sorted(arr)


def test_sorting_algorithms():
    sizes = [1000, 5000, 10000, 50000]
    results = {}

    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]

        results[size] = {
            "Insertion Sort": timeit.timeit(
                lambda: insertion_sort(arr.copy()), number=1
            ),
            "Merge Sort": timeit.timeit(lambda: merge_sort(arr.copy()), number=1),
            "Timsort": timeit.timeit(lambda: tim_sort(arr.copy()), number=1),
        }

    return results


if __name__ == "__main__":
    results = test_sorting_algorithms()

    for size, times in results.items():
        print(f"\nРозмір масиву: {size}")
        for method, time_taken in times.items():
            print(f"{method}: {time_taken:.6f} секунд")
