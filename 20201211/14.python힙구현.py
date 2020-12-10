
# i 레벨 왼쪽 자식노드는 (2i+1) 오른쪽 자식노드는 (2i+2)
# i번째 부모노드의 위치는(i-1/2)

class MaxHeap(object):
    def __init__(self):
        self.queue = []
    def insert(self,n):
        self.queue.append(n)
        last_index = len(self.queue)-1
        while 0 <= last_index:
            parent_index = self.parent(last_index)
            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:
                last_index = parent_index
            else:
                break

        def delete(self):
            last_index  = len(self.queue)
            if last_index < 0:
                return -1
            self.swap(0,last_index)
            maxv = self.queue.pop()
            self.maxHeapify(0)
            print(maxv)
            return maxv
        # 비교해나가며 재정렬
        def  maxHeapify(self,i):
            left_index = self.leftchild(i)
            right_index = self.rightchild(i)
            max_index  =right_index




