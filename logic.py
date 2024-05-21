import random
import mido
import time


class notes_system():
    def __init__(self):
        #G keys
        self.notes_list = ['1G','1A','1B','C','D','E','F','G','A','B','C1','D1','E1','F1','G1','A1','B1','C2','D2']
        self.simp_notes_list = ['G','A','B','C','D','E','F','G','A','B','C','D','E','F','G','A','B','C','D']
        
        self.keyboard_notes = ['j','k','l','a','s','d','h','j','k','l','a','s','d','h','j','k','l','a','s']

        self.notes_list_F = ['2B','2C','1D','1E','1F','1G','1A','1B','C','D','E','F','G','A','B','C1','D1','E1','F1']
        self.simp_notes_list_F = ['B','C','D','E','F','G','A','B','C','D','E','F','G','A','B','C','D','E','F']

        self.keyboard_notes_F = ['l','a','s','d','h','j','k','l','a','s','d','h','j','k','l','a','s','d','h']

        #normal 3->14(+1)
        #complete 0->18(+1)
        #if note less or equal to index 3, make 1 suplementary line bellow, if its less or igual to 1, make another one
        #if its more or equal to index 15 create 1 suplementary line above, if its more or iqual no index 17, make another one

    def random_note(self, extras=False):
        if extras == True:
            key = random.randrange(0,2)
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
            
            
        elif extras == False:
            key = random.randrange(0,2)
            rand = random.randrange(4, 15)
            sup = 0
            rev = False

            if rand > 9:
                rev = True
            
        if key == 0:
            key = 'g'
        elif key == 1:
            key = 'f'


        return [rand, sup, rev, key]

    def random_key(self):
        rand = random.randrange(1,3)

        return rand
    
    def verify_note(self, asw, quest, type_key='g'):
        if type_key == 'g':
            asw_index = self.keyboard_notes.index(asw)
            final_asw = self.simp_notes_list[asw_index]
            
            if final_asw == self.simp_notes_list[quest]:
                return True
            else:
                return False
        elif type_key == 'f':
            print('Enter f key')
            asw_index = self.keyboard_notes_F.index(asw)
            final_asw = self.simp_notes_list_F[asw_index]
            #print(f'quest:{quest}\nasw:{asw}\ntype_key: {type_key}\nasw_index:{asw_index}\nfinal_asw:{final_asw}')
            if final_asw == self.simp_notes_list_F[quest]:
                return True
            else:
                return False

class SfxAudio:
    def __init__(self):
        self.output = mido.open_output()  
        self.notes = {
            'C': 60,
            'D': 62,
            'E': 64,
            'F': 65,
            'G': 67,
            'A': 69,
            'B': 71
        }

    def play_note(self, note):
        note_number = self.notes[note]
        on_message = mido.Message('note_on', note=note_number, velocity=127)
        off_message = mido.Message('note_off', note=note_number, velocity=127)
        self.output.send(on_message)
        time.sleep(0.5)  
        self.output.send(off_message)

    def close(self):
        self.output.close()