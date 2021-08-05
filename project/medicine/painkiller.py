from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    HEALTH_INCREASE = 20

    def __init__(self):
        self.health_increase = Painkiller.HEALTH_INCREASE
