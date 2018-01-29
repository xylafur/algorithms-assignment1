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

        return b

    def __repr__(self):
        return str(self._stack)

def hanoi(t1, t2, t3, t4, t5, n):
    if n:
        hanoi(t1, t2, t3, t4, t5, n-1)
        t1 * t2 * t3 * t4
        hanoi(t5, t4, t3, t2, t1, n-1)
        t4 * t5
        hanoi(t1, t2, t3, t4, t5, n-1)


if __name__ == '__main__':
    n = 100
    t1 = HanoiPillar(n)
    t2 = HanoiPillar()
    t3 = HanoiPillar()
    t4 = HanoiPillar()
    t5 = HanoiPillar()

    print(t1, t2, t3, t4, t5)
    hanoi(t1, t2, t3, t4, t5, n)
    print(t1, t2, t3, t4, t5)





