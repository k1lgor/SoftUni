class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    if (name := input()) == 'End':
        break
    party.people.append(name)
print(f"Going: {', '.join(party.people)}\nTotal: {len(party.people)}")
