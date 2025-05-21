## Minimax algoritmus:

Egy **rekurzív döntési algoritmus**, amelyet tipikusan **két személyes, nulla összegű játékokban**\
(pl. sakk, tic-tac-toe) használnak. Célja, hogy megtalálja az egyik játékos (a **maximalizáló**)\
optimális lépését feltételezve, hogy a másik játékos (a **minimalizáló**) is optimálisan játszik\
a saját szempontjából. Az algoritmus a játékfa összes lehetséges lépését és azok kimenetelét értékeli,\
és a maximalizáló a számára legkedvezőbb kimenetelt biztosító lépést választja.

---

## Alpha-béta nyesés:

Egy optimalizációs technika a **minimax algoritmushoz**.\
Célja, hogy csökkentse a kiértékelt csomópontok számát a játékfában anélkül,\
hogy befolyásolná a végső döntést. Úgy működik, hogy **levágja (nyesi)** azokat az ágakat,\
amelyekről bebizonyosodik, hogy nem befolyásolhatják a legjobb lépést.

---

## AC-1 algoritmus:

Rendben, elnézést kérek! Félreértettem a "könnyen érthető" kérést, és túlmagyaráztam.
Most megpróbálom pontosan a kért formában, tömören és érthetően, példák nélkül átfogalmazni.

---

**AC-1 algoritmus:**

Egy **korlátozás-kielégítési probléma (CSP)** előfeldolgozására szolgáló **konzisztencia-ellenőrző algoritmus**. Célja, hogy **leszűkítse a változók (pl. input listák) lehetséges értékeit (tartományait, azaz az input listák egyes értékeit)**, kizárva azokat, amelyek biztosan nem vezetnek megoldáshoz.\

Úgy működik, hogy **ismételten ellenőrzi**, hogy minden változó tartományának minden értéke **összeegyeztethető-e** legalább egy értékkel a szomszédos változók tartományában, az adott korlátozás (azaz vannak feltételek, amiket teljesítenie kell az összes input lista összes elemének) alapján. Ha egy érték nem konzisztens, azt törli.\

Már vannak AC-3, AC-4 stb.. algoritmusok is, amelyek hatékonyabbak.

---

---

## A* kereső algoritmus

Az **A\* (ejtsd: A-csillag) kereső algoritmus** egy **informált gráfkereső** algoritmus, ami a legrövidebb utat találja meg egy kezdőponttól egy célpontig. Két tényező kombinációjával becsüli meg az egyes lépések "jóságát":
1.  **`g(n)`:** Az eddig megtett út valós költsége a kezdőponttól az aktuális `n` csomópontig.
2.  **`h(n)`:** Egy **heurisztikus függvény** által becsült költség az aktuális `n` csomóponttól a célpontig. Ez egy "okos tippelés" arról, hogy mennyire vagyunk messze a céltól.

Az A\* mindig azt a csomópontot választja ki a felfedezésre várók közül, amelynek `f(n) = g(n) + h(n)` értéke a legalacsonyabb. Ezáltal a legrövidebb utat garantálja (ha a heurisztika "megbízható"), miközben hatékonyabb, mint a nem informált keresések.

---

### Szélességi keresés (BFS - Breadth-First Search)

* **Működés:** Szinténként halad. Először az összes közvetlen szomszédot látogatja meg, majd azok szomszédait és így tovább. Mint amikor egy tóba dobsz egy követ, és a hullámok gyűrűkben terjednek.
* **Adatszerkezet:** **Sor (Queue)** (FIFO - First-In, First-Out).
* **Fakeresés:** Egyszerűen járja be a fa szintjeit.
* **Gráfkeresés:** Használ egy `látott` (explored) halmazt, hogy elkerülje a végtelen ciklusokat és a duplikált bejárásokat.
* **Jellemző:** Garantáltan megtalálja a **legrövidebb utat** (azaz a legkevesebb lépésből álló megoldást) súlyozatlan gráfokban.

### Mélységi keresés (DFS - Depth-First Search)

