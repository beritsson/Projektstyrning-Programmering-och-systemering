from tkinter import *
from tkinter import messagebox
import mysql.connector


# Databashanteringsklassen,
# här hämtar vi och lagrar data till/från databasen
class Database():
    def __init__(self):
        self.connectionstring = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'testmaster'
        }

    # Denna metod kollar mot databasen om användare existerar
    # Isåfall så returnerar den tillbaks dess användarnamn, ID samt vilken behörighet den har (roll)
    # som antingen kan vara administratör eller låntagare
    def checkUser(self, u, p):
        self.mydb = mysql.connector.connect(**self.connectionstring)

        cursor = self.mydb.cursor()

        sql = "SELECT UID, username, role FROM users WHERE username='%s' AND password='%s'" % (u.get(), p.get())

        # Förbered ett tomt användareobjekt (som vi returnerar tillbaks)
        # om vi misslyckade att logga in oss
        mUser = {
            "uid": "",
            "username": "",
            "role": ""
        }

        try:
            cursor.execute(sql)  # Utför SQL kommandot
            result = cursor.fetchone()  # Hämta den första träffen vi får

            # Spar resultatet
            mUser["uid"] = result[0]
            mUser["username"] = result[1]
            mUser["role"] = result[2]

            return mUser
        except:
            # Om vi inte hittade/fann någon användare så misslyckades vi
            # och hamnar därför här!
            print("Det gick inte att hämta datan från databasen")
            return mUser

        self.mydb.close()  # Stäng kopplingen mot databasen

    def saveBooks(self, books):
        pass

    def getAllBooks(self):
        pass


    def saveNewUser(self, u, p):
        self.mydb = mysql.connector.connect(**self.connectionstring)

        cursor = self.mydb.cursor()

        sql = "SELECT UID FROM users WHERE username=\'" + u + "\'"

        try:
            cursor.execute(sql)
            res = cursor.fetchone()
        except:
            return "Något gick fel att hämta användare ur databasen"

        if (res == None):

            # SQL Frågans formulering på hur man ska spara värden i databasen
            # Lägg märke till att "fältnamnen" här heter ju username och password
            sql2 = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
            val = (u, p, 'låntagare')  # Detta var ju värdet (value) som man skickar med

            try:
                cursor.execute(sql2, val)  # Utför SQL kommandot

                self.mydb.commit()  # Detta behövs om vi behöver backa tillbaks
                # dvs om vi misslyckades spara något i databasen
                # TAGET från w3schools.com
                # NEJ vi behöver inte returnera något om vi inte vill
                # Vi hämtar ju inte något eller hur ?? vi spar ju bara till databasen
                return "Användaren är tillagd"
            except:
                # Om vi inte hittade/fann någon användare så misslyckades vi
                # och hamnar därför här!
                print("Det gick inte att spara datan från databasen")
                # Samma här!
                return "Något gick fel att lägga till en användare"

            self.mydb.close()  # Stäng kopplingen mot databasen
        else:
            print("Sorry du har redan en användare som heter så")
            return "Du kan inte lägga till denna användare finns redan"


    def removeUser(self, uid):
        print("removeUser from database  , userID=", uid)
        self.mydb = mysql.connector.connect(**self.connectionstring)

        cursor = self.mydb.cursor()

        sql = "DELETE FROM users WHERE username=\'" + uid + "\'"

        try:
            cursor.execute(sql)  # Utför SQL kommandot

            self.mydb.commit()  # Detta behövs om vi behöver backa tillbaks
            # dvs om vi misslyckades spara något i databasen
            # TAGET från w3schools.com
            # NEJ vi behöver inte returnera något om vi inte vill
            # Vi hämtar ju inte något eller hur ?? vi spar ju bara till databasen

            # Visar popup att användaren är borttagen
            messagebox.showinfo("Info",
                                "Den valda användaren är borttagen")

            print("användare borttagen")
        except:
            # Om vi inte hittade/fann någon användare så misslyckades vi
            # och hamnar därför här!
            print("Det gick inte att hämta datan från databasen")
            # Samma här!

        self.mydb.close()  # Stäng kopplingen mot databasen



    # Lista alla användare som är med i databasen
    def getAllUsers(self):
        self.mydb = mysql.connector.connect(**self.connectionstring)

        cursor = self.mydb.cursor()

        sql = "SELECT UID, username, role FROM users"

        try:
            cursor.execute(sql)  # Utför SQL kommandot
            result = cursor.fetchall()  # Hämta ALLA träffar vi får

            # returnera resultatet
            return result
        except:
            # Om vi inte hittade/fann någon användare så misslyckades vi
            # och hamnar därför här!
            print("Det gick inte att hämta datan från databasen")
            return None

        self.mydb.close()  # Stäng kopplingen mot databasen

    # OSV .... varje metod här
    # ska ju vara SQL frågor som hämtar data och returnerar tillbaks den
    # eller lagrar datan i databasen


