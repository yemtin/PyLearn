class Instrument():
   def make_sound(self):
    pass

class Erhu(Instrument):
    def make_sound(self):
       print('erhu is playing')
class Violin(Instrument):
    def make_sound(self):
        print('violin is playing')
class Piano(Instrument):
    def make_sound(self):
        print('piano is playing')

def play(instrument):
    Instrument.make_sound()
    
    if __name__=='_main_':
     play(Erhu())
     play(Violin())
     play(Piano())





