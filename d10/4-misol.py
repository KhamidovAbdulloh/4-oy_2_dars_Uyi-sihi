class Bowling:
    def __init__(self):
        self.frames = [[] for _ in range(10)]
        self.current_frame = 0
        self.current_roll = 0

    def roll(self, pins):
        if self.current_frame == 9:
            self.roll_last_frame(pins)
        else:
            if pins < 0 or pins > 10:
                raise ValueError("Pins should be between 0 and 10")
            if self.current_roll == 0 and pins == 10:
                self.frames[self.current_frame].append(10)
                self.current_frame += 1
            elif self.current_roll == 1 and self.frames[self.current_frame][-1] + pins == 10:
                self.frames[self.current_frame].append(pins)
                self.current_frame += 1
            elif self.current_roll == 1:
                self.frames[self.current_frame].append(pins)
                self.current_frame += 1
            else:
                self.frames[self.current_frame].append(pins)
            self.current_roll = (self.current_roll + 1) % 2

    def roll_last_frame(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins should be between 0 and 10")
        if len(self.frames[9]) == 0 and pins == 10:
            self.frames[9].append(10)
        elif len(self.frames[9]) == 1 and self.frames[9][0] + pins == 10:
            self.frames[9].append(pins)
        elif len(self.frames[9]) == 2:
            if self.frames[9][0] + self.frames[9][1] >= 10 and pins == 10:
                self.frames[9].append(10)
            else:
                self.frames[9].append(pins)
        else:
            self.frames[9].append(pins)

    def score(self):
        total_score = 0
        frame_index = 0
        for frame in self.frames:
            if len(frame) == 0:
                break
            if len(frame) == 1:
                total_score += sum(frame)
                if frame_index < 9 and sum(frame) == 10:
                    total_score += sum(self.frames[frame_index+1][:2])
                    if frame_index < 8 and self.frames[frame_index+1][0] == 10:
                        total_score += self.frames[frame_index+2][0]
            elif len(frame) == 2:
                total_score += sum(frame)
                if frame_index < 9 and sum(frame) == 10:
                    total_score += self.frames[frame_index+1][0]
            elif len(frame) == 3:
                total_score += sum(frame)
            frame_index += 1
        return total_score

game = Bowling()
game.roll(10)
game.roll(5)
game.roll(5)
game.roll(9)
game.roll(0)
print(game.score()) # 48