# mysql + python

Mitt programm �r ett startprogram f�r en loginsida. 
D�r en redan f�rregistrerad Admin kan utf�ra vissa f�r�ndringar p� anv�ndare. 
Admin kan
- skapa ny anv�ndare 
- ta bort anv�ndare.
- lista anv�ndare 

Detta �r l�nkat till en databas s� all info h�mtas fr�n den

Admin beh�ver bara anv�nda GUI:t f�r att g�ra sina �nskem�l. 

Antingen testar anv�ndaren att logga in, g�r det inte kontaktas admin.

Login f�r Admin:
#Anv�ndarnamn: admin
#L�senord: admin



- Skapa ny anv�ndare:
I rullmenyn Anv�ndare tas "L�gga till anv�ndare" fram.
D�r anges nytt login/l�sen och tryck p� knappen spara

- Ta bort anv�ndare:
I rullistan Anv�ndare anges "Ta bort anv�ndare" 
Ange anv�ndarnamn och tryck spara. En popupruta ger info att anv�ndaren �r borttagen

- Visa alla anv�ndare:
Ger bild fr�n databasen vad som finns i registret.

Jag har valt att stanna d�r d� tiden inte fanns samt att det blev mycket komplicerat.

Programmet har tv� klasser, en f�r databasen och en f�r guit. Mellan dessa h�mtas 
info och l�ses in p� databasen.

M�jliga �tg�rder:
- Skapa en kundsida
- G�ra guit mer fint

