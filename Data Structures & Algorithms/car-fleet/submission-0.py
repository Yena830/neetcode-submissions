class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort first by speed
        combine = list(zip(position,speed))
        combine =sorted(combine,key=lambda x:x[0],reverse=True)


        #init
        stack = []

        # loop
        for p,s in combine:
            # add each time into the stack and check
            stack.append(float(target-p)/s)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)