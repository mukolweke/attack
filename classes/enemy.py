class Enemy:
    # hp->health mp->magic points
    def __init__(self, hp, mp):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp