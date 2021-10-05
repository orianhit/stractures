from dataclasses import dataclass


@dataclass
class node:
    isValid: bool


def stack():
    return []


def isRedandent(A, n):
    s = stack()
    for i in range(n):
        if A[i] == '(':
            s.append(node(False))
        if A[i] in ['+', '-', '*', ':']:
            if s:
                t = s.pop() # only added code
                t.isValid = True
                s.append(t)
        if A[i] == ')':
            t = s.pop()
            if (not t.isValid):
                return False
    return True


validEquation = list('(2+3)*((4+5)*2)')

print(f"validEquation returned - {isRedandent(validEquation, len(validEquation))}")

invalidEquation = list('(2+3)*(((4+5))*2)')

print(f"invalidEquation returned - {isRedandent(invalidEquation, len(invalidEquation))}")
