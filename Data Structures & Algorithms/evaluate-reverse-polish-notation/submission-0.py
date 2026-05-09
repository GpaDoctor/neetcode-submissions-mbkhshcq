class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t not in "+-*/":
                # If it's a number, push it onto the stack
                stack.append(int(t))
            else:
                # If it's an operator, pop the last two numbers
                # Note: b is the top element, a is the one below it
                b = stack.pop()
                a = stack.pop()
                
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    # Integer division in Python towards zero
                    # (a // b) behaves differently for negative numbers
                    stack.append(int(a / b))
        
        return stack[0]