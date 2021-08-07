from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumptions = 0
        for room in self.rooms:
            monthly_consumptions += room.expenses + room.room_cost
        return f"Monthly consumption: {monthly_consumptions:.2f}$."

    def pay(self):
        result = []
        rooms_to_remove = []
        for room in self.rooms:
            total_owed = room.expenses + room.room_cost
            if room.budget >= total_owed:
                room.budget -= total_owed
                result.append(f"{room.family_name} paid {total_owed:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(room)
        self.rooms = [x for x in self.rooms if x not in rooms_to_remove]
        return '\n'.join(result)

    def status(self):
        result = [f"Total population: {[x.members_count for x in self.rooms]}"]
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            for i, child in enumerate(room.children):
                result.append(f"--- Child {i} monthly cost: {child.cost*30:.2f}$")
            for appliance in room.appliances:
                result.append(f"--- Appliances monthly cost: {appliance.get_monthly_expenses():.2f}$")
        return '\n'.join(result)

