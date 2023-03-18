from dataclasses import dataclass

@dataclass
class Positional:
    x: int
    y: int

@dataclass
class Scroll:
    title: int
    topics: set[int]
    content: str

    def has_topic(self, topic):
        return topic in self.topics

    __next_title = 0
    @classmethod
    def unique_title(self):
        __next_title += 1
        return __next_title

class Actor:

    def __init__(self, parent = None):
        self.parent = parent

    def step():
        pass

    def reparent(parent):
        self.parent = parent

class Scene(Actor):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.children = set()

    def __iadd__(self, obj):
        self.children.add(obj)
        obj.reparent(self)
        return self

    def step(self):
        for x in self.children:
            x.step()

class Closter(Scene, Positional):

    def __init__(self, x, y, parent = None):
        super(Scene, self).__init__(parent)
        super(Positional, self).__init__(x, y)
        self.owned_scrolls = set()
        self.available_scrolls = set()
        self.desired_topics = set()
        self.copy_orders = set()

    def __iadd__(self, obj):
        if isinstance(obj, Scroll):
            self.owned_scrolls.add(obj)
            self.available_scrolls.add(obj)
        else:
            super().__iadd__(obj)

