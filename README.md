Python Trello API
=========================

trello.py is a simple Python API that is used to communicate with [Trello]("https://trello.com/"). It is an Object-Oriented API and uses the [Trello Rest API](https://trello.com/docs/api/index.html).

This API is insipired by LisaF854's [Roblox-Trello | Object Oriented Trello API](https://devforum.roblox.com/t/roblox-trello-object-oriented-trello-api/233582). It uses a similar structure to that API, so you will notice many of the functions there are applied to this API.

This API has easy and user-friendly functions that do a lot of the task you would do normally yourself. More functions will be added in the future in case they are needed.

Getting Started
---------------

To use the this API, first install it from PyPI using `pip`:

    pip install trello.py

or downloading from the [GitHub]("https://github.com/Batman212369/trello.py") page and run the code in your directory:

    python setup.py install

This API requires both an app key and a token in order to work. To get your app key, simply go to [https://trello.com/app-key](https://trello.com/app-key) and grab the app key generated. Keep it stored somewhere for now because you will need to access it later.

Once you have your app key, you will need to get your app token as well. You can visit [https://trello.com/1/authorize?expiration=never&scope=read,write&response_type=token&name=Trello.py%20Access&key=YOUR_KEY_HERE](https://trello.com/1/authorize?expiration=never&scope=read,write&response_type=token&name=Trello.py%20Access&key=YOUR_KEY_HERE) in order to get your token. Make sure that you replace `YOUR_KEY_HERE` with your app key. Once you have authorized it, it will give you your token. Store that token somewhere as well.

> **WARNING:** You should only share your token with people that you trust. Your token is like the password of your account and the app key is the username. If your app key is ever leaked, it should not cause many issues, but it is recommended that you change it. On the other hand, if your token is in fact leaked, make sure to remove access to it immediately and generate a new one. If a person has your token, then they have access to your account (via code) and have the ability to do anything that you can do. Make sure it is always kept in a safe place and hidden from the public.

The following code is an example of importing the Trello API (as Trello), retrieving board by it's name, and getting the board's data. 
```python
    from trello import TrelloAPI as Trello

    MyTrello = Trello("YOUR_APP_KEY", "YOUR_TOKEN")
    Board = MyTrello.GetBoardByName("Your Board Name")
    BoardData = Board.GetData()
```
###### (*Note: Trello does support OAuth, but the Python API does not have any support for it yet.*)

Basic Info
---------------

You can think of the `Trello` class as the account. You should only have one instance of `Trello` initialized in your script. Although it is allowed, it is not recommended to have more than one instances of `Trello`.

The `Trello` instance comes with three basic functions:
 * GetBoardByName(*String* `BoardName`) - Gets a board by it's name
 * GetBoardById(*String* `BoardId`) - Gets a board by it's ID
 * new(*String* `Type`, *String* `Name`, *Object* `Parent`) - Creates a new object (`Board`, `List`, `Card`) with the given name. If it is a `List` object, then the parent must be a `Board` object, which is the board that the list will be in. If it is a `Card` object, then the parent must be a `List` object, which is the list that the list will be in. If it is a board, ten you can leave it blank

Currently, there are five types of objects, `Trello`, `Board`, `List`, `Card`, and `Label`. Each object has it's own functions that relate to it, with all of them (except `Trello`) having some common functions which are;
 * GetId() - Gets the ID of the object
 * GetData(*String* `Param` *(OPTIONAL)*) - Gets the object's data in JSON. The `Param` parameter is optional. It is basically an extention to the pre-made URL for special requests, like lists of cards or labels
 * SetProperty(*String* `Property`, *String* `Value`) - Sets the value of the `Property` of the object to `Value`. It isn't recommended that you use this function. Only use when needed to
 * ClassName() - Returns the class name of the object (`Board`, `List`, `Card`, or `Label`)

 Bugs, Reports, and Suggestions
---------------

Keep in mind that this API is in its early stages. It **will** have bugs and that is something that is common to early versions. If you find any bugs or have any suggestions, please send them directly to me via Discord or create a bug report or suggestion on the [GitHub]("https://github.com/Batman212369/trello.py") page  (W.I.P.). If you contact me through Discord, my username is `Batman212369#5703`.

> **NOTE:** Yes, I know that currently there aren't any checkings (doesn't check for errors nor if the input is the correct type) when calling methods. This will be added soon, but for now just use the API responsibly and you should not get any errors.