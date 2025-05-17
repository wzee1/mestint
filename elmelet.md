**Alpha-béta nyesés:**

Egy optimalizációs technika a **minimax algoritmushoz**.\
Célja, hogy csökkentse a kiértékelt csomópontok számát a játékfában anélkül,\
hogy befolyásolná a végső döntést. Úgy működik, hogy **levágja (nyesi)** azokat az ágakat,\
amelyekről bebizonyosodik, hogy nem befolyásolhatják a legjobb lépést.


**AC-1 algoritmus:**

Egy **korlátozás-kielégítési probléma (CSP)** megoldására használt **konzisztencia-ellenőrző algoritmus**.\
Biztosítja, hogy egy változó tartományának minden értéke konzisztens legyen legalább egy\
értékkel a szomszédos változók tartományában az adott korlátozás szempontjából.\
Az "AC" az "Arc Consistency" (ívkonzisztencia) rövidítése, az "1" pedig a konzisztencia\
egy bizonyos szintjére utal.


**Minimax algoritmus:**

Egy **rekurzív döntési algoritmus**, amelyet tipikusan **két személyes, nulla összegű játékokban**\
(pl. sakk, tic-tac-toe) használnak. Célja, hogy megtalálja az egyik játékos (a **maximalizáló**)\
optimális lépését feltételezve, hogy a másik játékos (a **minimalizáló**) is optimálisan játszik\
a saját szempontjából. Az algoritmus a játékfa összes lehetséges lépését és azok kimenetelét értékeli,\
és a maximalizáló a számára legkedvezőbb kimenetelt biztosító lépést választja.