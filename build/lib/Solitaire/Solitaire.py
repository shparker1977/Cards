from Deck import Deck

class Solitaire:
    def __init__(self):
        self.deck = Deck.Deck()
        self.deck.shuffle()
        self.end_stacks = {'H': [], 'D': [], 'S': [], 'C': []}
        self.row = []

        for x in range(7):
            row = []
            for i in range(x + 1):
                row.append(self.deck.deal())
            self.row.append(row)        

    def display_hand(self):
        print(self.row)

    def add_to_rank_stack(self, card):
        suit, rank = convert_card_to_rank_suit(card)
        if rank == len(self.end_stacks[rank]) + 1:
            self.end_stacks[rank].append(card)

    def move_card_from_row(self, card_to_move, card_to_move_to):
        # Check if moveto location is accurate
        # If card to move is different suit and one less it's ok
        pass
            
        # If not legal return "Not Leagal"
        
    def convert_card_to_rank_suit(card):
        rank, suit = card
        if rank == 'J':
            rank = 10
        elif rank == 'Q':
            rank = 11
        elif rank == 'K':
            rank = 12
        elif rank == 'A':
            rank = 1

        return(suit, rank)
        
    def check_if_game_won(self):
        # Add check for length of stacks each should be 13 long
        for stack in self.end_stacks:
            if len(stack) != 13:
                return 0
            suit, rank = convert_card_to_rank_suit(stack[-1:])
            if rank != 12:
                return 0
        return 1

