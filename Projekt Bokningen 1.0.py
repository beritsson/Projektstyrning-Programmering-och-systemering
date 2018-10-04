import random                                                               # tillämpar randomfunktionen
CorrectBokningsId = "admin"                                                 # hårdkodar admin-loginet
CorrectPassword = "admin"

y = 0                                                                       # anger y = 0 för usermeny 5


class User:                                                                 # definierar user classen
    def __init__(self, namn, password):                                     # inlogningen sker med namn och password
        self.__boknings_id = str(random.randint(100, 999))                  # skapar bokningsnumrets randomfunktion som hemlig
        self.__password = password                                          # passordet är hemligt
        self.namn = namn
        self.boklista = []                                                  # boklistan jag beskrev om i dokumentationen


    def getboknings_id(self):                                               # gör bokningsnumret och passordet synbart
        return self.__boknings_id

    def setboknings_id(self,boknings_id):
        self.__boknings_id = boknings_id

    def getpassword(self):
        return self.__password

    def setpassword(self,password):
        self.__password = password

    def addbook(self, Roman):                                               # User menyval 1
        self.boklista.append(Roman)                                         # adderar böcker i boklista

    def removebook(self,tabort):                                            # User menyval 2
        for x in self.boklista:                                             # tar bort böcker i boklistan
            if (x.getauthor() == tabort) or (x.gettitle() == tabort):       # kan ta bort antingen författare eller titel
                self.boklista.remove(x)

    def listbooks(self):                                                    # User menyval 3
        for x in self.boklista:                                             # listar fram böcker i boklistan
            print(x)

    def numberofbook(self):                                                 # hanterar antalet böcker i listan
        print("Antalet böcker: ")
        print(len(self.boklista))

    def sparatillfil(self):                                                 # User menyval 4
        with open(self.__boknings_id + ".txt", mode="a") as output:         # sparar boklistan till fil
            for x in self.boklista:
                output.write(str(x))

    def removeallbooks(self):                                               # User menyval 5
        self.boklista = []                                                  # raderar alla böcker i listan
        print("Din boklista är nu raderad")

    def __str__(self):                                                      # Inbyggd metod att göra dessa tre till strängar
        return self.__boknings_id + ", " + self.__password + ", " + self.namn

class Books:                                                                # skapar bok klassen
    def __init__(self, author, title):                                      # bokklassen initieras med författare och titel
        self.__title = title
        self.__author = author

    def gettitle(self):
        return self.__title

    def settitle(self,title):
        self.__title = title

    def getauthor(self):
        return self.__author

    def setauthor(self,author):
        self.__author = author

    def __str__(self):
        return self.__author + ": " + self.__title + "\n"



userlist = []                                                               # userlist för användarna


def checkUser(u, p):                                                        # kontrollerar loginet
    for account in userlist:
         if (account.getboknings_id().upper() == u.upper()) and (account.getpassword().upper() == p.upper()):
            return True
    return False

while True:
    boknings_id = input("Ange ditt Boknings-ID: ")
    password    = input("Ange ditt lösenord: ")

    if(boknings_id.upper() == CorrectBokningsId.upper()) and (password.upper() == CorrectPassword.upper()):

        print("\nVälkommen " + boknings_id)                                 # är inlogget sant möts man av "Hej och sitt namn

        Adminloopen = True

        while Adminloopen == True:

            huvudadminmenu = "\nMenysystemet för admin\n" \
                             "1 - Skapa ny användare\n" \
                             "2 - Radera användare\n" \
                             "3 - Lista användare\n" \
                             "4 - Avsluta\n" \
                             "Ange svar: "


            try:                                                            # Användaren måste använda siffror
                val = int(input(huvudadminmenu))



                if (val ==1):

                    konto = User(input("Skriv in ditt namn: "), input("Skriv in önskat lösenord: "))

                    userlist.append(konto)

                    menustr =   "\n\o/ Välkommen till Bokningen \o/\n" \
                                "\nLåntagarens bokningsnummer är: " + konto.getboknings_id() + "\n" \
                                "Låntagarens lösenord är: " + konto.getpassword() + "\n";

                    print(menustr)                                          # konto skapas till userlist.

                elif (val == 2):
                    radera = input("Ange den användare som ska raderas. Ange dess användarID : ")
                    for x in userlist:
                        if (x.getboknings_id() == radera):
                            userlist.remove(x)                              # radera med hjälp av boknings_id
                elif (val == 3):
                    for x in userlist:
                        print(x)

                    print("Antal användare i listan: ")
                    print(len(userlist))                                    # listar och skriver ut hur många i userlist

                elif (val == 4):
                    print("Du har valt att avsluta adminfönstret")
                    Adminloopen = False                                     # avslutar med Adminloopen = False för att komma till inloggningssidan

                else:
                    print("Valet du angav finns inte")                      # Om man valt någon annan siffra än 1-4

            except:
                print("Bara siffror fungerar")                              # tillhör try




    elif (checkUser(boknings_id, password)):

        for användare in userlist:                                          # om man loggar in med userpassword
            if (boknings_id == användare.getboknings_id()):
                print("\n\nHej " + användare.namn)


                print("\nVälkommen till lånelistan")

                Loanmaker = True

                while Loanmaker == True:


                    låntagarmeny = "\n\n1 - Vill du lägga till bok\n"  \
                               "2 - Vill du ta bort bok\n" \
                               "3 - Vill du se böcker i din lista\n" \
                               "4 - Vill du skriva ut till bookloan.txt\n" \
                               "5 - Vill du radera din lista\n" \
                               "6 - VIll du avsluta\n" \
                               "Ange val: "
                    try:

                        låntagare = int(input(låntagarmeny))                # Förhindrar "strings" i valmenyn

                        if (låntagare == 1):

                            Roman = Books(input("\nLägg till författare: "), input("Lägg till titel: "))
                            användare.addbook(Roman)                        # pekar på addbooks-objektet i User klassen
                            användare.numberofbook()                        # pekar på numberofbook-objektet i Userklassen



                        elif (låntagare == 2):

                            tabort = input("Ange den författare eller titel som ska tas bort: ")
                            användare.removebook(tabort)                    # perkar på objektet i Userklassen

                        elif (låntagare == 3):
                            användare.listbooks()
                            användare.numberofbook()

                        elif (låntagare == 4):
                            användare.sparatillfil()

                        elif (låntagare == 5):
                            rad = input("Vill du verkligen radera listan? (y),(n)")
                            if (rad == "y"):
                                användare.removeallbooks()

                            else:                                           # Valet nej blir pass för att återgå till menyn
                                pass

                        elif (låntagare == 6):
                            print("Du har valt att avsluta Bokningen")
                            Loanmaker = False

                        else:
                            print("Menyval 1-6 fungerar bara")

                    except:
                        print("Siffror fungerar bara")

    else:
        print("Ditt bokningsnummer eller lösenord är felaktigt")             # Om checken för user och password inte stämmer
