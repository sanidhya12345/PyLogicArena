import math

class FibonacciNode:
    def __init__(self,key):
        self.key=key
        self.degree=0
        self.parent=None
        self.child=None
        self.left=self
        self.right=self
        self.mark=False # used for cascading cut

class FibonacciHeap:
    def __init__(self):
        self.min_node=None
        self.total_nodes=0

    def insert(self,key):
        node=FibonacciHeap(key)
        if self.min_node is None:
            self.min_node=node
        else:
            node.right=self.min_node
            node.left=self.min_node.left
            self.min_node.left.right=node
            self.min_node.left=node
            if node.key<self.min_node.key:
                self.min_node=node
        self.total_nodes+=1
        return node
    
    def get_min(self):
        return self.min_node.key if self.min_node else None
    

    def union(self,other_heap):

        # agar dusra heap khali hai to kuch nhi karna hai 

        if other_heap is None:
            return self
        
        # agar current heap khali hai to doosre ko consider karlo

        if self.min_node is None:
            self.min_node=other_heap.min_node
            self.total_nodes=other_heap.total_nodes
            return self
        
        #Pointer Magic: Dono list ko join karna

        # L1_start <-> L1_min <-> L1_end  AND  L2_start <-> L2_min <-> L2_end
        # Hum L1_min aur L2_min ke beech ke links ko swap/adjust karte hain

        self_min_next=self.min_node.right
        other_min_prev=other_heap.min_node.left

        self.min_node.right=other_heap.min_node
        other_heap.min_node.left=self.min_node

        self_min_next.left=other_min_prev
        other_min_prev.right=self_min_next

        if other_heap.min_node.key < self.min_node.key:
            self.min_node=other_heap.min_node
        
        self.total_nodes+=other_heap.total_nodes
        return self
    
    
    def decrease_key(self,node, new_key):

        if new_key > node.key:
            return "new key is not be greater than node"
        
        node.key=new_key
        parent=node.parent

        # agar heap property violate ho rahi hai

        if parent is not None and node.key < parent.key:
            self.cut=(node,parent)
            self.cascading_cut(parent)

        #naya min check karo

        if node.key< self.min_node.key:
            self.min_node=node

    def cut(self,node, parent):
        # 1 . node ko parent ki child list se hatao
        # (isme pointer manipulation code aayega)

        parent.degree=-1

        #2. node ko root list mein add karo

        node.parent=None
        node.mark=False # root pe aate hi mark false ho jata hai
        # link to root  list logic

    def cascading_cut(self,node):
        parent=node.parent
        if parent is not None:
            if node.mark==False:
                #agar pehli baar koi bacha khoya hai, to mark kardo

                node.mark=True

            else:
                # agar pehle se marked tha (doosra bacha khoya), to isko bhi cut karo

                self.cut(node,parent)
                self.cascading_cut(parent)



