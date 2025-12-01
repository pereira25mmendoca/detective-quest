class ClueList:
    def __init__(self):
        self.clues = []

    def add_clue(self, id, location, suspect, importance):
        self.clues.append({
            "id": id,
            "location": location,
            "suspect": suspect,
            "importance": importance
        })

    def print_clues(self):
        for c in self.clues:
            print(f"[{c['id']}] {c['location']} — Suspeito: {c['suspect']} (importância {c['importance']})")

    def find_primary_suspect(self):
        count = {}
        for c in self.clues:
            if c["suspect"] not in count:
                count[c["suspect"]] = 0
            count[c["suspect"]] += 1

        return max(count, key=count.get)
