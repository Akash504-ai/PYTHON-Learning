class Memento:
    def __init__(self, text):
        self.text = text

class Document:
    def __init__(self, text):
        self.text = text

    def save(self):
        return Memento(self.text)

    def restore(self, memento):
        self.text = memento.text

class History:
    def __init__(self):
            self.snapshots = [] 