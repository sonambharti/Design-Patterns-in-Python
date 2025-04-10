from abc import ABC, abstractmethod


# Interface 1: Printer
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


# Interface 2: Scanner
class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


# Concrete implementation: A simple printer
class MyPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")


# Concrete implementation: A simple scanner
class MyScanner(Scanner):
    def scan(self, document):
        print(f"Scanning: {document}")


# Combined Interface (multi-function device)
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


# Concrete multi-function machine using composition
class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


# ------------------------
# ✅ Executing the code
# ------------------------

if __name__ == "__main__":
    # Create separate components
    printer = MyPrinter()
    scanner = MyScanner()

    # Combine them into a multi-function machine
    mfd = MultiFunctionMachine(printer, scanner)

    # Use the device
    mfd.print("ISP_Report.pdf")
    mfd.scan("ISP_Report.pdf")
