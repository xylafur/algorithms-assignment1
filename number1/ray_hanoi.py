class InvalidMoveException(Exception): pass

class HanoiPillar:
    def __init__(self, high=0):
        self._stack = [i+1 for i in reversed(range(high))]\
                      if high >= 1 else []

    def __mul__(self, b):
        # overloaded multiplication operator for disk movement
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


def hanoi(pillars, n, print_state):
    """
        This function solves towers of hanoi
        for 5 pegs with edges:
            S -> A1 <-> A2 <-> A3 -> D

        Parameters:
            pillars     - list of HanoiPillar objects in order
                          to be traversal
            n           - number disks to move
            print_state - function pointer for state printing

    """
    if n > 0:
        if len(pillars) == 3: # acts like hanoi 3
            t1, t2, t3 = tuple(pillars)

            hanoi([t1, t2, t3], n-1, print_state)
                # recursive call 1

            t1 * t2
            print_state()

            hanoi([t3, t2, t1], n-1, print_state)
                # recursive call 2

            t2 * t3
            print_state()

            hanoi([t1, t2, t3], n-1, print_state)
                # recursive call 3

        elif len(pillars) == 5: # acts like hanoi 5
            t1,t2,t3,t4,t5 = tuple(pillars)

            hanoi([t1, t2, t3, t4, t4], n-1, print_state)
                # recursive call 1

            t1 * t2
            if t1 != t2:
                print_state()

            t2 * t3
            print_state()

            hanoi([t4, t3, t2], n-1, print_state)
                # recursive call 2

            t3 * t4
            print_state()

            t4 * t5
            if t4 != t5:
                print_state()

            hanoi([t2, t2, t3, t4, t5], n-1, print_state)
                # recursive call 3

def Main():
    n = 0
    while n <= 0:
        n = int(input('Enter n : '))

    P1 = HanoiPillar(n)
    P2 = HanoiPillar()
    P3 = HanoiPillar()
    P4 = HanoiPillar()
    P5 = HanoiPillar()

    def print_state():
        print('S:{}, A1:{}, A2:{}, A3:{}, D:{}'
              .format(P1, P2, P3, P4, P5))

    print_state()
    hanoi([P1, P2, P3, P4, P5], n, print_state)

if __name__=='__main__':
    Main()

