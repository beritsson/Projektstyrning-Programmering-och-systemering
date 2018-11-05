# mysql + python

Mitt programm är ett startprogram för en loginsida. 
Där en redan förregistrerad Admin kan utföra vissa förändringar på användare. 
Admin kan
- skapa ny användare 
- ta bort användare.
- lista användare 

Detta är länkat till en databas så all info hämtas från den

Admin behöver bara använda GUI:t för att göra sina önskemål. 

Antingen testar användaren att logga in, går det inte kontaktas admin.

Login för Admin:
#Användarnamn: admin
#Lösenord: admin



- Skapa ny användare:
I rullmenyn Användare tas "Lägga till användare" fram.
Där anges nytt login/lösen och tryck på knappen spara

- Ta bort användare:
I rullistan Användare anges "Ta bort användare" 
Ange användarnamn och tryck spara. En popupruta ger info att användaren är borttagen

- Visa alla användare:
Ger bild från databasen vad som finns i registret.

Jag har valt att stanna där då tiden inte fanns samt att det blev mycket komplicerat.

Programmet har två klasser, en för databasen och en för guit. Mellan dessa hämtas 
info och läses in på databasen.

Möjliga åtgärder:
- Skapa en kundsida
- Göra guit mer fint

