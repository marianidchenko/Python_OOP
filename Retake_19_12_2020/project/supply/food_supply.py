from Retake_19_12_2020.project.supply.supply import Supply


class FoodSupply(Supply):
    NEEDS_INCREASE = 20

    def __init__(self):
        super().__init__(FoodSupply.NEEDS_INCREASE)

