from Algoritmos.Poo.Back import Metodo_de_ordenamiento


class BubbleSort(Metodo_de_ordenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):                # O(n^2)
        n = len(arr)                # O(1)
        for i in range(n - 1):            # O(n)
            for j in range(0, n - i - 1):        #O(n^2)
                if arr[j] > arr[j + 1]:            # O(1)
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]        # O(1)
        return arr            # O(1)
