# 1 imports an Anfang
import matplotlib.pyplot as plt

# 2 Assignment funktion entfernen


# Sortiert die Liste nach dem mergeSort verfahren
def mergeSort(list_to_sort_by_merge):

    # Wenn die Teil-Liste <= 1 ist, ist sie schon sortiert
    if (len(list_to_sort_by_merge) > 1):        # 3. doppelte checker entfernen

        # Aufteilen der Liste in 2 Teil-Listen
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        # Sortieren der Teil-Listen (rekursiv)
        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        # Zusammenführen der Teillisten (nächste Zahl kann aus beiden der Teil-Listen kommen )
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                list_to_sort_by_merge[i] = left[l]
                l += 1
            else:
                list_to_sort_by_merge[i] = right[r]
                r += 1
            i += 1

        # Eine Teil-Liste ist schon durch. Alle restlichen Zahlen kommen aus der anderen Teil-Liste
        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


# 4 Nur ausführen, wenn Datei aktiviert wird und nicht auch, wenn die Datei importiert wird
if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.xlabel("index")                             # 5 Beschriftung hinzufügen
    plt.ylabel("my numbers")
    plt.title("unsortierte Zahlen vs index")
    plt.show()

    # 6 Das range Objekt muss nicht neu initialisiert werden
    mergeSort(my_list)
    plt.plot(x, my_list)
    plt.xlabel("index")
    plt.ylabel("my numbers")
    plt.title("sortierte Zahlen vs index")
    plt.show()
