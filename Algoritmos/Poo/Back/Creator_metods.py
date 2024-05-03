from Algoritmos.Poo.Back.Algoritmos_ordenamiento import Bubble_sort,Bucket_sort, Counting_sort, Heap_sort,insetion_sort,Merge_sort,Quick_sort,Radix_sort,Selection_sort


class Creator:
    def __init__(self):
        self.dict_clases = {
            1: Bubble_sort.BubbleSort(),
            2: Bucket_sort.BucketSort(),
            3: Counting_sort.CountingSort(),
            4: Heap_sort.HeapSort(),
            5: insetion_sort.InsertionSort(),
            6: Merge_sort.MergeSort(),
            7: Quick_sort.QuickSort(),
            8: Radix_sort.RadixSort(),
            9: Selection_sort.SelectionSort()
        }

    def ordenar(self, num, arr, colum):
        metod_name = {
            1: "BubbleSort",
            2: "BucketSort",
            3: "CountingSort",
            4: "HeapSort",
            5: "InsertionSort",
            6: "MergeSort",
            7: "QuickSort",
            8: "RadixSort",
            9: "SelectionSort"
        }
        clase = self.dict_clases.get(num)
        if clase:
            array_sorted = clase.sort(arr)
            name_metod = metod_name.get(num)
            message = f"El array fue ordenado utilizando el método de ordenamiento {name_metod} y la columna {colum}."
            return array_sorted, message
        else:
            print("Número de método de ordenamiento no válido")