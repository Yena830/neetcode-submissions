class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.stack) <= 1:
            self.min.append(val)
        else:
            if self.min[-1] >= val:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])
            

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) >0:
            self.stack.pop()
            self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        
