# Memento: stores a snapshot
class Memento:
    def __init__(self, text):
        self.text = text


# Originator: the object whose state is saved
class Document:
    def __init__(self, text):
        self.text = text

    def save(self):
        return Memento(self.text)

    def restore(self, memento):
        self.text = memento.text


# Caretaker: stores snapshots
class History:
    def __init__(self):
        self.snapshots = []

    def save(self, memento):
        self.snapshots.append(memento)

    def undo(self):
        if self.snapshots:
            return self.snapshots.pop()

        return None


# Usage
document = Document("Hello")
history = History()

# Save the first state
history.save(document.save())

# Modify the document
document.text = "Hello World"
print(document.text)

# Undo
memento = history.undo()

if memento:
    document.restore(memento)

print(document.text)