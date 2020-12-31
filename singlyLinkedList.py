class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    
    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node
    

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None: 
            self.head = new_node 
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node



    def enqueue(self, new_data):
        new_node = Node(new_data)

        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    
    def deleteNode(self, data):
        temp = self.head
        while temp.next:
            if temp.data == data:
                break

            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        temp = None

    

    def del_pos(self, pos):
        counter = 0
        temp = self.head
        while temp:
            if counter == pos - 1:
                break
            counter += 1
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        temp = None

    

    def getCountIter(self):
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
        return counter


    def getCountRec(self, node): 
        if not node:
            return 0
        else:
            return 1 + self.getCountRec(node.next) 
    def getCount(self):
        return self.getCountRec(self.head)

    
    def search(self, data):
        pos = 0
        temp = self.head

        while temp:
            if temp.data == data:
                break
            pos += 1
            temp = temp.next
        if pos + 1 == 1:
            return 'This is the first node'
        elif pos + 1 == 2:
            return 'This is the second node'
        elif pos + 1 == 3:
            return 'This is the third node'

        return 'this is the {}th node'.format(pos + 1)
    

    def exists(self, val):
        temp = self.head
        while temp:
            if temp.data == val:
                return True
            temp = temp.next 

        return False
            
        
    def getNthFromTheHead(self, n):
        counter = 1
        temp = self.head

        if n > self.getCountIter():
            return 'The position given over bounded'
        while temp:
            if counter == n:
                return temp.data
            counter += 1
            temp = temp.data


    def getNthFromTheEnd(self, n):
        counter = self.getCountIter()
        temp = self.head

        while temp:
            if counter == n:
                return temp.data
                break
            counter -= 1
            temp = temp.next

    
    def get_middle(self):
        
        mid = self.head
        temp = self.head
        counter = 1
        while temp:
            if counter % 2 == 0:
                mid = mid.next
            temp = temp.next
            counter += 1
        if mid:
            return mid.data



    def get_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    
    def getNumCount(self, n):
        temp = self.head
        counter = 0
        while temp:
            if temp.data == n:
                counter += 1
            temp = temp.next
        return counter 

    
    def is_palindrome(self):
        stack = []
        temp = self.head
        is_palin = True

        while temp:
            stack.append(temp.data)
            temp = temp.next

        temp = self.head
        while temp:
            if temp.data == stack.pop():
                is_palin = True
            else:
                is_palin = False
                break
            temp = temp.next
        return is_palin


    def remove_dups(self):
        temp = self.head
        if temp is None:
            return
        while temp.next:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new 
            else:
                temp = temp.next
        

                
            
    


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(0)
    llist.append(0)
    llist.append(1)
    llist.append(2)
    llist.remove_dups()
    print(llist.get_list())

