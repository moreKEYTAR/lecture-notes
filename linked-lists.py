"""
Linked lists store information in non-consecutive memory.
LLs can rearrange without other items having to "move"
Pointers are explicit, and also not stored consecutively
No indices. Nodes reference each other.
Nodes have at least these attributes:
- data
- next
- prev / previous (sometimes)

The LL class attributes are:
- head
- tail (sometimes)

The LL methods often include:
- print
- search ll and find node with specific data value
- add a node after a given node/position
- append to the ll
- remove a node

The node class is separate from the LL class.

>>> rock = Node("rock")
>>> paper = Node("paper", rock)
>>> scissors = Node("scissors", paper)
>>> rock.next = scissors
>>> scissors.next.data
'paper'

>>> game = LinkedList()
>>> game.head = rock
>>> game.head.data
'rock'
>>> game.head.next.data
'scissors'
>>> game.print_nodes()
rock
scissors
paper

"""


class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # we have not handled the self.next.data if there
                            # is no next
        # >>> print paper
        # <__main__.Node object at 0x7fcb17c1f890>


class LinkedList(object):

    def __init__(self):
        self.head = None

    def print_nodes(self):

        current = self.head
        seen = set()  # my adjustment for my specific circular list

        while current is not None:
            if current.data in seen:
                break
            else:
                seen.add(current.data)
                print current.data
                current = current.next

    def find_node(self, data):  # does not work for circular list

        current = self.head

        while current is not None:
            if current.data == data:
                return True
        return False



if __name__ == "__main__":
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print "\nALL TESTS PASSED.\n"
