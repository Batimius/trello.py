# Import #

import requests
import json

# Tables #

Headers = {
   "Accept": "application/json"
}

# Classes #

class Trello:
    def __init__(self, Key, Token):
        self.__AUTH = "?key=" + Key + "&token=" + Token

    def new(self, Type, Name, Parent=None):
        if Type == "Board":
            URL = "https://api.trello.com/1/boards" + self.__AUTH
            Query = {
                "name": f"{Name}"
            }
            Response = requests.request("POST", URL, params=Query)
            Result = json.loads(Response.text)
            return Board(self.__AUTH, Result["id"])
        elif Type == "List":
            URL = "https://api.trello.com/1/lists" + self.__AUTH
            Query = {
                "name": f"{Name}",
                "idBoard": Parent.GetId(),
                "pos": "bottom"
            }
            Response = requests.request("POST", URL, params=Query)
            Result = json.loads(Response.text)
            return List(self.__AUTH, Result["id"])
        elif Type == "Card":
            URL = "https://api.trello.com/1/cards" + self.__AUTH
            Query = {
                "name": f"{Name}",
                "idList": Parent.GetId(),
                "pos": "bottom"
            }
            Response = requests.request("POST", URL, params=Query)
            Result = json.loads(Response.text)
            return Card(self.__AUTH, Result["id"])


    def GetBoardByName(self, BoardName):
        URL = "https://api.trello.com/1/members/me/boards" + self.__AUTH
        Response = requests.request("GET", URL, headers=Headers)
        Result = json.loads(Response.text)
        for BoardObject in Result:
            if BoardObject["name"] == BoardName:
                return Board(self.__AUTH, BoardObject["id"])
        return None
    
    def GetBoardById(self, BoardId):
        return Board(self.__AUTH, BoardId)

class Board:
    def __init__(self, Auth, BoardId):
        self.__AUTH = Auth
        self.ID = BoardId

    def GetId(self):
        return self.ID

    def GetData(self, Argument=""):
        URL = "https://api.trello.com/1/boards/" + self.GetId() + Argument + self.__AUTH
        Response = requests.request("GET", URL)
        Result = json.loads(Response.text)
        return Result

    def SetProperty(self, Property, Value):
        URL = "https://api.trello.com/1/boards/" + self.GetId() + "/" + Property + self.__AUTH + "&value=" + Value
        requests.request("PUT", URL)

    def GetURL(self):
        return self.GetData()["url"]

    def GetShortURL(self):
        return self.GetData()["shortUrl"]

    def GetName(self):
        return self.GetData()["name"]
    
    def GetDesc(self):
        return self.GetData()["desc"]

    def IsArchived(self):
        return self.GetData()["closed"]

    def GetLists(self):
        return self.GetData("/lists")

    def GetCards(self):
        return self.GetData("/cards")

    def GetLabels(self):
        return self.GetData("/labels")

    def GetListByName(self, ListName):
        Lists = self.GetLists()
        for ListObject in Lists:
            if ListObject["name"] == ListName:
                return List(self.__AUTH, ListObject["id"])
        return None

    def GetListById(self, ListId):
        return List(self.__AUTH, ListId)
    
    def GetCardByName(self, CardName):
        Cards = self.GetCards()
        for CardObject in Cards:
            if CardObject["name"] == CardName:
                return Card(self.__AUTH, CardObject["id"])
        return None

    def GetCardById(self, CardId):
        return Card(self.__AUTH, CardId)

    def GetLabelByName(self, LabelName):
        Labels = self.GetLabels()
        for LabelObject in Labels:
            if LabelObject["name"] == LabelName:
                return Label(self.__AUTH, LabelObject["id"])
        return None

    def GetLabelById(self, LabelId):
        return Label(self.__AUTH, LabelId)

    def GetLabelByNameAndColor(self, LabelName, LabelColor):
        Labels = self.GetLabels()
        for LabelObject in Labels:
            if LabelObject["name"] == LabelName and LabelObject["color"] == LabelColor:
                return Label(self.__AUTH, LabelObject["id"])
        return None

    def SetName(self, Name):
        self.SetProperty("name", Name)

    def SetDesc(self, Desc):
        self.SetProperty("desc", Desc)

    def SetArchived(self, Closed):
        self.SetProperty("closed", Closed)

    def Delete(self):
        URL = "https://api.trello.com/1/boards/" + self.GetId() + self.__AUTH
        requests.request("DELETE", URL)

    def ClassName(self):
        return "Board"

