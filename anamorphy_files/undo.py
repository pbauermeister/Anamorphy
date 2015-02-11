"""
This class implements a generic Undo/Redo stack.  Because it only
holds parameters (supposed to remain small in size), there is no
limitation.
"""

import copy

DEBUG = False


class Undo(object):

    def __init__(self, capacity=1000, make_copy=True):
        self.stack = []
        self.index = -1
        self.capacity = capacity
        self.enabled = True
        self.make_copy = make_copy
        self.dbg_cntr = 0

    def add(self, item):
        if not self.enabled:
            return
        if self.index < -1:
            # remove forward history
            self.stack = self.stack[:self.index + 1]
            self.index = -1
        if self.make_copy:
            item = copy.deepcopy(item)
        self.stack.append(item)  # add item
        self.stack = self.stack[-self.capacity:]  # limit size
        self.debug("add")

    def fixup(self, fn):
        """
        Apply fn() on every item
        """
        self.stack = [fn(i) for i in self.stack]

    def enable(self, enabled):
        self.enabled = enabled

    def undo(self):
        if self.canUndo():
            self.index -= 1
            res = self.stack[self.index]
            if self.make_copy:
                res = copy.deepcopy(res)
        else:
            res = None
        self.debug("undo")
        return res

    def redo(self):
        if self.canRedo():
            self.index += 1
            res = self.stack[self.index]
            if self.make_copy:
                res = copy.deepcopy(res)
        else:
            res = None
        self.debug("redo")
        return res

    def canUndo(self):
        return len(self.stack) > -self.index

    def canRedo(self):
        return self.index < -1

    def debug(self, action):
        if DEBUG:
            self.dbg_cntr += 1
            print
            print "%d: %s>" % (self.dbg_cntr, action)
            for i in range(len(self.stack)):
                print ">>>", i, ":", self.stack[i]
            print "===", self.index, ":", self.stack[self.index]

if __name__ == "__main__":
    u = Undo(4)
    while 1:
        print
        print u.stack
        if u.canUndo():
            print "(u)",
        if u.canRedo():
            print "(r)",
        print "u/r/NUM :",
        v = raw_input()
        if v == "u":
            print "==>", u.undo()
        elif v == "r":
            print "==>", u.redo()
        else:
            u.add(v)
