Skillnader mellan protocoller.
==============================

##OCI
�r modellen f�r att beskriva de olika lagren i en dataupps�ttning. 
Den beskriver allt fr�n grunden med inkoppling med sladdar till f�rdigt program och applikationer. 
OCI har sju olika grundlager som m�ste uppfyllas f�r att ett system ska kunna k�ras.
 
##TCP/UDP
�r ett f�renklat system som beskriver OCI-lagren i fyra stycken lager. 
Network Access � �r f�renklat som inneh�ller OCI-lagren: den fysiska datorn, och anslutningen
Internet  -  �r OCIs n�tverket till omv�rlden
Host to host � �r OCIs �verflyttningen av data
Application � �r programmet och alla applikationer som tillh�r huvudprogrammet. 

##TCP
Det inneb�r att paketen s�nds �ver med en checksum i slutet. Den inneb�r att mottagande
server kollar att checksum �r samma som skickande server. �r den inte det skickas
paketet om. Detta �r bra om man ska skicka �ver filer d�r allt m�ste komma med, tex
en websida eller en datafil. Om ett paket m�ste skickas om g�rs det utan avbrott i en datastr�m
		
##UDP
Detta protokoll s�nds �ver utan �vervakning. Skulle ett paket vara fel ignoreras det och �verf�rningen 
forts�tter som vanligt. Detta protokoll anv�nds vanligtvis via voice �verf�rningar som iptelefoni 
Skulle man anv�nda TCP vid telefoni skulla man f� delayer vilket g�r att man pratar i
munnen p� varandra, detta undviks med UDP


