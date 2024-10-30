class Bowling:
    def __init__(self):
        self.throws = []

    def throw(self, pins_knocked_down: int) -> None:
        self.throws.append(pins_knocked_down)

    def score(self) -> int:
        total_score = 0
        throws_index = 0
        for _ in range(10):
            if self.is_strike(throws_index):
                total_score += 10 + self.get_strike_bonus(throws_index)
                throws_index += 1
            elif self.is_spare(self.get_total_pins_in_frame(throws_index)):
                total_score += 10 + self.get_spare_bonus(throws_index)
                throws_index += 2
            else:
                total_score += self.get_total_pins_in_frame(throws_index)
                throws_index += 2

        # 10 frame
        return total_score

    def get_spare_bonus(self, throws_index):
        return self.throws[throws_index + 2]

    def get_strike_bonus(self, throws_index):
        return self.throws[throws_index + 1] + self.throws[throws_index + 2]

    def is_strike(self, throws_index: int) -> bool:
        return self.throws[throws_index] == 10

    def is_spare(self, total_pins_knocked_down_in_frame):
        return total_pins_knocked_down_in_frame == 10

    def get_total_pins_in_frame(self, throws_index):
        return self.throws[throws_index] + self.throws[throws_index + 1]