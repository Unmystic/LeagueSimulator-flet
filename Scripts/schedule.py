import csv
import random


class Schedule:
    def __init__(self):
        self.teams = []

        comb = self.teamList()
        self.drawSchedule(comb)

    def teamList(self):
        with open("Scripts/data/teams.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["name", "rating"])
            for row in reader:
                self.teams.append(row["name"])

        return self.teams

    def first_draw(self,comb):
        n = int(len(self.teams) / 2)

        stages = []
        for i in range(len(self.teams) - 1):
            t = self.teams[:1] + self.teams[-i:] + self.teams[1:-i] if i else self.teams
            stages.append(list(zip(t[:n], reversed(t[n:]))))
        stages = self.tuple_conv(stages)

        for tour in stages:
            for game in tour:
                random.seed()
                x = random.choice([0, 1])
                if x:
                    game[0], game[1] = game[1], game[0]
        return stages

    def tuple_conv(self, stages):
        cel = []
        for tour in stages:
            tour = [list(elem) for elem in tour]
            cel.append(tour)

        return cel

    def second_draw(self, first):
        second = first.copy()
        for tour in second:
            for match in tour:
                match[0], match[1] = match[1], match[0]
        random.shuffle(second)
        return second

    def drawSchedule(self, comb):
        first = self.first_draw(comb)
        second = self.second_draw(first)

        with open("Scripts/data/schedule.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["tour", "homeTeam", "awayTeam"])
            for i in range(len(first)):
                for game in first[i]:
                    writer.writerow({"tour": i + 1, "homeTeam": game[0], "awayTeam": game[1]})
            for i in range(len(second)):
                for game in second[i]:
                    writer.writerow({"tour": i + len(self.teams), "homeTeam": game[0], "awayTeam": game[1]})