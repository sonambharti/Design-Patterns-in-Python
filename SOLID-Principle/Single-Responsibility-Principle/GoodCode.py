class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP
    # def save(self, filename):
    #     file = open(filename, "w")
    #     # file = open(filename, "a")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    # creating new common class for saving files of each class
    # def save_to_file(self, journal, filename):
    #     file = open(filename, "w")
    #     file.write(str(journal))
    #     file.close()
    
    
    # f you don't need an instance of PersistenceManager to call save_to_file, make it a staticmethod
    @staticmethod
    def save_to_file(journal, filename):  # No self needed
        with open(filename, "w") as file:
            file.write(str(journal))


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

file = r'../../temp/journal.txt'
# j.save(file)
# Now, we can call it without creating an instance:
# PersistenceManager.save_to_file(j, file)
p = PersistenceManager()
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())


