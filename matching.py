import random

class Tile(object):
  def __init__(self,kind, name, imageurl):
    self.kind = kind
    self.name = name
    self.imageurl = imageurl

walrus = Tile("walrus", "walrus", "url")
babywalrus = Tile("walrus", "baby walrus", "url")
tiger = Tile("tiger", "tiger", "url")
babytiger = Tile("tiger", "baby tiger", "url")
narwhal = Tile("narwhal", "narwhal", "url")
babynarwhal = Tile("narwhal", "baby narwhal", "url")
orangutan = Tile("orangutan", "orangutan", "url")
babyorangutan = Tile("orangutan", "baby orangutan", "url")
robin = Tile("robin", "robin", "url")
babyrobin = Tile("robin", "baby robin", "url")
dog = Tile("dog", "dog", "url")
babydog = Tile("dog", "baby dog", "url")
iguana = Tile("iguana", "iguana", "url")
babyiguana = Tile("iguana", "baby iguana", "url")
cow = Tile("cow", "cow", "url")
babycow = Tile("cow", "baby cow", "url")

cards = [
walrus,
babywalrus, 
tiger,
babytiger,
narwhal,
babynarwhal,
orangutan,
babyorangutan,
robin,
babyrobin,
dog,
babydog,
iguana,
babyiguana,
cow,
babycow
]

# class Grid(object):
#   def __init__(cards):
#     self.cards = cards
#     self.selected = []

def play():
    selected = []
    # grid = random.sample(cards, len(cards))
    grid = cards
    while True:
        while True:
            i = int(raw_input("choose a numbered tile!"))
            if i not in selected:
                print "You picked %s" %grid[i-1].name
                break
            else:
                print "This number in unavailable, pick again."
                    
        while True: 
            k = int(raw_input("choose another numbered tile!"))
            if k == i:
                print "Sorry, you cannot guess the same tile twice."
            if i not in selected:
                print "You picked %s" %grid[k-1].name
                break
            else:
                print "This number in unavailable, pick again."

        if k != i and grid[i-1].kind == grid[k-1].kind:
            selected.append(k)
            selected.append(i)
            print "it's a match!"
            print selected
        else:
            if grid[i-1].kind != grid[k-1].kind:
                print "Sorry, these tiles aren't a match"
play()




  
    

