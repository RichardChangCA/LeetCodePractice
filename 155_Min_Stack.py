class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        stack_list = []
        self.stack_list = stack_list
        

    def push(self, x: int) -> None:
        self.stack_list.append(x)

    def pop(self) -> None:
        self.stack_list = self.stack_list[:-1]

    def top(self) -> int:
        return self.stack_list[-1]

    def getMin(self) -> int:
        return min(self.stack_list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Question:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

# Example:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.