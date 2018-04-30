"""
Where python lists are inefficient, stacks and queues help.

QUEUE
Items enqueued at the back, dequeued at the front. Older items
are near the front. (horizontal language) FIFO.
Buffers, caches, task list
Methods for queues:
- enqueue / push
- dequeue / pop
- peek (for item that will be removed next)
- is_empty

>>> my_line = Queue()
>>> my_line.enqueue("Abby")
>>> my_line.enqueue("Bobby")
>>> my_line.enqueue("Carla")
>>> my_line.enqueue("Desmond")
>>> my_line.enqueue("Elinor")
>>> my_line.dequeue()
Abby is removed from queue.
>>> my_line.peek()
'Bobby'
>>> my_line.is_empty()
False


STACK
Items are pushed onto the top. Items are removed by popping off the top.
(vertical language) LIFO
The "top" can be the end of the list.
Error tracebacks in Python, balancing parentheses (nearest match), functions
calling functions, undo or back
Methods for stacks:
- push
- pop
- peek
- is_empty

>>> card_stack = Stack()
>>> card_stack.push("Ace of Hearts")
>>> card_stack.push("5 of Clubs")
>>> card_stack.pop()
5 of Clubs is removed from stack.
>>> card_stack.push("Ace of Clubs")
>>> card_stack.peek()
'Ace of Clubs'
>>> card_stack.pop()
Ace of Clubs is removed from stack.
>>> card_stack.pop()
Ace of Hearts is removed from stack.
>>> card_stack.is_empty()
True

"""

class Queue(object):

    def __init__(self):
        self._queue = []  # ._queue is all data in the queue

    def enqueue(self, item):
        self._queue.append(item)
        # print item, "is added to queue."

    def dequeue(self):
        popped = self._queue.pop(0)  # not a great implementation
        print popped, "is removed from queue."

    def peek(self):
        return self._queue[0]

    def is_empty(self):
        return not self._queue  # Returns true if IS empty


class Stack(object):

    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        popped = self._stack.pop()
        print popped, "is removed from stack."

    def peek(self):
        return self._stack[-1]  # will be an issue (index error)

    def is_empty(self):
        return not self._stack

# collections library is built for more efficient runtime than lists
# though linked lists are also a better option...
# Here is a double entded queue, or DEQUE...
import collections
my_deque = collections.deque()
my_deque.append("This")
my_deque.append("is")
my_deque.append("a")
my_deque.append("sentence.")
print my_deque  # (['This', 'is', 'a', 'sentence.'])
my_deque.pop()
print my_deque  # (['This', 'is', 'a'])
my_deque.popleft()
print my_deque  # (['is', 'a'])
my_deque.pop()
print my_deque  # (['is'])

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\nALL TESTS PASSED.\n"
