import random

class notes_system():
    def __init__(self):
        #G keys
        self.notes_list = ['1G','1A','1B','C','D','E','F','G','A','B','C1','D1','E1','F1','G1','A1','B1','C2','D2']
        self.simp_notes_list = ['G','A','B','C','D','E','F','G','A','B','C','D','E','F','G','A','B','C','D']
        self.keyboard_notes = ['j','k','l','a','s','d','h','j','k','l','a','s','d','h','j','k','l','a','s']

        self.notes_1 = self.random_note()
        self.notes_2 = self.random_note()

        #normal 3->14(+1)
        #complete 0->18(+1)
        #if note less or equal to index 3, make 1 suplementary line bellow, if its less or igual to 1, make another one
        #if its more or equal to index 15 create 1 suplementary line above, if its more or iqual no index 17, make another one

    def random_note(self):
        rand = random.randrange(0, 19)
        sup = 0
        rev = False
        if rand <= 3:
            sup = -1
            if rand <=1:
                sup = -2

        if rand >= 15:
            sup = 1
            if rand >= 17:
                sup = 2
            
        if rand > 9:
            rev = True


        return [rand, sup, rev]

    def random_key(self):
        rand = random.randrange(1,3)

        return rand
    
    def verify_note(self, asw, quest):
        asw_index = self.keyboard_notes.index(asw)
        final_asw = self.simp_notes_list[asw_index]
        
        if final_asw == self.simp_notes_list[quest]:
            return True
        else:
            return False

notes_system()