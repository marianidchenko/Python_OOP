from Retake_19_12_2020.project.medicine.medicine import Medicine


class Salve(Medicine):
    HEALTH_INCREASE = 50

    def __init__(self):
        super().__init__(Salve.HEALTH_INCREASE)