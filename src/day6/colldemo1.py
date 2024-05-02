import collections

Card =  collections.namedtuple('Card',['rank','suit'])


class Deck:
    ranks=[  str(n)  for n in range (2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
            self.cards=[Card(rank,suit) for suit in self.suits
                                    for rank in self.ranks]
            print('Deck initialized')
        
    def __len__(self):
           print('length of deck')
           return len(self.cards)
    
    def __getitem__(self,position):
          return self.cards[position]
    


deck = Deck()
print(deck.__len__())

print(deck.__getitem__(1))


   