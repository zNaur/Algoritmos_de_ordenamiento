from Algoritmos.Poo.Back import Metodo_de_ordenamiento
import pandas as pd


class MergeSort(Metodo_de_ordenamiento.MetodoOrdenamiento):
    @staticmethod
    def merge(arr1, arr2):                            # Complejidad: O(n)
        i = 0                                         # O(1)
        j = 0                                         # O(1)
        result = []                                   # O(1)
        while i < len(arr1) and j < len(arr2):        # O(n)
            if arr2[j] > arr1[i]:                     # O(1)
                result.append(arr1[i])                # O(1)
                i += 1                                # O(1)
            else:
                result.append(arr2[j])                # O(1)
                j += 1                                # O(1)
        while i < len(arr1):                          # O(n)
            result.append(arr1[i])                    # O(1)
            i += 1                                    # O(1)
        while j < len(arr2):                          # O(n)
            result.append(arr2[j])                    # O(1)
            j += 1                                    # O(1)

        return result

    @staticmethod
    def sort(arr):                                    # Complejidad: O(log n)
        if isinstance(arr, list):                     # O(1)
            arr = pd.Series(arr)                      # O(1)

        if len(arr) <= 1:                             # O(1)
            return arr.values.tolist()                # O(1)
        mid = len(arr) // 2                           # O(1)
        left = MergeSort.sort(arr[:mid])              # O(log n)
        right = MergeSort.sort(arr[mid:])             # O(log n)

        return MergeSort.merge(left, right)           # O(n)
