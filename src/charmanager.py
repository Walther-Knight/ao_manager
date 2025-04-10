import math

#character node defaults to human
#may rework into species based later
class CharacterNode:
    def __init__(self, name=None, str=12, agi=12, con=12, vit=12, dis=12, int=12, cha=12, cdp=500, species="human"):
        if name == None:
            self.name = "Default Character"
        else:
            self.name = name
        
        #set primary quality variables
        self.str = str
        self.agi = agi
        self.con = con
        self.vit = vit
        self.dis = dis
        self.int = int
        self.cha = cha
        #setup cdp tracking dictionary
        self.cdp_dict = {"Input CDP": cdp}
        self.species = species

        #derive secondary qualities
        self.athl = math.ceil((self.str + self.agi)/2)
        self.phac = math.ceil((self.agi + self.con)/2)
        self.fitn = math.ceil((self.con + self.vit)/2)
        self.will = math.ceil((self.vit + self.dis)/2)
        self.wisd = math.ceil((self.dis + self.int)/2)
        self.wit = math.ceil((self.int + self.cha)/2)
        self.pres = math.ceil((self.cha + self.str)/2)

        #derive tertiary
        self.reaction = math.ceil((self.athl + self.wisd)/2)
        self.physis = round((self.str + self.agi + self.con + self.vit + self.dis + self.int + self.cha)/7)
        self.endurance = self.con + self.dis
        self.health = self.con + self.vit
        self.defense = math.ceil(self.reaction / 2)
        self.moverate = self._calc_move_rate()

    #calculate movement rate
    def _calc_move_rate(self):
        if not self.athl:
            return Exception("Althleticism value not calculated or passed!")
        if self.athl < 6:
            return {"Swim": 0, "Crawl": 0, "Monkey Run": 0, "Walk": 1, "Run": 1, "Sprint": 2, "Flying": 2}
        elif self.athl < 11:
            return {"Swim": 1, "Crawl": 1, "Monkey Run": 1, "Walk": 1, "Run": 2, "Sprint": 3, "Flying": 6}
        elif self.athl < 16:
            return {"Swim": 1, "Crawl": 2, "Monkey Run": 2, "Walk": 2, "Run": 3, "Sprint": 6, "Flying": 10}
        elif self.athl < 21:
            return {"Swim": 2, "Crawl": 2, "Monkey Run": 3, "Walk": 3, "Run": 4, "Sprint": 8, "Flying": 14}
        elif self.athl < 31:
            return {"Swim": 1, "Crawl": 3, "Monkey Run": 4, "Walk": 4, "Run": 6, "Sprint": 12, "Flying": 18}
        elif self.athl < 41:
            return {"Swim": 3, "Crawl": 3, "Monkey Run": 4, "Walk": 4, "Run": 8, "Sprint": 16, "Flying": 22}
        elif self.athl < 51:
            return {"Swim": 4, "Crawl": 4, "Monkey Run": 6, "Walk": 6, "Run": 10, "Sprint": 20, "Flying": 26}
        elif self.athl < 61:
            return {"Swim": 4, "Crawl": 6, "Monkey Run": 6, "Walk": 6, "Run": 12, "Sprint": 24, "Flying": 30}
        elif self.athl < 71:
            return {"Swim": 6, "Crawl": 6, "Monkey Run": 8, "Walk": 8, "Run": 14, "Sprint": 28, "Flying": 34}
        elif self.athl < 81:
            return {"Swim": 6, "Crawl": 8, "Monkey Run": 10, "Walk": 10, "Run": 20, "Sprint": 32, "Flying": 40}
        elif self.athl < 91:
            return {"Swim": 8, "Crawl": 10, "Monkey Run": 12, "Walk": 12, "Run": 24, "Sprint": 36, "Flying": 45}
        elif self.athl <= 100:
            return {"Swim": 12, "Crawl": 14, "Monkey Run": 16, "Walk": 16, "Run": 30, "Sprint": 40, "Flying": 50}
        
    def print_attributes(self):
        print(f"Primary Qualities:\nStrength: {self.str}\nAgility: {self.agi}\nConditioning: {self.con}\nVitality: {self.vit}\nDiscipline: {self.dis}\nIntelligence: {self.int}\nCharisma: {self.cha}\n")
        print(f"Secondary Qualities:\nAthleticism: {self.athl}\nPhysical Acumen: {self.phac}\nFitness: {self.fitn}\nWill: {self.will}\nWisdom: {self.wisd}\nWit: {self.wit}\nPresence: {self.pres}\n")
        print(f"Tertiary Qualities:\nReaction: {self.reaction}\nPhysis: {self.physis}\nDefense Rating: {self.defense}")

    def print_move_rate(self):
        print(f"Movement Rates:\n{self.moverate}")