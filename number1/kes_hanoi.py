class InvalidMoveException(Exception): pass

class HanoiPillar:
    def __init__(self, high=0, unstackable=False, unmovable=False):
        self._stack = [i+1 for i in reversed(range(high))] if high >= 1 else []
        self.unstackable = unstackable
        self.unmovable = unmovable

    def __mul__(self, b):
        """ This is used to represent movement
        """
        if b.unstackable:
            raise InvalidMoveException("Cannot move disks to this pillar")
        if self.unmovable:
            raise InvalidMoveException("Cannot move disks off of this pillar")
        def check_order(a):
            for ii in range(len(a) - 1):
                if a[ii] < a[ii + 1]:
                    raise InvalidMoveException
                
        if len(b._stack) > 0:
            a_high = self._stack[0]
            b_high = self._stack[0]

        if len(self._stack) == 0:
            raise InvalidMoveException("No pillar to move")

        b._stack.append(self._stack.pop())
        check_order(self._stack)
        check_order(b._stack)

    def __repr__(self):
        return str(self._stack)

def hanoi5(S, A1, A2, A3, D, n):
    """ Steps:
            1: Move all disks to the second peg
            2: move all disks forward 2 pegs, we can treat the middle 3 pegs
               as a standard hanoi 3
            3: Move all disks to the last peg
    """
    def hanoi3(S, A, D, n):
        print(pillars)
        if n == 1:
            S * A
            A * D
        elif n >= 2:
            hanoi3(S, A, D, n-1)
            S * A
            hanoi3(D, A, S, n-1)
            A * D
            hanoi3(S, A, D, n-1)

    print(pillars)
    for i in range(n):
        hanoi3(A1, A2, A3, i)
        S * A1
        hanoi3(A3, A2, A1, i)
    hanoi3(A1, A2, A3, n)

    for i in reversed(range(n)):
        hanoi3(A3, A2, A1, i)
        A3 * D
        hanoi3(A1, A2, A3, i)
    print(pillars)
        

pillars = [HanoiPillar(5, unstackable=True), HanoiPillar(), HanoiPillar(),
           HanoiPillar(), HanoiPillar(unmovable=True)
          ]

if __name__ == '__main__':
    #using pillars as a global was the only way to print in the same order after
    #every call to the hanoi function
    print(pillars)
    S = pillars[0]
    A1 = pillars[1]
    A2 = pillars[2]
    A3 = pillars[3]
    D = pillars[4]

    hanoi5(S, A1, A2, A3, D, 5)








