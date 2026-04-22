class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position,speed)]
        cars.sort(reverse=True) #离终点最近的车先处理
        stack = []
        for p,s in cars:
            time = (target-p)/s #计算每辆车到达终点的时间
            if stack and stack[-1]>=time: #如果当前车比前面的车更快到达，说明它会被前面的车"挡住"，合并成同一个车队
                continue
            stack.append(time) #否则它会形成一个新的车队，压入栈中
        return len(stack)