* **Működés:** Egy ágon a lehető legmélyebbre hatol, amíg zsákutcába nem ütközik, vagy célállapotot nem talál. Ezután visszalép, és egy másik ágat kezd felfedezni. Mint amikor egy labirintusban egy folyosón haladsz, ameddig csak tudsz.
* **Adatszerkezet:** **Verem (Stack)** (LIFO - Last-In, First-Out) vagy rekurzió.
* **Fakeresés:** Mélyen bejárja a fa egy ágát, mielőtt visszatérne.
* **Gráfkeresés:** Szintén használ `látott` (explored) halmazt a ciklusok elkerülésére.
* **Jellemző:** Jól használható, ha a megoldások "mélyen" vannak a gráfban, vagy ha az összes lehetséges utat be kell járni.

---

## Naiv Bayes (Naive Bayes)

A **Naiv Bayes osztályozó** egy **felügyelt gépi tanulási algoritmus**, amelyet **klasszifikációs** (besorolási) feladatokra használnak. A **Bayes-tétel** alapul, de egy "naiv" feltételezéssel él:
* Azt feltételezi, hogy az összes bemeneti **jellemző (attribútum) egymástól független**, *feltéve* az osztálykategóriát. Például, ha egy e-mail spam-e (osztály) alapján ítélünk, a "kupon" szó előfordulása független attól, hogy a "nyertes" szó is benne van, ha tudjuk, hogy az e-mail spam.
Bár ez a függetlenségi feltételezés a valóságban ritkán igaz, az algoritmus meglepően jól teljesít sok feladatban, különösen szöveges adatok (pl. spamszűrés, érzelem-elemzés) esetén, mert egyszerű, gyors és hatékony.

---

## Neurális háló (Neural Network)

A **neurális hálózatok** (vagy mesterséges neurális hálózatok, ANN) a **gépi tanulás** egyik formája, amelyet az emberi agy működése inspirált. Összekapcsolt "neuronokból" (vagy csomópontokból) állnak, amelyek rétegekbe rendeződnek:

1.  **Bemeneti réteg:** Fogadja az adatokat.
2.  **Rejtett rétegek:** Feldolgozzák az adatokat, bonyolultabb összefüggéseket tanulnak meg. (Lehet egy vagy több is, ha sok van, akkor "mély tanulásról" beszélünk.)
3.  **Kimeneti réteg:** Előállítja az eredményt (pl. osztálycímke, számérték).

A neuronok közötti kapcsolatoknak **súlyai** vannak, amelyeket az adatok alapján állít be a hálózat a **tanulási folyamat** során. Egy neuron akkor "aktiválódik" (átadja a jelet a következő rétegnek), ha a súlyozott bemenete meghalad egy bizonyos küszöböt. Képesek komplex, nemlineáris kapcsolatok megtanulására, ezért kiválóak például képfelismerésre, természetes nyelvi feldolgozásra és egyéb komplex mintafelismerési feladatokra.

---

## Megerősítéses tanulás (Reinforcement Learning - RL)

A **megerősítéses tanulás** egy olyan gépi tanulási paradigma, ahol egy **ügynök** tanulja meg, hogyan hozzon döntéseket egy **környezetben** azáltal, hogy **jutalmakat** (vagy büntetéseket) kap a végrehajtott **akciókért**. Célja a kumulatív jutalom maximalizálása hosszú távon.

**Főbb komponensek:**

* **Ügynök:** A "tanuló" vagy döntéshozó entitás.
* **Környezet:** Az a világ, amellyel az ügynök interakcióba lép.
* **Állapot (State):** Az ügynök pillanatnyi helyzete vagy leírása a környezetről.
* **Akció (Action):** Az ügynök által végrehajtható cselekedetek.
* **Jutalom (Reward):** Visszajelzés a környezettől minden akció után, ami lehet pozitív vagy negatív.
* **Szabályzat (Policy):** Az ügynök stratégiája, ami megmondja, melyik állapotban milyen akciót hajtson végre.

Az ügynök **próba-szerencse** alapon (trial and error) fedezi fel a környezetet. Akciókat hajt végre, megfigyeli az eredményt (új állapot, jutalom), és frissíti a tudását (például egy Q-táblát vagy egy neurális hálózatot), hogy legközelebb jobb döntést hozzon. Ez a módszer ideális olyan feladatokhoz, ahol nincs előre meghatározott címke (pl. játékok, robotika, autonóm járművek).
