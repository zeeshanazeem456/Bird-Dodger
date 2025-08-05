class Leaderboard:
    def __init__(self, filename=r"C:\Users\4STAR\Downloads\Zeeshan's Stuff\Space_Dodger\leaderboard.txt"):
        self.filename = filename
        self.entries = []
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, score = line.strip().split(",")
                    self.entries.append((name, int(score)))
        except FileNotFoundError:
            pass 

    def add_entry(self, name, score):
        self.entries.append((name, score))
        self.entries.sort(key=lambda x: x[1], reverse=True)
        self.save()

    def save(self):
        with open(self.filename, "w") as file:
            for name, score in self.entries:
                file.write(f"{name},{score}\n")

    def get_leaderboard(self):
        return self.entries