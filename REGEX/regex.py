class Node:

    # Constructor to initialize the node object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    # Function to initialize LL
    def __init__(self,arr=None):
        if not arr:
            self.head = None
        else :
            self.head = Node(arr[0])
            current = self.head
            for data in arr[1:]:
                node = Node(data)
                current.next = node
                current = current.next

    # Function to insert an element to the tail of list
    def append(self,data):
        new_node = Node(data)

        # Case of emplty list
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Function to reverse elements of linked list

    def reverse(self):

        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    # Function to print out the linked list
    def __str__(self):

        # Case of emplty list
        if not self.head:
            return 'Empty Linked List'

        current = self.head
        result = '[ '

        while current.next:
            result += str(current.data)+' -- '
            current = current.next

        result += str(current.data)+' ]'

        return result






def leftover_bidders(bids, number_of_items):
    ######### DO NOT MODIFY BELOW ###########
    myQueue = MySpecialQueue()

    for bid in bids:
        myQueue.insert(bid)
    for sale in range(number_of_items):
        myQueue.dequeue()

    return myQueue.queue if myQueue.queue else [None]


######### DO NOT MODIFY ABOVE ###########

class MySpecialQueue:
    def __init__(self):
        # Do not change the variable name of self.queue
        self.queue = None

    def insert(self, data):
        if  self.queue is None:
            self.queue = [data]
        else:
            self.queue.append(data)

    def dequeue(self):
        if self.queue is not None:
            return self.queue.pop(self.queue.index(max(self.queue)))
        return None






def pop(arr,i):
    result = []
    j = 0
    while j < i :
        result.append(arr[j])
        j += 1

    while j < len(arr):
        if j != i:
            result.append(arr[j])
        j+=1

    return result


def pop2(arr,i):
    return arr[:i] + arr[i+1:]







if __name__ == '__main__':

    arr = [1,3,5,7,9,11,13,15]
    print(pop(arr,9))



