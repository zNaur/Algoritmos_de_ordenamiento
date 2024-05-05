from Algoritmos.Poo.Back import Metodo_de_ordenamiento


class BucketSort(Metodo_de_ordenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):
        max_value = max(arr)    # O(n)
        min_value = min(arr)    # O(n)
        bucket_range = (max_value - min_value) / len(arr)    # O(1)

        buckets = [[] for _ in range(len(arr) + 1)]    # O(n)

        for num in arr:    # O(n)
            index = int((num - min_value) / bucket_range)    # O(1)
            if index == len(arr):    # O(1)
                index -= 1    # O(1)
            buckets[index].append(num)    # O(1)

        for i in range(len(arr)):    # O(nlogn)
            buckets[i].sort()    # O(logn)

        k = 0    # O(1)
        for i in range(len(arr)):    # O(n)
            for j in range(len(buckets[i])):    # O(n^2)
                arr[k] = buckets[i][j]    # O(1)
                k += 1    # O(1)

        return arr    # O(1)
