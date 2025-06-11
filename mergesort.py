# 1 imports an Anfang
import matplotlib.pyplot as plt

# 2 Assignment funktion entfernen


def mergeSort(list_to_sort_by_merge):
    """
    Sortiert die Liste nach dem mergeSort verfahren
    """

    # Wenn die Teil-Liste <= 1 ist, ist sie schon sortiert
    if (len(list_to_sort_by_merge) <= 1):
        return        # 3. doppelte checker entfernen

        # Aufteilen der Liste in 2 Teil-Listen
    mid = len(list_to_sort_by_merge) // 2
    left = list_to_sort_by_merge[:mid]
    right = list_to_sort_by_merge[mid:]

    # Sortieren der Teil-Listen (rekursiv)
    mergeSort(left)
    mergeSort(right)

    # 4. ausgeschriebenes naming
    left_index = 0
    right_index = 0
    main_index = 0

    # Zusammenführen der Teillisten (nächste Zahl kann aus beiden der Teil-Listen kommen )
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            list_to_sort_by_merge[main_index] = left[left_index]
            left_index += 1
        else:
            list_to_sort_by_merge[main_index] = right[right_index]
            right_index += 1
        main_index += 1

    # Kopieren der restlichen Elemente der linken Hälfte (Rechts komplett durch)
    while left_index < len(left):
        list_to_sort_by_merge[main_index] = left[left_index]
        left_index += 1
        main_index += 1

    # Kopieren der restlichen Elemente der rechten Hälfte (Links komplett durch)
    while right_index < len(right):
        list_to_sort_by_merge[main_index] = right[right_index]
        right_index += 1
        main_index += 1


# 5 Nur ausführen, wenn Datei aktiviert wird und nicht auch, wenn die Datei importiert wird
if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    x = range(len(my_list))
    plt.plot(x, my_list)
    plt.xlabel("index")                             # 6 Beschriftung hinzufügen
    plt.ylabel("my numbers")
    plt.title("unsortierte Zahlen vs index")
    plt.show()

    # 7 Das range Objekt muss nicht neu initialisiert werden
    mergeSort(my_list)
    plt.plot(x, my_list)
    plt.xlabel("index")
    plt.ylabel("my numbers")
    plt.title("sortierte Zahlen vs index")
    plt.show()
