from dslink.DSLink import DSLink, Configuration, Node


class LargeNodeStructure(DSLink):
    def __init__(self):
        super().__init__(Configuration("python-large", responder=True, requester=True))
        for x in range(0, 99999):
            first = Node("Test%i" % x, self.super_root)
            for y in range(0, 10):
                second = Node("Test%i" % y, first)
                second.set_type("number")
                second.set_value(y)
                first.add_child(second)
            self.super_root.add_child(first)

if __name__ == "__main__":
    LargeNodeStructure()