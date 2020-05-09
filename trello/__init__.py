# Include #

from .Trello import Trello, Board, List, Card

# Function #

class TrelloAPI(object):
    def __init__(self, Key, Token):
        self.API = Trello(Key, Token)

    def new(self, Type, Name, Parent=None):
        return self.API.new(Type, Name, Parent)
    
    def GetBoardByName(self, BoardName):
        return self.API.GetBoardByName(BoardName)

    def GetBoardById(self, BoardId):
        return self.API.GetBoardById(BoardId)