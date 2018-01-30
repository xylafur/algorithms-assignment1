class InvalidMoveException(Exception): pass

class HanoiPillar:
    def __init__(self, high=0):
        self._stack = [i+1 for i in reversed(range(high))] if high >= 1 else []

    def __mul__(self, b):
        """
            This is used to represent movement
        """
        if self._stack == b._stack:
            return self
        if len(self._stack) == 0:
            raise InvalidMoveException

        def check_order(a):
            if any([a[i] < a[i+1] for i in range(len(a) - 1)]):
                raise InvalidMoveException

        b._stack.append(self._stack.pop())
        check_order(self._stack) # not sure why we need this
        check_order(b._stack)

        return b

    def __repr__(self):
        return str(self._stack)



n = 10
P1 = HanoiPillar(n)
P2 = HanoiPillar()
P3 = HanoiPillar()
P4 = HanoiPillar()
P5 = HanoiPillar()

def hanoi(pillars, n):
    if n > 0:
        if len(pillars) == 3:
            t1, t2, t3 = tuple(pillars)
            hanoi([t1, t2, t3], n-1)

            t1 * t2
#            print(P1, P2, P3, P4, P5)

            hanoi([t3, t2, t1], n-1)

            t2 * t3
#            print(P1, P2, P3, P4, P5)

            hanoi([t1, t2, t3], n-1)

        elif len(pillars) == 5:
            t1,t2,t3,t4,t5 = tuple(pillars)

            hanoi([t1, t2, t3, t4, t4], n-1)

            t1 * t2 * t3
#            print(P1, P2, P3, P4, P5)

            hanoi([t4, t3, t2], n-1)

            t3 * t4 * t5
#            print(P1, P2, P3, P4, P5)

            hanoi([t2, t2, t3, t4, t5], n-1)




print('Initial state:\n', P1, P2, P3, P4, P5)
print('Running hanoi\n')
hanoi([P1, P2, P3, P4, P5], n)
print(P1, P2, P3, P4, P5)


