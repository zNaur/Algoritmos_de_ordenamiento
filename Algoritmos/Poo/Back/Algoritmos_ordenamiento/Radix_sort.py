from Algoritmos.Poo.Back import Metodo_de_ordenamiento


class RadixSort(Metodo_de_ordenamiento.MetodoOrdenamiento):
    @staticmethod
    def sort(arr):                          # Complejidad: O(n^2)    
        def counting_sort(arr, exp):        # Complejidad: O(n)
            n = len(arr)                    # O(1)       
            output = [0] * n                # O(1)
            count = [0] * 10                # O(1)

            for i in range(n):              # O(n)
                index = arr[i] // exp       # O(1)
                count[index % 10] += 1      # O(1)

            for i in range(1, 10):          # O(n)
                count[i] += count[i - 1]    # O(1)

            i = n - 1                       # O(1)
            while i >= 0:                   # O(n)
                index = arr[i] // exp       # O(1)
                output[count[index % 10] - 1] = arr[i]   # O(1)
                count[index % 10] -= 1      # O(1)
                i -= 1                      # O(1)

            for i in range(n):              # O(n)
                arr[i] = output[i]          # O(1)

        max_value = max(arr)                # O(1)
        exp = 1                             # O(1)
        while max_value // exp > 0:         # O(n)
            counting_sort(arr, exp)         # O(n)
            exp *= 10                       # O(1)

        return arr   