class List:
    def __init__(self, Auth, ListId):
        self.__AUTH = Auth
        self.ID = ListId

    def GetId(self):
        return self.ID

    def GetData(self, Argument=""):
        URL = "https://api.trello.com/1/lists/" + self.GetId() + Argument + self.__AUTH
        Response = requests.request("GET", URL)
        Result = json.loads(Response.text)
        return Result

    def SetProperty(self, Property, Value):
        URL = "https://api.trello.com/1/lists/" + self.GetId() + "/" + Property + self.__AUTH + "&value=" + Value
        requests.request("PUT", URL)

    def GetName(self):
        return self.GetData()["name"]

    def GetBoard(self):
        return Board(self.__AUTH, self.GetData()["idBoard"])

    def IsSubscribed(self):
        return self.GetData()["subscribed"]

    def IsArchived(self):
        return self.GetData()["closed"]

    def GetPosition(self):
        return self.GetData()["pos"]

    def GetCards(self):
        return self.GetData("/cards")

    def GetCardByName(self, CardName):
        Cards = self.GetCards()
        for CardObject in Cards:
            if CardObject["name"] == CardName:
                return Card(self.__AUTH, CardObject["id"])
        return None

    def GetCardById(self, CardId):
        return Card(self.__AUTH, CardId)

    def SetName(self, Name):
        self.SetProperty("name", Name)
    
    def Move(self, Board):
        self.SetProperty("idBoard", Board.GetId())

    def ClassName(self):
        return "List"

class Card:
    def __init__(self, Auth, CardId):
        self.__AUTH = Auth
        self.ID = CardId

    def GetId(self):
        return self.ID

    def GetData(self, Argument=""):
        URL = "https://api.trello.com/1/cards/" + self.GetId() + Argument + self.__AUTH
        Response = requests.request("GET", URL)
        Result = json.loads(Response.text)
        return Result

    def SetProperty(self, Property, Value):
        URL = "https://api.trello.com/1/cards/" + self.GetId() + "/" + Property + self.__AUTH + "&value=" + Value
        requests.request("PUT", URL)

    def GetName(self):
        return self.GetData()["name"]
    
    def GetDesc(self):
        return self.GetData()["desc"]

    def GetBoard(self):
        return Board(self.__AUTH, self.GetData()["idBoard"])

    def GetList(self):
        return List(self.__AUTH, self.GetData()["idList"])

    def IsSubscribed(self):
        return self.GetData()["subscribed"]

    def GetLabels(self):
        return self.GetData()["labels"]

    def IsArchived(self):
        return self.GetData()["closed"]

    def GetPosition(self):
        return self.GetData()["pos"]

    def SetName(self, Name):
        self.SetProperty("name", Name)

    def SetDesc(self, Desc):
        self.SetProperty("desc", Desc)

    def SetArchived(self, Closed):
        self.SetProperty("closed", Closed)

    def AddLabel(self, Label):
        URL = "https://api.trello.com/1/cards/" + self.GetId() + "/idLabels" + self.__AUTH + "&value=" + Label.GetId()
        requests.request("POST", URL)

    def RemoveLabel(self, Label):
        URL = "https://api.trello.com/1/cards/" + self.GetId() + "/idLabels/" + Label.GetId() + self.__AUTH
        requests.request("DELETE", URL)

    def Comment(self, Comment):
        URL = "https://api.trello.com/1/cards/" + self.GetId() + "/actions/comments" + self.__AUTH
        Query = {
            "text": f"{Comment}"
        }
        requests.request("POST", URL, Params=Query)

    def Move(self, List):
        self.SetProperty("idBoard", List.GetId())

    def Delete(self):
        URL = "https://api.trello.com/1/cards/" + self.GetId() + self.__AUTH
        requests.request("DELETE", URL)

    def ClassName(self):
        return "Card"

