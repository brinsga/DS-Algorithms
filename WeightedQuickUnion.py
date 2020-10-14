# Reference - https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf

class WeightedQuickUnion():
    """
    QuickUnion Class provides an lazy approach to solve the Union-Find Problem
    
    """
    def __init__(self,n):
        """
        Keywords Arguments:
        id (int): The size of the data structures (Contains ids 0 to n-1)
        
        Returns: 
        None
        
        """
        
        self.id = list(range(n))
        self.n = n
        self.size = [0]*n
        
        
        
    def root(self, node):
        """
        Returns the ultimate parent node of the connected component that the given node belongs to.
        
        Keyword Argumets:
        node (int): Component identifier
        
        Returns:
        int: Parent Component Identifier
        
        """
        
        while self.id[node] != node:
            node = self.id[node]
            
        return node
        
         
    def find(self,p,q):
        """
        Returns True, if p and q are connected, False otherwise. Checks connection by comparing the roots 
        of p and q.
        
        Keyword Arguments:
        
        p (int): First Component Identifier
        q (int): Second Component Identifier
        
        Returns: 
        bool: True if the two components are connected, False Otherwise

        """
        
        proot = self.root(self.id[p])
        qroot = self.root(self.id[q])
        
        return proot == qroot
   
        
        
            
    def union(self,p,q):
        """
        Sets the value of root node of q as with the root of p. All connected components are made to come 
        under the same tree using this operation.
        
        Keyword Arguments:
        
        p (int): First Component Identifier
        q (int): Second Component Identifier
        
        Returns: 
        None

        """
        proot = self.root(self.id[p])
        qroot = self.root(self.id[q])
        
        if proot < qroot:
            self.id[proot] = qroot
            self.size[qroot]+=self.size[proot]
        else:
            self.id[qroot] = proot
            self.size[proot]+=self.size[qroot]

    def checkCurrentStatus(self):
        
        """
        Returns the current state of the union-find datastructure
        
        """
        return self.id
        