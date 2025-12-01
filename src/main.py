from structures.list import ClueList
from structures.stack import ActionStack
from structures.queue import TestimonyQueue
from structures.graph import Graph
from structures.hashtable import HashTable

def main():
    print("=== Detective Quest ===")

    clues = ClueList()
    actions = ActionStack()
    testimonies = TestimonyQueue()
    locations = Graph()
    suspects = HashTable()

    # exemplo de pistas
    clues.add_clue(1, "Armazém", "Carlos", 4)
    clues.add_clue(2, "Praça", "Maria", 2)
    clues.add_clue(3, "Hotel", "Carlos", 5)

    # exemplo de depoimentos
    testimonies.enqueue("Carlos foi visto perto do hotel.")
    testimonies.enqueue("Maria estava nervosa na praça.")

    # exemplo de navegação
    locations.add_edge("Praça", "Hotel")
    locations.add_edge("Hotel", "Armazém")

    print("\nPistas registradas:")
    clues.print_clues()

    print("\nDepoimentos:")
    testimonies.print_all()

    print("\nMapa dos locais:")
    locations.print_graph()

    print("\nDeterminando suspeito principal...")
    guilty = clues.find_primary_suspect()
    print(f"Suspeito possivelmente culpado: {guilty}")

if __name__ == "__main__":
    main()
