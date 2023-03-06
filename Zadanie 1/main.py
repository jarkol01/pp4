# Funkcję obliczającą wartość ceny netto na podstawie przekazanych parametrów wartość ceny brutto oraz stawki podatku
def calculate_netto(brutto, podatek):
    return brutto / (1+podatek)

# Strukturę danych reprezentującą KOLEJKĘ FIFO
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
print(stack.pop(0))
print(stack)

# Procedurę dopisującą przekazany ciąg znaków jako nową linijkę do pliku
with open('tekst.txt', 'a') as file:
    file.write(input("Enter your text: ") + '\n')

# Obiekt reprezentujący Zajęcia który opisuje zachowanie zapiszStudenta oraz przestrzega reguły maksymalnie 10 studentów na zajęciach
class Zajecia():
    def __init__(self):
        self.studenci = []

    def zapisz_studenta(self, student):
        if len(self.studenci) < 10:
            self.studenci.append(student)
        else:
            print("Max amount of student!")
