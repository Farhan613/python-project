import queue
from tabnanny import check
import DoublyLinkedList

QueList = DoublyLinkedList.DoublyLinkedList
class QueueLinkedList:
    list = QueList()
    
    def first(self):
        return self.head.value

    def checkEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def  enqueue(self, element) ->bool:
        list.append(element)
        return True
    def dequeue(self):
        if self.checkEmpty():
            element = self.list.first
        else:
            return None
        return self.list.remove(element)



queue = QueueLinkedList()
queue.enqueue(1)
queue.enqueue(2)

queue.enqueue(3)

queue.enqueue(4)

queue.enqueue(5)

queue.enqueue(6)

queue.enqueue(7)







queue = QueueLinkedList()
queue.checkEmpty()


