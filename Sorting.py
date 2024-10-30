class Sorting:
    
    def bubble_sort(self,sortList):
        for i in range(0,len(sortList)):
            for j in range(i+1,len(sortList)):
                if sortList[i] > sortList[j]:
                    temp = sortList[i]
                    sortList[i] = sortList[j]
                    sortList[j] = temp
        print(sortList)
    
    def insertion_sort(self,insertionSortList):
        for i in range(1,len(insertionSortList)):
            for j in range(i,0,-1):
                if insertionSortList[j] < insertionSortList[j-1]:
                    temp = insertionSortList[j]
                    insertionSortList[j] = insertionSortList[j-1]
                    insertionSortList[j-1] = temp
        print(insertionSortList)





