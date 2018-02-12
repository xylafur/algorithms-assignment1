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


def hanoi3(S,A,D, n, print_state):
    hanoi3(S,A,D, n-1):
    S * A
    print_state()
    hanoi3(D,A,S, n-1):
    A * S
    print_state()
    hanoi3(S,A,D, n-1):


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
            S, A, D = tuple(pillars)

            hanoi([S, A, D], n-1, print_state)
                # move n-1 disks from S to D

            S * A # move disk n from S to A
            print_state()

            hanoi([D, A, S], n-1, print_state)
                # move n-1 disks from D to S

            A * S # move disk n from A to S
            print_state()

            hanoi([t1, t2, t3], n-1, print_state)
                # move n-1 disks from S to D


        elif len(pillars) == 5: # acts like hanoi 5
            S, A1, A2, A3, D = tuple(pillars)

            hanoi([S, A1, A2, A3, A3], n-1, print_state)
                # move the n-1 disks from S to A3

            S * A1  # move disk n to A1

            if S != A1:
                print_state()

            A1 * A2 # move disk n to A2

            print_state()

            hanoi([A3, A2, A1], n-1, print_state)
                # move n-1 disks from A3 to A1

            A2 * A3 # move disk n from A2 to A3

            print_state()

            A3 * D  # move disk n from A3 to D

            if t4 != t5:
                print_state()

            hanoi([A1, A1, A2, A3, D], n-1, print_state)
                # move n-1 disks from A1 to D

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

