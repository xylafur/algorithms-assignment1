from copy import deepcopy
import sys

class InvalidMoveException(Exception): pass

class HanoiPillar:
    """ Object that ensures no invalid moves are made in my algorithm
    """
    def __init__(self, disks=0, unstackable=False, unmovable=False):
        """ Constructor for HanoiPillar Object

            Params:
                disks <int>: Number of disks in the tower
                unstackable <bool>: Can we move disks onto this pillar?
                unmovable <bool>: Can we move disks off of this pillar?
        """
        self._stack = [i+1 for i in reversed(range(disks))] if disks >= 1 else []
        self.unstackable = unstackable
        self.unmovable = unmovable
        self.pritner = None

    def __mul__(self, b):
        """ This is used to represent movement, makes sure that all moves made
            are valid and also prints out all of the pillars on every movement.

            If we are trying to move a disk to a pillar that disks cannot be 
            moved to an exception will be thrown.  
            If we try to move disks off of a pillar that disks cannot be moved 
            off of, an Exception is thrown.  
            If we put a larger disk on top of a smaller disk an Exception is 
            thrown.  
            If there is not a disk on the pillar an exception is thrown.
        """
        if b.unstackable:
            raise InvalidMoveException("Cannot move disks to this pillar")
        if self.unmovable:
            raise InvalidMoveException("Cannot move disks off of this pillar")
        #helper function
        def check_order(a):
            for ii in range(len(a) - 1):
                if a[ii] < a[ii + 1]:
                    raise InvalidMoveException
                
        if len(b._stack) > 0:
            a_disks = self._stack[0]
            b_disks = self._stack[0]

        if len(self._stack) == 0:
            raise InvalidMoveException("No disk to move")

        b._stack.append(self._stack.pop())
        check_order(self._stack)
        check_order(b._stack)

        if self.printer:
            self.printer()

    def __repr__(self):
        """ Just for prettier output
        """
        return str(self._stack)

class PillarPrinter:
    """ Helper class that assists in outputting the pillars onto the screen
        Also acts as a counter for the total number of moves
    """
    def __init__(self, pillars, log=False):
        """ Constructor, assigns a printer object to all of the pillars (so 
            they can handle printing when a movement is made)
        """
        self.last_pillars = []
        self.pillars = pillars
        self.moves = 0
        for pillar in self.pillars:
            pillar.printer = self
        self.log = log
        self.logs = []

    def assign_printers(self, val):
        """ Helper function to assign all of this object's pillars printer
            property to a particular value
        """
        for pillar in self.pillars:
            pillar.printer = val

    def __call__(self):
        """ Function used to print out the output and increment the moves

            This function only prints out the pillars if they have changed since
            the last time this function was called.

            The Pillar's printer property is assigned to None before the deep
            copy to avoid infintie recursion
        """
        if self.last_pillars != self.pillars:
            result = "Move number: {}, Pillars: {}".format(self.moves, self.pillars)
            if not self.log:
                print(result)
            else:
                self.logs.append(result)
            self.assign_printers(None)
            self.last_pillars = deepcopy(self.pillars)
            self.assign_printers(self)
            self.moves += 1

    def print_100(self):
        length = len(self.logs)
        for ii, log in enumerate(self.logs):
            if ii < 100 or ii >= length - 100:
                print(log)

def hanoi5(S, A1, A2, A3, D, n, printer):
    """ Steps:
            Move all disks to the first peg.
                Do this by moving everything from A1 to A3 (which at the beginning
                should be nothing) Then move the top disk of S to A1, then move
                everything from A3 back to A1.  Repeat until S is empty.
            Treat the inner 3 pegs like a standard Hanoi 3, move everythnig to
            A3.
            Move all the disks to the last peg:
                So this by moving eevery disk but the bottom one from A3 to A1, 
                then move the bottom disk from A3 to D.  Then Move everyrthing 
                back from A1 to A3 and repeat until all of the disks are on D.
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

    for i in range(n):
        hanoi3(A1, A2, A3, i)
        S * A1
        hanoi3(A3, A2, A1, i)

    hanoi3(A1, A2, A3, n)

    for i in reversed(range(n)):
        hanoi3(A3, A2, A1, i)
        A3 * D
        hanoi3(A1, A2, A3, i)

if __name__ == '__main__':
    """ This is out main, first we have a simple check for input to see if there
        is a particular n that this program should be run with, if there is we
        use it, if not we use n = 3.  Then we create the Hanoi Pillar objects
        and the printer and call the Hanoi 5 function
    """
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 3

    S = HanoiPillar(n, unstackable=True)
    A1 = HanoiPillar()
    A2 = HanoiPillar()
    A3 = HanoiPillar()
    D = HanoiPillar(unmovable=True)

    printer = PillarPrinter([S, A1, A2, A3, D], log=True)

    printer()
    hanoi5(S, A1, A2, A3, D, n, printer)

    printer.print_100()
