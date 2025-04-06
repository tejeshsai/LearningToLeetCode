class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)
        
    def deleteRoot(self):
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_value
    
    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        size = len(self.heap)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)
        
    def buildHeap(self, arr):
        size = len(arr)
        self.heap = arr
        for i in range(size // 2 - 1, -1, -1):
            self.heapify_down(i)

if __name__ == "__main__":
    heap = Heap()
    heap.buildHeap([5, 3, 8, 4, 6, 2, 1])
    print(heap.heap)
    heap.deleteRoot()
    print(heap.heap)
    
    

        
        