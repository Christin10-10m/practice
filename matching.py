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

cards = [Tile('tiger', 'baby tiger', 'url'), 
Tile('walrus', 'baby walrus', 'url'), 
Tile('iguana', 'iguana', 'url'),
Tile('iguana', 'baby iguana', 'url'),
Tile('dog', 'dog', 'url'),
Tile('dog', 'baby dog', 'url')]

def play():
    selected = []
while True:
    grid = random.sample(cards, len(cards))
   #pick card, eventually: int(raw_input("choose a number!"))
    i = 6
    print "You picked %s" %grid[i-1].name 
    #pick  a second card, eventually: int(raw_input("choose another number!"))
    k = 5
    print "You picked %s" % grid[k-1].name
    # k cannot == i
    if k == i:
      print "Sorry, you cannot guess the same tile twice."
    if k != i and grid[i-1].kind == grid[k-1].kind:
    # later, after you have this working add x-1 and y-1 to selected list...
      print "it's a match!"
    else:
      if grid[i-1].kind != grid[k-1].kind:
        print "Sorry, these tiles aren't a match"
    break





  
    

