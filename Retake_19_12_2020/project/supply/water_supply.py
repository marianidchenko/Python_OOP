from Retake_19_12_2020.project.supply.supply import Supply


class WaterSupply(Supply):
    NEEDS_INCREASE = 40

    def __init__(self):
        super().__init__(WaterSupply.NEEDS_INCREASE)
