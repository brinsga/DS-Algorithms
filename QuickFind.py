class QuickFind():
    """
    QuickFind Class provides an eager approach to solve the Union-Find Problem
    
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
        
    def find(self,p,q):
        """
        Returns True, if p and q are connected, False otherwise.
        
        Keyword Arguments:
        
        p (int): First Component Identifier
        q (int): Second Component Identifier
        
        Returns: 
        bool: True if the two components are connected, False Otherwise

        """
        
        return self.id[p] == self.id[q]
        
            
    def union(self,p,q):
        """
        Combines the disjoint sets that contain p and q. Replaces all ids in the set containing p with the id
        of set that contains q
        
        Keyword Arguments:
        
        p (int): First Component Identifier
        q (int): Second Component Identifier
        
        Returns: 
        None

        """
        
        # Checking if p and q are connected already
        
        if not self.find(p,q):
            pid = self.id[p]
            for i in range(self.n):
                if self.id[i] == pid:
                    self.id[i] = self.id[q]
                    
    def checkCurrentStatus(self):
        
        """
        Returns the current state of the union-find datastructure
        
        """
        return self.id
        