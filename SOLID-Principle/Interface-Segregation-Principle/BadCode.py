from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        print(int(document) + 1)
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')



print("Calling Multi Functional Printer methods....")
multiFunc = MultiFunctionPrinter()
multiFunc.fax(123)  # nothing happens   
multiFunc.print(123)
multiFunc.scan(123)

print("Calling Old Fashioned Printer methods....")
printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.print(123)
printer.scan(123)  # oops!