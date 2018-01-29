class InvalidMoveException(Exception): pass

class HanoiPillar:
    def __init__(self, high=0):
        self._stack = [i+1 for i in reversed(range(high))] if high >= 1 else []

    def __mul__(self, b):
        """ This is used to represent movement
        """
        def check_order(a):
            for ii in range(len(a) - 1):
                if a[ii] < a[ii + 1]:
                    raise InvalidMoveException
                
        if len(b._stack) > 0:
            a_high = self._stack[0]
            b_high = self._stack[0]
        b._stack.append(self._stack.pop())
        check_order(self._stack)
        check_order(b._stack)

    def __repr__(self):
        return str(self._stack)

def hanoi(S, A, D, n):
    if n == 1:
        S * D
    if n >= 2:
        hanoi(S, D, A, n-1)
        S * D
        hanoi(A, S, D, n-1)

if __name__ == '__main__':
    S = HanoiPillar(3)
    A = HanoiPillar()
    D = HanoiPillar()
    print(S, A, D)
    hanoi(S, A, D, 3)
    print(S, A, D)








