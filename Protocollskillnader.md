Skillnader mellan protocoller.
==============================

##OCI
Är modellen för att beskriva de olika lagren i en datauppsättning. 
Den beskriver allt från grunden med inkoppling med sladdar till färdigt program och applikationer. 
OCI har sju olika grundlager som måste uppfyllas för att ett system ska kunna köras.
 
##TCP/UDP
Är ett förenklat system som beskriver OCI-lagren i fyra stycken lager. 
Network Access – är förenklat som innehåller OCI-lagren: den fysiska datorn, och anslutningen
Internet  -  är OCIs nätverket till omvärlden
Host to host – är OCIs överflyttningen av data
Application – Är programmet och alla applikationer som tillhör huvudprogrammet. 

##TCP
Det innebär att paketen sänds över med en checksum i slutet. Den innebär att mottagande
server kollar att checksum är samma som skickande server. Är den inte det skickas
paketet om. Detta är bra om man ska skicka över filer där allt måste komma med, tex
en websida eller en datafil. Om ett paket måste skickas om görs det utan avbrott i en dataström
		
##UDP
Detta protokoll sänds över utan övervakning. Skulle ett paket vara fel ignoreras det och överförningen 
fortsätter som vanligt. Detta protokoll används vanligtvis via voice överförningar som iptelefoni 
Skulle man använda TCP vid telefoni skulla man få delayer vilket gör att man pratar i
munnen på varandra, detta undviks med UDP


