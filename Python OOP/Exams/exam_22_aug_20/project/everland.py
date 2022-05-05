from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = sum(room.expenses + room.room_cost for room in self.rooms)
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                result += f'{room.family_name} paid {total_expenses}$ and have {room.budget}$ left.\n'
            else:
                result += f'{room.family_name} does not have enough budget and must leave the hotel.\n'
                self.rooms.remove(room)
        return result.strip()

    def status(self):
        total_people = 0
        result = f'Total population: {total_people}\n'
        for room in self.rooms:
            total_people += room.members_count
            result += f'{room.family_name} with {room.members_count} ' \
                      f'members. Budget: {room.budget}$, Expenses: {room.expenses:.2f}$\n'

            appliances = room.expenses
            if room.children:
                for i, value in enumerate(room.children):
                    result += f'--- Child {i} monthly cost: {value.get_monthly_expense()}$\n'
                    appliances += value.get_monthly_expense()

            result += f'--- Appliances monthly cost: {appliances:.2f}$\n'
        return result
