from Algoritmos.Poo.Back import Metodo_de_ordenamiento


class CountingSort(Metodo_de_ordenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):    # O(n+k)
        max_value = max(arr)    # O(n)
        min_value = min(arr)    # O(n)
        count = [0] * (max_value - min_value + 1)    # O(k)

        for num in arr:    # O(n)
            count[num - min_value] += 1    # O(1)

        sorted_arr = []    # O(1)
        for i in range(len(count)):    # O(k)
            sorted_arr.extend([i + min_value] * count[i])    # O(n)

        return sorted_arr    # O(1)
