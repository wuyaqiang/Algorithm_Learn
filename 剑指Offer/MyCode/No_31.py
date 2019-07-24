'''
剑指 Offer 第31题 栈的压入、弹出序列
leetcode 946. Validate Stack Sequences
'''

def validate_stack_sequences(pushed, popped):
    if not pushed and not popped:
        return True
    if len(pushed) == 0 and len(popped) == 0:
        return True
    if not pushed or not popped or len(pushed) == 0 or len(popped) == 0:
        return False

    pop_idx, stack = 0, []
    for n in pushed:
        stack.append(n)
        while stack and stack[-1] == popped[pop_idx]:
            stack.pop()
            pop_idx += 1

    return len(stack) == 0