# Hela bokningssystemet är representerat som en klass
class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self)
        self.parent = parent
        self.parent.geometry("800x600+120+120")
        self.parent.configure(background="sky blue")  # Sätt bakgrundsfärgen på hela fönstret
        self.db = Database()  # Skapa ett beroende av klassen Database här
        self.currentFrame = []  # Denna del håller på den nuvarande frame som vi använder
        self.password = StringVar()
        self.username = StringVar()
        self.menubar = Menu(tearoff=False)
        self.parent.config(menu=self.menubar)  # se till att konfigurera / förberedd för att ha meny längs överst
        self.showLoginUI()

    # Visa inloggningsrutan
    def showLoginUI(self):

        self.parent.title("Inloggningssida till Biblioteket")

        self.loginframe = Frame(self.parent)
        self.loginframe.pack(expand=True, padx=10,
                             pady=10)  # Expand = true gör att man centrerar frame i mitten av fönstret

        Mintext1 = Label(self.loginframe, text="Användarnamn:", anchor=CENTER, justify="right")
        Mintext1.grid(row=0, column=0)

        Enter1 = Entry(self.loginframe, text=self.username, bd=2)
        Enter1.grid(row=0, column=1)

        Mintext2 = Label(self.loginframe, text="Lösenord:", anchor=CENTER, justify="right")
        Mintext2.grid(row=1, column=0)

        Enter2 = Entry(self.loginframe, bd=2, show="*", text=self.password)
        Enter2.grid(row=1, column=1)

        Knapp2 = Button(self.loginframe, text="Avsluta", bg="grey", fg="black", command=exit)
        Knapp2.grid(row=2, column=0)

        Knapp1 = Button(self.loginframe, text="Login", bg="lawn green", fg="black", command=self.checkUser)
        Knapp1.grid(row=2, column=1)

    # Kollar om vi lyckades logga in oss eller ej
    def checkUser(self, *e):
        # Gör en SQL fråga och skicka med inloggningsuppgifterna för användare
        res = self.db.checkUser(self.username, self.password)

        if res["role"] == "låntagare":
            self.loginframe.pack_forget()  # Dölj först inloggningen self.loginframe
            self.showUserUI()  # Visa sedan användargränssnittet för en enkel låntagare
        elif res["role"] == "administratör":
            self.loginframe.pack_forget()
            self.showAdminUI()
        else:
            # Visa popup felmeddelande för användare om man angav en användare som inte fanns med i databasen
            messagebox.showinfo("Felmeddelande",
                                "Antingen har du angivit fel användarnamn och/eller lösenord, försök igen")
            # Rensa sedan användarnamn och lösenordet här
            self.cleanUp()
            pass

    # Visa låntagarens huvudgränssnitt
    def showUserUI(self):
        # Skapa en ny frame här som bara visar vår användares UI
        self.userframe = Frame(self.parent, bg="antique white")
        self.userframe.pack(side="top", fill="both", expand=True)

        # skapa topframe där vi kan placera olika knappar
        topFrame = Frame(self.userframe, bg="grey")
        topFrame.pack(side="top", fill="both", expand=True, ipadx=10, ipady=10)

        # Utloggningsknappen (placera den i den översta topframe)
        signOutBtn = Button(topFrame, text="Logga ut", bg="lawn green", fg="black", command=self.signOutUser)
        signOutBtn.grid(row=0, column=1)

        # Skapa menysystem för hantering av boklån
        boklan = Menu(self.menubar, tearoff=False)

        self.menubar.add_cascade(label="Boklån", menu=boklan, command=None)
        boklan.add_command(label="Valfri Meny1", command=None)
        boklan.add_command(label="Valfri Meny2", command=None)
        boklan.add_command(label="Valfri Meny3", command=self.showMybooks)
        boklan.add_separator()
        boklan.add_command(label="Valfri Meny4", command=None)

        self.parent.geometry("800x600+120+120")
        self.parent.title("Välkommen! du är nu inloggad som: " + self.username.get())

    # Visa administratörens huvudgränssnitt
    def showAdminUI(self):
        # Skapa en ny frame här som bara visar vår administratörs UI
        self.adminframe = Frame(self.parent, bg="antique white")
        self.adminframe.pack(side="top", fill="both", expand=True)

        # skapa topframe där vi kan placera olika knappar
        topFrame = Frame(self.adminframe, bg="grey")
        topFrame.pack(side="top", fill="both", expand=False, ipadx=10, ipady=10)

        # Utloggningsknappen (placera den i den översta topframe)
        signOutBtn = Button(topFrame, text="Logga ut", bg="lawn green", fg="black", command=self.signOutAdmin)
        signOutBtn.grid(row=0, column=1)

        # Skapa menysystem för hantering av användare
        users = Menu(self.menubar, tearoff=False)

        self.menubar.add_cascade(label="Användare", menu=users, command=None)
        users.add_command(label="Lägg till användare", command=self.createNewUser)
        users.add_command(label="Ta bort användare", command=self.removeUser)
        users.add_separator()
        users.add_command(label="Visa alla användare", command=self.showAllUsers)



        self.parent.geometry("800x600+120+120")
        self.parent.title("Välkommen! du är nu inloggad som: " + self.username.get())

    # Ta bort en användare från databasen
    def removeUser(self):
        # Rensa tidigare frame om vi hade en sådan (OBS detta gäller endast menyvalens frame inte userframe eller adminframe eller loginframe)
        self.closeAllFramesWhenChangeInMenu()

        self.removeuserframe = Frame(self.adminframe, bg="antique white")
        self.removeuserframe.pack(side="top", fill="both", expand=True)

        # Spar en kopia av denna removeuserframe frame så vi kan ta bort den när vi väljer något annat val i menyn INNAN vi är klara
        # Vi sparar då en "kopia" av removeuserframe som ett objekt i array:en i currentFrame
        self.currentFrame = [self.removeuserframe]

        # Definiera lokalt två nya variabler som vi ska skicka med till spara ny användare metoden
        # och som vi ska använda i Entry elementen
        uid = StringVar()

        # Nedan lägger till två rutor för att skriva in användarnamn och lösenord för den nya användare
        Mintext1 = Label(self.removeuserframe, text="Användar-ID:", anchor=CENTER, justify="right")
        Mintext1.grid(row=0, column=0)

        Enter1 = Entry(self.removeuserframe, text=uid, bd=2)
        Enter1.grid(row=0, column=1)

        Knapp2 = Button(self.removeuserframe, text="Ta Bort", bg="grey", fg="black",
                        command=lambda: self.db.removeUser(uid.get()))  # <-- obs skickar med u och p som skrev in
        Knapp2.grid(row=2, column=0)

        # Stäng fönstret när vi är klara
        closeBtn = Button(self.removeuserframe, text="Stäng", fg="black",
                          command=lambda: self.removeuserframe.pack_forget())  # <-- pack_forget() stänger ned frameobjektet!
        closeBtn.grid(row=2, column=1)

        # Denna visar ett UI för att lägga till en ny användare

    def createNewUser(self):
        # Rensa tidigare frame om vi hade en sådan (OBS detta gäller endast menyvalens frame inte userframe eller adminframe eller loginframe)
        self.closeAllFramesWhenChangeInMenu()

        self.createnewuser = Frame(self.adminframe, bg="antique white")
        self.createnewuser.pack(side="top", fill="both", expand=True)

        # Spar en kopia av denna createnewuser frame så vi kan ta bort den när vi väljer något annat val i menyn INNAN vi är klara
        # Vi sparar då en "kopia" av createnewuser som ett objekt i array:en i currentFrame
        self.currentFrame = [self.createnewuser]

        # Definiera lokalt två nya variabler som vi ska skicka med till spara ny användare metoden
        # och som vi ska använda i Entry elementen
        u = StringVar()
        p = StringVar()

        # Nedan lägger till två rutor för att skriva in användarnamn och lösenord för den nya användare
        Mintext1 = Label(self.createnewuser, text="Användarnamn:", anchor=CENTER, justify="right")
        Mintext1.grid(row=0, column=0)

        Enter1 = Entry(self.createnewuser, text=u, bd=2)
        Enter1.grid(row=0, column=1)

        Mintext2 = Label(self.createnewuser, text="Lösenord:", anchor=CENTER, justify="right")
        Mintext2.grid(row=1, column=0)

        Enter2 = Entry(self.createnewuser, bd=2, show="*", text=p)
        Enter2.grid(row=1, column=1)

        Knapp2 = Button(self.createnewuser, text="Spara", bg="grey", fg="black",
                        command=lambda: self.saveNewUser(u, p))  # <-- obs skickar med u och p som skrev in
        Knapp2.grid(row=2, column=0)

        # Stäng fönstret när vi är klara
        closeBtn = Button(self.createnewuser, text="Stäng", fg="black",
                          command=lambda: self.createnewuser.pack_forget())  # <-- pack_forget() stänger ned frameobjektet!
        closeBtn.grid(row=2, column=1)

    # Detta spar nu i databasen
    def saveNewUser(self, u, p):
        print("SaveNewUser")
        self.db.saveNewUser(u.get(), p.get())  # skicka nu detta till vår databasklass för att spara datan i databasen

    # Listar alla användare som finns med i databasen
    def showAllUsers(self):

        # Först stänger vi tidgare ev frame om vi hade en sådan ram visad sedan tidigare
        self.closeAllFramesWhenChangeInMenu()

        res = self.db.getAllUsers()  # Hämta alla användare i system

        self.showallusers = Frame(self.adminframe, bg="antique white")
        self.showallusers.pack(side="top", fill="both", expand=True)

        # Spar en kopia av denna showallusers frame så vi kan ta bort den när vi väljer något annat val i menyn INNAN vi är klara
        # Vi sparar då en "kopia" av showallusers som ett objekt i array:en i currentFrame
        self.currentFrame = [self.showallusers]

        t = Text(self.showallusers)
        r = ""

        # Gå igenom samtliga användare i via forloop och lägg till användarna i variabeln r
        for x in res:
            r = r + "Användare : " + str(x[1]) + " , Typ : " + str(x[
                                                                       2]) + "\n"  # <-- här tar vi ut innehållet på position 1 och 2 ur "tupeln" (dvs x) för de innehåller användarnamnet och vilken typ

        # Här lägger vi till allt i r till vårt text-widget objekt vi skapat och visar därmed alla användare i UI
        t.insert(END, r)

        t.pack()

    # Visar alla böcker som en inloggad användare har
    def showMybooks(self):
        # Först stänger vi tidgare ev frame om vi hade en sådan ram visad sedan tidigare
        self.closeAllFramesWhenChangeInMenu()

        # TODO: Här har vi använding av self.db för att
        # ställa en SQL fråga mot databasen för att hämta alla våra böcker
        print("Visa mina lånade böcker från databasen")

    # Utloggningen som kastar tillbaka oss till inloggningsrutan igen
    def signOutUser(self):
        self.userframe.pack_forget()
        self.showLoginUI()
        self.cleanUp()

    def signOutAdmin(self):
        self.adminframe.pack_forget()
        self.showLoginUI()
        self.cleanUp()

    # Rensa inloggningsuppgifter och menysystemet
    def cleanUp(self):
        self.username.set("")
        self.password.set("")
        self.menubar.delete(0, END)

    # Stäng alla Frames som är öppna förutom den inloggade framesen beroende
    # på om man är admin eller låntagare, men detta används när man väljer något annat i menyn
    def closeAllFramesWhenChangeInMenu(self):
        # Kolla bara så att denna INTE är tom, då är det ju omöjligt och fel att
        # försöka stänga tidigare frames
        if self.currentFrame is not None:
            for obj in self.currentFrame:
                obj.pack_forget()  # <---som tidigare används pack_forget för att stänga detta


# Huvudprogrammet
if __name__ == '__main__':
    root = Tk()
    myApp = App(root)  # Här skapar vi appobjektet och startar igång programmet
    root.mainloop()  # viktiga mainloop för hela GUI