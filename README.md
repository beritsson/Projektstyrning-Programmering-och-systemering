Boklånesystemet

Syftet med mitt boklånesystem är att fånga in allt vi lärt oss på kursen.
Mitt system innehåller classer, listor, for och whileloopar, random-funktioner osv.

När man startar boklånesystemet möts man av ett login och passord. Jag har hårdkodat ett adminkonto som skapar nya
användarkonton.

Adminlogin: admin
passord: admin

Som admin har du rätt till att
- skapa nya konton till användare:  Man anger namn och önskat lösenord. Där slumpar systemet upp ett tresiffrigt tal
som används som boknings-id och det passord användaren angav.
- lista användare:  Där ser admin vilka som ligger uppe i systemet, den anger även hur många som är i listan
- radera enskilda i listan med hjälp av boknings-id:t
- avsluta

Tanken är att kunden söker upp en anställd som skapar ett användarkonto till kunden

När detta är gjort och kunden fått sitt specifika boknings-id och sitt egna lösenord kan denne logga in.
Där möts man av ”Hej (sitt namn)”

Nu kan kunden:
- lägga till böcker i sin bokningslista
- ta bort böcker i sin bokningslista
- se böcker i sin bokningslista
- skriva ut sina böcker till en personunik textfil
- radera sin bokningslista
- och att avsluta och logga ut.

Jag har byggt upp koden kring en Användarklass (Users) där jag knytit namn, lösenord som med interaktiv input och ett
framslumpat tresiffrigt nummer som är grunden till inloggningen sen.
Sen finns en till klass Books som har hand om författare och titel.

Allt styrs via två while-loopar en för admin-menyn och en för users-menyn. Sen med forloopar i själva svarsalternativen
som tar fram rätt användare eller rätt bok. Jag har tagit med AND så att jag kan ha en IF-sats för att få ut
bokningsid och passord samtidigt och jag har en OR för att kunden kan välja att radera en bok med antingen författare
eller titel.

Jag var i stort sätt helt klar när jag insåg att jag lagt boklistan (booklist = []) global. Det innebar att oavsett
inloggad användare blev inte boklistan privat. Alla användare kunde nå en användares boklista.
För att göra boklistan privat var jag tvungen att lägga alla funktioner som berörde boklistan i User-klassen, sen
anropa objekten från val-menyerna.
Valmöjligeheten i detta program är nästan oändlig, det finns långt fler funktioner man kan lägga på som tex
- nu skriver den bara till i textfilen, men man kan göra samma ändringar som ovan.
- en funktion är att göra userlist som en textfil med och hämta användare där ifrån så raderas inte de varje gång jag
startar om programmet.
- skicka textfilen till en epostadress.

Jag har stött på stora problem under tiden, från programatiska fel till vanliga småfel som att glömt en parantes.

