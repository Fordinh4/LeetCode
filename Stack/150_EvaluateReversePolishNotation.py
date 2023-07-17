def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    valid_signs = ['+', '-', '*', "/"]

    for index, num in enumerate(tokens):
        if num in valid_signs:
            num1= int(stack.pop())
            num2= int(stack.pop())

            if num == "+":
                temp = num2 + num1
            elif num == "-":
                temp = num2 - num1
            elif num == "*":
                temp = num2 * num1
            elif num == "/":
                temp = int(float(num2)/num1)
            
            stack.append(temp)

        else:
            stack.append(int(num))


    return stack[0]






print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))