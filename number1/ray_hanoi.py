class InvalidMoveException(Exception): pass

class HanoiPillar:
    def __init__(self, high=0):
        self._stack = [i+1 for i in reversed(range(high))] if high >= 1 else []

    def __mul__(self, b):
        """
            This is used to represent movement
        """
        def check_order(a):
            if any([a[i] < a[i+1] for i in range(len(a) - 1)]):
                raise InvalidMoveException

        b._stack.append(self._stack.pop())
        check_order(self._stack) # not sure why we need this
        check_order(b._stack)

        return b

    def __repr__(self):
        return str(self._stack)


def hanoi(t1, t2, t3, t4, t5, n):
    if n > 0:
        # TO-DO print pillars in right order
        hanoi(t1, t2, t3, t4, t5, n-1)
        t1 * t2 * t3 * t4
        hanoi(t5, t4, t3, t2, t1, n-1)
        t4 * t5
        hanoi(t1, t2, t3, t4, t5, n-1)


if __name__ == '__main__':
    n = 5
    P1 = HanoiPillar(n)
    P2 = HanoiPillar()
    P3 = HanoiPillar()
    P4 = HanoiPillar()
    P5 = HanoiPillar()

    print(P1, P2, P3, P4, P5)
    hanoi(P1, P2, P3, P4, P5, n)
    print(P1, P2, P3, P4, P5)





