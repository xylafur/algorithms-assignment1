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
        else:
            raise InvalidMoveException("No pillar to move")
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

def hanoi_5(S, A1, I, A2, D, n):
    """ This problem can really be viewed as two hanoi3 problems as shown below 
        | | | | |
        1 2 3
            1 2 3

        so first we will move all disks from S to I, then from I to D
    """
    def hanoi3(S, A, D, n):
        if n == 1:
            S * A
            A * D
        elif n >= 2:
            hanoi3(S, A, D, n-1)
            S * A
            hanoi3(D, A, S, n-1)
            A * D
            hanoi3(S, A, D, n-1)
    hanoi3(S, A1, I, n)
    hanoi3(I, A2, D, n)

def hanoi5(S, A1, A2, A3, D, n):
    """ Steps:
            1: Move all disks to the second peg
            2: move all disks forward 2 pegs, we can treat the middle 3 pegs
               as a standard hanoi 3
            3: Move all disks to the last peg
    """
    def move1(S, D, A2, A3, n, move_from_d=True):
        """ Inner function where we want to move all of the disks from S to D
            (which we assume is right next to S)
        """
        pass
    def move3(S, A, D, n):
        pass
    move1(S, A1, A2, A3, n)
    move3(A1, A2, A3, n)
    move1(A3, D, A2, A1, n, move_from_d=False)


            

if __name__ == '__main__':
    S = HanoiPillar(3)
    A1 = HanoiPillar()
    A2 = HanoiPillar()
    A3 = HanoiPillar()
    D = HanoiPillar()
    hanoi5(S, A1, A2, A3, D, 3)








