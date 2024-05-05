from Algoritmos.Poo.Back import Metodo_de_ordenamiento


class QuickSort(Metodo_de_ordenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):                  # Complejidad: O(n^2)                                   
        if len(arr) <= 1:           # O(1)
            return arr
        pivot = arr[len(arr) // 2]                # O(1)
        left = [x for x in arr if x < pivot]      # O(n)
        middle = [x for x in arr if x == pivot]   # O(n)
        right = [x for x in arr if x > pivot]     # O(n)
        return QuickSort.sort(left) + middle + QuickSort.sort(right) # O(n^2)