class Label:
    def __init__(self, Auth, LabelId):
        self.__AUTH = Auth
        self.ID = LabelId

    def GetId(self):
        return self.ID

    def GetData(self, Argument=""):
        URL = "https://api.trello.com/1/labels/" + self.GetId() + Argument + self.__AUTH
        Response = requests.request("GET", URL)
        Result = json.loads(Response.text)
        return Result

    def SetProperty(self, Property, Value):
        URL = "https://api.trello.com/1/labels/" + self.GetId() + "/" + Property + self.__AUTH + "&value=" + Value
        requests.request("PUT", URL)

    def GetName(self):
        return self.GetData()["name"]

    def GetColor(self):
        return self.GetData()["color"]
    
    def GetBoard(self):
        return Board(self.__AUTH, self.GetData()["idBoard"])

    def SetName(self, Name):
        self.SetProperty("name", Name)

    def SetColor(self, Color):
        self.SetProperty("color", Color)

    def Delete(self):
        URL = "https://api.trello.com/1/labels/" + self.GetId() + self.__AUTH
        requests.request("DELETE", URL)

    def ClassName(self):
        return "Label"

class CustomField:
    def __init__(self, Auth, CustomFieldId):
        self.__AUTH = Auth
        self.ID = CustomFieldId

    def GetId(self):
        return self.ID

    def GetData(self, Argument=""):
        URL = "https://api.trello.com/1/customFields/" + self.GetId() + Argument + self.__AUTH
        Response = requests.request("GET", URL)
        Result = json.loads(Response.text)
        return Result

    def SetProperty(self, Property, Value):
        URL = "https://api.trello.com/1/customFields/" + self.GetId() + "/" + Property + self.__AUTH + "&value=" + Value
        requests.request("PUT", URL)

    def GetName(self):
        return self.GetData()["name"]

    def GetCustomFieldOptions(self):
        return self.GetData("/options")

    def GetCustomFieldOptionByName(self, CustomFieldOptionName):
        Options = self.GetCustomFieldOptions()
        for Option in Options:
            if Option["value"]["text"] == CustomFieldOptionName:
                return CustomFieldOption(self.__AUTH, self, Option["_id"])
        return None

    def SetName(self, CustomFieldName):
        self.SetProperty("name", CustomFieldName)

    def Delete(self):
        URL = "https://api.trello.com/1/customFields/" + self.GetId() + self.__AUTH
        requests.request("DELETE", URL)

    def ClassName(self):
        return "CustomField"

class CustomFieldOption:
    def __init__(self, Auth, CustomFieldObject, CustomFieldOptionId):
        self.__AUTH = Auth
        self.ID = CustomFieldOptionId
        self.CustomField = CustomFieldObject

    def GetId(self):
        return self.ID

    def GetCustomField(self):
        return self.CustomField

    def GetData(self, Argument=""):
        URL = "https://api.trello.com/1/customFields/" + self.GetCustomField().GetId() + "/options/" + self.GetId() + Argument + self.__AUTH
        Response = requests.request("GET", URL)
        Result = json.loads(Response.text)
        return Result

    def GetName(self):
        return self.GetData()["value"]["text"]

    def GetColor(self):
        return self.GetData()["color"]

    def Delete(self):
        URL = "https://api.trello.com/1/customFields/" + self.GetCustomField().GetId() + "/options/" + self.GetId() + self.__AUTH
        requests.request("DELETE", URL)

    def ClassName(self):
        return "CustomFieldOption"