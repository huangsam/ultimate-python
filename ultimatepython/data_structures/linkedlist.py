class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None
        self.preval = None

class CLinkedList:
    def __init__(self):
        self.headval = None

    def AtBeginning(self, newdata):
        if self.headval == None:
            NewNode = Node(newdata)
            self.headval = NewNode
        else:
            
            NewNode = Node(newdata)
            temp = self.headval
            while temp.nextval is not None:
                if temp.nextval == self.headval:
                    break
                temp = temp.nextval
            
            NewNode.preval = temp
            NewNode.nextval = self.headval
            self.headval.preval = NewNode
            self.headval = NewNode
            temp.nextval = self.headval

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        temp = self.headval
        while temp.nextval is not None:
            if temp.nextval == self.headval:
                break
            temp = temp.nextval
        temp.nextval = NewNode
        NewNode.preval = temp
        NewNode.nextval = self.headval
        self.headval.preval = NewNode

    def InBetween(self, middle_node, newdata):
        temp = self.headval
        while temp is not None:
            if temp.dataval == middle_node:
                break
            temp = temp.nextval
        else:
            print("Could not find node")
            return
        
        NewNode = Node(newdata)
        NewNode.nextval = temp.nextval
        NewNode.preval = temp
        temp.nextval = NewNode

    def removeStart(self):
        temp = self.headval
        while temp.nextval is not None:
            if temp.nextval == self.headval:
                break
            temp = temp.nextval
        temp.nextval = self.headval.nextval
        self.headval.nextval.preval = temp
        self.headval = self.headval.nextval

    def removeEnd(self):
        temp = self.headval
        if temp == None:
            return
        else:
            
            while temp.nextval is not None:
                if temp.nextval.nextval == self.headval:
                    break
                temp = temp.nextval
            temp.nextval = self.headval
            self.headval.preval = temp

    def listprint(self):
        temp = self.headval
        if temp == None:
            return
        else:
            while temp.nextval is not None:
                print(temp.dataval)
                if temp.nextval == self.headval:
                    break
                temp = temp.nextval
    def listcount(self):
        temp = self.headval
        if temp == None:
            return 0
        
        count = 0
        while temp.nextval is not None:
            count += 1
            if temp.nextval == self.headval:
                break
            temp = temp.nextval
        return count
    
    def removeMiddle(self, removeKey):
        temp = self.headval
        while temp is not None:
            if temp.nextval.dataval == removeKey:
                break
            temp = temp.nextval
        before = temp
        key = self.headval
        while key is not None:
            if key.dataval == removeKey:
                break
            key = key.nextval
        after = key.nextval
        before.nextval = after
        after.preval = before
