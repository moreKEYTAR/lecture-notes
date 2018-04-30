

# from lecture notes...Basic tree

class Node(object):

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):

        return "<Node {}>".format(self.data)


dumble = Node("Dumbledore", [])
print dumble