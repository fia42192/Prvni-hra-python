#git add . - stage souborů
#git commit -m"něco" - připravit na odeslání
#git push origin master - pushnout na github
#jednoduché uvozovky- ‚‘
import sys
import random
import time


print("\nVítej v mojí únikové hře! Hra je převážně zaměřena na všeobecné a dějepisné události formou kvízu. Cílem hry je dostat se do trezoru plného peněz a uniknout z budovy.")
time.sleep(5)
print("V této hře jsou dva trezory, je jen na tobě, ke kterému se vydáš.")
time.sleep(2)
print("Pozorně si zapisuj všechny číselné kódy, budeš je potřebovat pro otevření trezoru, protože heslo od trezoru jsou všechny dosavadní kódy zapsány za sebou.")
time.sleep(6)
#room1
volba_cesty = str(input("Vnikl jsi do již opuštěné budovy, kde jsou ovšem zapomenuté peníze, všechny bezpečnostní opatření jsou stále v provozu, tak do toho!\nNacházíš se v první místnosti, máš na výběr ze dvou cest, z pravé a levé, každá vede k jednomu trezoru, napiš, kterou si přeješ zvolit. (Pravá/Levá): "))

#pravá cesta
if volba_cesty == "Pravá":
    #konec cesty
    print("\nVybral sis pravou cestu, nyní si došel na konec cesty a před tebou jsou dvoje dveře, na jedných je napsáno ‘Top secret‘ a na druhých ‘Entry‘")
    while True:
        #Výběr ze dvou dveří
        volba_cesty = str(input("Nyní si vyber do kterých dveří chceš vstoupit. (Top secret/Entry): "))
        #dveře "Entry" (správná možnost)
        if volba_cesty == "Entry":
            #room2
            time.sleep(1)
            print("\nJsem rád, že si přeješ pokračovat, nyní si prošel dveřmi a objevil si se v nové místnosti.")
            #úloha číslo 1 (kraje ČR)
            odpoved = int(input("Mám tu pro tebe jednoduchou otázku, kolik krajů má Česká republika? "))
            #správná odpověď
            if odpoved == 14:
                #room3
                time.sleep(1)
                print("\nSprávná odpověď! Nyní získáváš klíč od dveří s názvem ‘Top secret‘, vracíš se tedy k nim a vstupuješ do další místnosti.")
                #otázka zda chceš pokračovat
                volba_cesty = str(input("Přeješ si pokračovat na tvé cestě za bohatstím? Už nebude cesty zpět (Ano/Ne): "))
                if volba_cesty == "Ano":
                    #otázka číslo 2 (Einstein)
                    time.sleep(1)
                    odpoved = str(input("\nMám tu pro tebe již poněkud těžší otázku... Kde se narodil Albert Einstein? Máš na výběr, zvol jedno z písmen: \n a) Rakousko \n b) Německo \n c) Švýcarsko \n Správná odpověď: "))
                    #správná odpověď
                    if odpoved == "b":
                        time.sleep(1)
                        print("\nSprávně!")
                        while True:
                            volba_cesty = str(input("Před sebou máš dvoje dveře, do kterých si přeješ vstoupit? (Pravé/Levé): "))
                            #pravé dveře
                            if volba_cesty == "Pravé":
                                #otázka číslo 3 (Vodní plocha)
                                time.sleep(1)
                                odpoved = (str(input("\nJak se jmenuje největší vodní plocha na území ČR? ")))
                                #správná odpověď
                                if odpoved == "Lipno":
                                    #otázka číslo 4 (Jan Hus)
                                    time.sleep(1)
                                    kod = str(input("\nSprávná odpověď! Teď jsi nastoupil do výtahu, vyjel o patro výš a před sebou máš dveře, které po tobě chtějí osmimciferný kód. \nOtázka zní, kdy byl upálen Mistr Jan Hus? (DDMMYYYY) \nJaký je tedy kód? "))
                                    #správná odpověď
                                    if kod == "06071415":
                                        #room4
                                        time.sleep(1)
                                        print("\nSprávná odpověď! Dveře se odemčely, v místnosti je na papíře napsán kód od levých dveří.\nKód: 12345\nVracíš se tedy o patro níže a musíš zadat kód od dveří, které jsou hned vedle tebe.")
                                        kód = int(input("kód: "))
                                        #kód od levých dveří
                                        if kód == 12345:
                                            time.sleep(1)
                                            print("\nDveře se otevřely a vstupuješ do dlouhé chodby, na konci vidíš křižovatku se dvěmi možnými cestami.")
                                            volba_cesty = (str(input("Kam si přeješ pokračovat? (Doleva/Rovně): ")))
                                            #Cesta doleva
                                            if volba_cesty == "Doleva":
                                                #otázka číslo 5 (Amerika)
                                                time.sleep(1)
                                                print("\nVydal si se doleva a dále pokračuješ chodbou, na konci vejdeš do místnost, kde na stole leží notebook, ten však vyžaduje čtyřmístné heslo.")
                                                Heslo = int(input("Na obrazovce je napsána otázka: Kdy byla objevena Amerika? (YYYY)\nHeslo: "))
                                                if Heslo == 1492:
                                                    time.sleep(1)
                                                    print("Dostal jsi se do počítače, kde je kus plánku, na kterém je zobrazena část cesty k trezoru, tam je však nakresleno, že se musíš vrátit zpět a pokračovat rovně.")
                                                    time.sleep(5)
                                                    print("Tam tě čekají další dveře s heslem. Dále tě tam bude čekat další křižovatka, u které když se vydáš doleva, tak dojdeš do místnosti,\nkterá také nikam nevede a už se nebudeš moct vrátit zpět.")
                                                    time.sleep(8)
                                                    print("Vracíš se tedy zpět a pokračuješ rovně.")
                                                    #otázka číslo 6 (Západořímská říše)
                                                    time.sleep(2)
                                                    kód = int(input("Pokračuješ tedy rovně a před tebou jsou další bezpečnostní dveře, které chtějí trojciferný kód.\nOtázka zní: Kdy se rozpadla Západořímská říše? (YYY): "))
                                                    #správná odpověď
                                                    if kód == 476:
                                                        time.sleep(1)
                                                        print("\nSprávně!")
                                                        #rozcestí
                                                        time.sleep(1)
                                                        volba_cesty = str(input("Nyní před sebou máš další rozcestí, jedna cesta vede doleva a druhá rovně, na dveřích nalevo je napsáno ‘Trap‘, kam si tedy přeješ pokračovat? (Doleva/Rovně): "))
                                                        #správná možnost
                                                        if volba_cesty == "Rovně":
                                                            time.sleep(1)
                                                            print("\nSprávná možnost!")
                                                            #otázka číslo 7 (sovětská vojska)
                                                            time.sleep(1)
                                                            kód = int(input("Teď jsi se dostal k dalších dveřím, otázka zní: Ve kterém roce Československý parlament legalizoval pobyt sovětských vojsk v zemi? (YYYY): "))
                                                            #správná odpověď
                                                            if kód == 1968:
                                                                time.sleep(1)
                                                                print("Správná odpověď, nyní pokračuješ chodbou a na konci vcházíš do výtahu a jedeš o 3 patra dolů.")
                                                                while True:
                                                                    #hádání čísla
                                                                    zahadne_cislo = random.randint(1, 5)
                                                                    tve_cislo = int(input("\nNyní jsi došel ke dveřím, kde pro tebe nemám žádnou otázku, ale musíš uhádnout jednociferný kód od dveří (1-5), který se po každém pokusu změní. (číslo nebude potřeba k otevření trezoru), číslo: "))
                                                                    #správné číslo
                                                                    if tve_cislo == zahadne_cislo:
                                                                        time.sleep(1.5)
                                                                        print("\nSprávný kód!")
                                                                        break
                                                                    #špatné číslo, máš další pokus
                                                                    else:
                                                                        time.sleep(1.5)
                                                                        print("\nŠpatná odpověď, zkus to znovu...")
                                                                        continue
                                                                print("Výborně, nyní ti už zbývá jen pár posledních dveří, aby ses dostal k trezoru.")
                                                                time.sleep(4)
                                                                print("Prošel jsi dveřmi a je před tebou chodba, ve které od jedné strany na druhou svítí lasery, které jsou napojeny na bezpečnostní čidla, ")
                                                                time.sleep(6)
                                                                print("na stěně vedle tebe se nachází obrazovka, kde je další otázka: ")
                                                                time.sleep(2)
                                                                #otázka číslo 8 (století páry)
                                                                kód_od_alarmu = str(input("\nKterému století se říká století páry? (vypiš prosím celým slovem, např.patnácté): "))
                                                                #správná odpověď
                                                                if kód_od_alarmu == "devatenácté":
                                                                    print("\nSkvěle! Po celé chodbě zhasly lasery a ty můžeš pokračovat k posledním dveřím!")
                                                                    time.sleep(2)
                                                                    print("\nPoslední otázka:")
                                                                    #otázka číslo 9 (prezident čsr)
                                                                    prezident_csr = str(input("Kdo byl druhým prezidentem ČSR?: "))
                                                                    #správná odpověď
                                                                    if prezident_csr == "Edvard Beneš":
                                                                        time.sleep(1)
                                                                        print("\nSprávně! Dorazil jsi k trezoru!")
                                                                        #správné heslo od trezoru
                                                                        kod_trezoru = int(input("Zadej heslo od trezoru: "))
                                                                        if kod_trezoru == 14060714151234514924761968:
                                                                            time.sleep(2)
                                                                            print("\nGratuluji! vedle sebe vidíš dveře s názvem ‘Exit‘, zde už jen závěrečná otázka...")
                                                                            time.sleep(3)
                                                                            #otázka číslo 10 (závěrečná)
                                                                            posledni_otazka = str(input("\nJe Atlantský oceán největší na Zemi? (Ano/Ne): "))
                                                                            #správná odpověď
                                                                            if posledni_otazka == "Ne":
                                                                                def print_text_slowly(text):
                                                                                    for char in text:
                                                                                        if char != ' ':
                                                                                            print(char, end='', flush=True)
                                                                                            time.sleep(0.1)
                                                                                        else:
                                                                                            print(' ', end='', flush=True)

                                                                                text_to_print = "Úspěšně jsi dokončil hru! Gratuluji!"
                                                                                print_text_slowly(text_to_print)
                                                                                print()
                                                                                sys.exit()
                                                                        
                                                                            #špatná odpověď
                                                                            else:
                                                                                time.sleep(1)
                                                                                ("\nŠkoda, už jsi byl skoro venku...")
                                                                                sys.exit()
                                                                    
                                                                        #špatné heslo
                                                                        else:
                                                                            time.sleep(1)
                                                                            print("\nJá ti říkal ať si je zapisuješ...")
                                                                            sys.exit()
                                                                
                                                                    #špatná odpověď
                                                                    else:
                                                                        time.sleep(1)
                                                                        print("\nŠpatná odpověď.")
                                                                        sys.exit()
                                                                
                                                                
                                                                #špatná odpověď
                                                                else:
                                                                    print("\nŠpatná odpověď.")
                                                                    sys.exit()
                                                                    
                                                            
                                                            #špatná odpověď    
                                                            else:
                                                                print("\nŠpatná odpověď.")
                                                                sys.exit()

                                                        #špatná cesta (past)
                                                        else:
                                                            print("\nMěl jsi poslouchat značení, odtud se už nedostaneš.")
                                                            sys.exit()
                                            
                                            
                                            
                                            
                                            #Cesta rovně
                                            elif volba_cesty == "Rovně":
                                                time.sleep(1)
                                                print("\nPokračuješ tedy rovně a před tebou jsou další bezpečnostní dveře, které chtějí trojciferný kód.")
                                                #otázka číslo 6 (Západořímská říše)
                                                time.sleep(1)
                                                kód = int(input("Kdy se rozpadla Západořímská říše? (YYY): "))
                                                #správná odpověď
                                                if kód == 476:
                                                    time.sleep(1)
                                                    print("\nSprávně!")
                                                    #rozcestí
                                                    time.sleep(1)
                                                    volba_cesty = str(input("\nNyní před sebou máš další rozcestí, jedna cesta vede doleva a druhá rovně, na dveřích nalevo je napsáno ‘Trap‘, kam si tedy přeješ pokračovat? (Doleva/Rovně): "))
                                                    #správná cesta
                                                    if volba_cesty == "Rovně":
                                                        time.sleep(1)
                                                        print("Správná možnost!")
                                                        #otázka číslo 7 (sovětská vojska)
                                                        time.sleep(1)
                                                        kód = int(input("\nTeď jsi se dostal k dalších dveřím, otázka zní: Ve kterém roce Československý parlament legalizoval pobyt sovětských vojsk v zemi? (YYYY): "))
                                                        #správná odpověď
                                                        if kód == 1968:
                                                            time.sleep(1)
                                                            print("Správná odpověď, nyní pokračuješ chodbou a na konci vcházíš do výtahu a jedeš o 3 patra dolů.")
                                                            while True:
                                                                    #hádání čísla
                                                                    zahadne_cislo = random.randint(1, 5)
                                                                    tve_cislo = int(input("\nNyní jsi došel ke dveřím, kde pro tebe nemám žádnou otázku, ale musíš uhádnout jednociferný kód od dveří, který se po každém pokusu změní. (číslo nebude potřeba k otevření trezoru), číslo: "))
                                                                    #správné číslo
                                                                    if tve_cislo == zahadne_cislo:
                                                                        time.sleep(1.5)
                                                                        print("\nSprávný kód!")
                                                                        break
                                                                    #špatné číslo, máš další pokus
                                                                    else:
                                                                        time.sleep(1.5)
                                                                        print("\nŠpatná odpověď, zkus to znovu...")
                                                                        continue
                                                            print("Výborně, nyní ti už zbývá jen pár posledních dveří, aby ses dostal k trezoru.")
                                                            time.sleep(4)
                                                            print("Prošel jsi dveřmi a je před tebou chodba, ve které od jedné strany na druhou svítí lasery, které jsou napojeny na bezpečnostní čidla, ")
                                                            time.sleep(6)
                                                            print("na stěně vedle tebe se nachází obrazovka, kde je další otázka: ")
                                                            time.sleep(2)
                                                            #otázka číslo 8 (století páry)
                                                            kód_od_alarmu = str(input("\nKterému století se říká století páry? (vypiš prosím celým slovem, např.patnácté): "))
                                                            #správná odpověď
                                                            if kód_od_alarmu == "devatenácté":
                                                                time.sleep(1)
                                                                print("\nSkvěle! Po celé chodbě zhasly lasery a ty pokračuješ k posledním dveřím!")
                                                                time.sleep(2)
                                                                print("\nPoslední otázka:")
                                                                #otázka číslo 9 (prezident čsr)
                                                                prezident_csr = str(input("Kdo byl druhým prezidentem ČSR?: "))
                                                                #správná odpověď
                                                                if prezident_csr == "Edvard Beneš":
                                                                    time.sleep(1)
                                                                    print("\nSprávně! Dorazil jsi k trezoru!")
                                                                    #správné heslo od trezoru
                                                                    kod_trezoru = int(input("Zadej heslo od trezoru:"))
                                                                    if kod_trezoru == 1406071415123454761968:
                                                                        time.sleep(2)
                                                                        print("\nGratuluji! vedle sebe vidíš dveře s názvem ‘Exit‘, zde už jen závěrečná otázka...")
                                                                        time.sleep(3)
                                                                        #otázka číslo 10 (závěrečná)
                                                                        posledni_otazka = str(input("\nJe Atlantský oceán největší na Zemi? (Ano/Ne): "))
                                                                        #správná odpověď
                                                                        if posledni_otazka == "Ne":
                                                                            def print_text_slowly(text):
                                                                                for char in text:
                                                                                    if char != ' ':
                                                                                        print(char, end='', flush=True)
                                                                                        time.sleep(0.1)
                                                                                    else:
                                                                                        print(' ', end='', flush=True)

                                                                            text_to_print = "Úspěšně jsi dokončil hru! Gratuluji!"
                                                                            print_text_slowly(text_to_print)
                                                                            print()
                                                                            sys.exit()

                                                                        
                                                                        #špatná odpověď
                                                                        else:
                                                                            time.sleep(1)
                                                                            ("\nŠkoda, už jsi byl skoro venku...")
                                                                            sys.exit()
                                                                    
                                                                    #špatné heslo
                                                                    else:
                                                                        time.sleep(1)
                                                                        print("\nJá ti říkal ať si je zapisuješ...")
                                                                        sys.exit()
                                                                
                                                                #špatná odpověď
                                                                else:
                                                                    time.sleep(1)
                                                                    print("\nŠpatná odpověď.")
                                                                    sys.exit()
                                                                
                                                            #špatná odpověď
                                                            else:
                                                                time.sleep(1)
                                                                print("\nŠpatná odpověď.")
                                                                sys.exit()
                                                            
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        
                                                        #špatná odpoveď
                                                        else:
                                                            time.sleep(1)
                                                            print("\nŠpatná odpověď.")
                                                            sys.exit()

                                                        
                                                    #špatná cesta (past)
                                                    else:
                                                        time.sleep(1)
                                                        print("\nMěl jsi poslouchat značení, odtud se už nedostaneš.")
                                                        sys.exit()
                                                
                                                
                                                #špatná odpověď
                                                else:
                                                    time.sleep(1)
                                                    print("\nŠpatná odpověď.")
                                                    sys.exit()

                                            #špatná možnost
                                            else:
                                                time.sleep(1)
                                                print("\nŠpatná možnost.")
                                                sys.exit()
                                        
                                        
                                        #špatná odpověď
                                        else:
                                            time.sleep(1)
                                            print("\nNeumíš ani zadat kód? V tom případě nemá cenu abys pokračoval.")
                                            sys.exit()
                                    
                                    
                                    
                                    
                                    #špatná odpověď
                                    else:
                                        time.sleep(1)
                                        print("\nŠpatná odpověď, hra pro tebe končí.")
                                        sys.exit()
                                
                                #špatná odpověď
                                else:
                                    time.sleep(1)
                                    print("\nŠpatná odpověď, hra pro tebe končí.")
                                    sys.exit()

                            #levé dveře (špatná možtnost)         
                            else:
                                time.sleep(1)
                                print("\nOd dveří nemáš prozatím kód, musíš tedy pokračovat do pravých dveří.")
                                continue
                                
                            


                    #špatná odpověď
                    else:
                        time.sleep(1)
                        print("\nŠpatná odpověď! Nyní pro tebe hra končí, program můžeš restartovat a hrát od začátku.")
                        break

                else:
                    time.sleep(1)
                    print("\nUvidíme se příště") 
                    break 
            #špatná odpověď
            else:
                time.sleep(1)
                print("\nŠpatná odpověd, je vidět, že jsi nedával v zeměpise pozor, nyní pro tebe hra končí, program můžeš restartovat a hrát od začátku.")
                break
        #Top secret (špatná možnost)
        else:
            time.sleep(1)
            print("\nDveře jsou uzamčeny. Máš jen jednu možnost.")
            
            


#levá cesta
elif volba_cesty == "Levá":
    time.sleep(1)
    print("\nVybral sis levou cestu, projdeš temnou chodbu, zabočíš doprava a před sebou vidíš dveře.")
    time.sleep(3)
    print("jsou však zamčené, pro jejich odemknutí je potřeba odpovědět na následující otázku:")
    time.sleep(3)
    #otázka číslo 1 (OSN)
    print("Kde se nachází hlavní sídlo OSN?:")
    time.sleep(2)
    print("a) v Bruselu")
    time.sleep(0.5)
    print("b) ve Washingtonu")
    time.sleep(0.5)
    print("c) v New Yorku")
    time.sleep(0.5)
    print("d) v Haagu")
    odpoved = str(input("Napiš prosím písmeno: "))
    #správná odpověď
    if odpoved == "c":
        print("\nSprávná odpověď.")
        time.sleep(1)
        print("Nyní jsi prošel dveřmi, na zemi jsi našel papírek s nápisem ‘Door No.5 - password: 24680‘ a pokračuješ dále.")
        time.sleep(5)
        print("\nDošel jsi na rozcestí.")
        time.sleep(1)
        print("Jsi na rozcestí, jsou zde dvoje dveře, jedny s nápisem ‘Warehouse‘ a druhé s nápisem ‘Door No.3‘.")
        while True:
            volba_cesty = input("Vyber si jednu z možností. (Warehouse/Door3): ")
            #správná volba 
            if volba_cesty == "Door3":
                time.sleep(1)
                #room2
                print("\nVešel jsi do dveří a vcházíš do velké místnosti.")
                print("Zde jsou jen jediné dveře, k jejich odemčení odpověz na následujicí otázku:")
                #otázka číslo 2 (Černobyl)
                odpoved = int(input("Ve kterém roce se stala havárie jaderné elektrárny v Černobylu?: "))
                #správná odpověď
                if odpoved == 1986:
                    time.sleep(1)
                    print("\nSprávně.")
                    time.sleep(1)
                    print("\nProcházíš dveřma a před tebou je na televizi napsáno:")
                    time.sleep(3)
                    print("Seřaď následující čísla vzestupně a vytvoř kód: 4, 1, 9, 7 (např.:7914)")
                    time.sleep(2)
                    serazene_cislo = int(input("Pořadí: "))
                    #správný kód
                    if serazene_cislo == 1479:
                        time.sleep(1)
                        print("\nSprávný kód.")
                        time.sleep(1)
                        print("Nyní jsou před tebou dveře číslo 5.")
                        time.sleep(1)
                        #kód, který byl na papírku
                        kod = int(input("Zadej kód: "))
                        #správný kód
                        if kod == 24680:
                            time.sleep(1)
                            print("\nDveře se otevřely a pokračuješ dále.")
                            time.sleep(2)
                            print("Procházíš dlouhou chodbou a na konci je výtah.")
                            time.sleep(2)
                            print("Je však zamčený a pro jeho odemčení je potřeba odpovědět na následujicí otázku: ")
                            time.sleep(4)
                            #otázka číslo 3 (Vltava)
                            odpoved = str(input("Jaká je nejdelší řeka ČR?: "))
                            #správná odpověď
                            if odpoved == "Vltava":
                                time.sleep(1)
                                print("\nSprávná odpověď.")
                                time.sleep(1)
                                #výtah
                                print("\nVcházíš tedy do výtahu a jedeš o dvě patra nahoru.")
                                time.sleep(2)
                                while True:
                                    #rozcestí
                                    print("Zde je rozcestí, máš zde na výběr z levé a pravé cesty, do které se chceš vydat?")
                                    time.sleep(3)
                                    odpoved = str(input("Vyber si cestu. (Levá/Pravá): "))
                                    #pravá cesta
                                    if odpoved == "Pravá":
                                        time.sleep(1)
                                        print("\nPokračuješ tedy doprava, jdeš po schodech dolů a jsou před tebou dveře.")
                                        #otázka číslo 5 (Sametová revoluce)
                                        kod = int(input("\nV jakém roce proběhla Sametová revoluce? "))
                                        #správná odpověď
                                        if kod == 1989:
                                            time.sleep(1)
                                            print("\nSprávně, dveře se otevřely a ty pokračuješ chodbou dále.")
                                            time.sleep(2)
                                            print("Na konci chodby jsou nade dveřmi kamery s pohybovými senzory, které musíš vypnout.")
                                            time.sleep(3)
                                            print("Ty však vypneš tlačítkem ve skříni, která je kousek od tebe směrem doprava.")
                                            time.sleep(3)
                                            print("Do skříně se dostaneš odpovědí na otázku: ")
                                            time.sleep(2)
                                            #otázka číslo 6 (Hlavní Město)
                                            hlavni_mesto = str(input("\nJaké je hlavní město Portugalska? "))
                                            #správná odpověď
                                            if hlavni_mesto == "Lisabon":
                                                time.sleep(1)
                                                print("Správná odpověď! Nyní vypínáš senzory a pokračuješ dveřmi do další místnosti.")
                                                time.sleep(2)
                                                print("Zde pro tebe mám 3 otázky, z každé odpovědi ti vznikne část kódu, který jen spojíš za sebe a vznikne ti tak další kód.")
                                                time.sleep(3)
                                                print("Který pak jen napíšeš za sebe a vznikne ti tak kód od dalších bezpečnostních dveří.")
                                                time.sleep(2)
                                                #kontrolní otázka
                                                odpoved = str(input("\nJsi připraven na otázky? (Ano/Ne): "))
                                                #Jsi připraven
                                                if odpoved == "Ano":
                                                    time.sleep(1)
                                                    print("\nDobře tedy, začneme.")
                                                    time.sleep(1)
                                                    #otázla číslo 7 (Bílá hora)
                                                    bila_hora = int(input("\nVe kterém roce se odehrála bitva na Bíle hoře? "))
                                                    #správná odpověď
                                                    if bila_hora == 1620:
                                                        time.sleep(1)
                                                        print("Správně! Pokračujeme na druhou otázku.")
                                                        #otázka číslo 8 (Titanik)
                                                        time.sleep(1)
                                                        titanik = int(input("\nVe kterém roce se potopil zaoceánský parník Titanik? "))
                                                        #správná odpověď
                                                        if titanik == 1912:
                                                            time.sleep(1)
                                                            print("Správná odpověď, jdeme na třetí otázku.")
                                                            #otázka číslo 9 (Panamský průplav)
                                                            time.sleep(1)
                                                            pruplav = int(input("\nByl Panamský průplav otevřen ve stejném roce, jako začala První světová válka? (1/0): "))
                                                            #správná odpověď
                                                            if pruplav == 1:
                                                                time.sleep(1)
                                                                print("Správně!")
                                                                time.sleep(1)
                                                                #kód
                                                                print("\nNyní musíš spojit tyto tři kódy dohromady a otevřít tak následujicí dveře. (I Tento spojený kód bude potřeba pro otevření trezoru).")
                                                                kod = int(input("Kód: "))
                                                                #správný kód
                                                                if kod == 162019121:
                                                                    time.sleep(1)
                                                                    print("\nSprávný kód! Prošel jsi do další chodby, na konci na tebe čekají poslední dveře.")
                                                                    time.sleep(1)
                                                                    while True:
                                                                        #hádání čísla
                                                                        zahadne_cislo = random.randint(1, 5)
                                                                        tve_cislo = int(input("Nyní jsi došel ke dveřím, kde pro tebe nemám žádnou otázku, ale musíš uhádnout jednociferný kód od dveří (1-5), který se po každém pokusu změní. (číslo nebude potřeba k otevření trezoru), číslo: "))
                                                                        #správné číslo
                                                                        if tve_cislo == zahadne_cislo:
                                                                            time.sleep(1.5)
                                                                            print("\nSprávný kód!")
                                                                            break
                                                                        
                                                                        
                                                                        #špatné číslo, máš další pokus
                                                                        else:
                                                                            time.sleep(1.5)
                                                                            print("\nŠpatné číslo, zkus to znovu.")
                                                                            continue

                                                                    #heslo od trezoru
                                                                    print("Došel jsi až k trezoru! Nyni zadej finální kód.")
                                                                    kod_trezoru = int(input("Kód: "))
                                                                    #správné heslo
                                                                    if kod_trezoru == 19861479246801989162019121162019121:
                                                                        time.sleep(2)
                                                                        print("Získáváš veškerý obsah trezoru a nyní už jen poslední dveře a jsi venku!")
                                                                        time.sleep(3)
                                                                        #otázka číslo 10 (závěrečná)
                                                                        posledni_otazka = str(input("\nJe Antarktida větší než Evropa? (Ano/Ne): "))
                                                                        #správná odpověď
                                                                        if posledni_otazka == "Ano":
                                                                            def print_text_slowly(text):
                                                                                for char in text:
                                                                                    if char != ' ':
                                                                                        print(char, end='', flush=True)
                                                                                        time.sleep(0.1)
                                                                                    else:
                                                                                        print(' ', end='', flush=True)

                                                                            text_to_print = "Úspěšně jsi dokončil hru! Gratuluji!"
                                                                            print_text_slowly(text_to_print)
                                                                            print()
                                                                            sys.exit()

                                                                        
                                                                        
                                                                        
                                                                        
                                                                        #špatná odpověď
                                                                        else:
                                                                            time.sleep(1)
                                                                            print("Škoda, moc nechybělo.")
                                                                            sys.exit()


                                                                    #nesprávný kód
                                                                    else:
                                                                        time.sleep(2)
                                                                        print("\nJá ti říkal ať si ty kódy zapisuješ.")
                                                                        sys.exit()
                                                                
                                                                
                                                                
                                                                #nesprávný kód
                                                                else:
                                                                    time.sleep(1)
                                                                    print("\nNěco jsi pokazil.")
                                                                    sys.exit()

                                                            

                                                            #špatná odpověď
                                                            else:
                                                                time.sleep(1)
                                                                print("\nŠkoda, už jsi byl skoro na konci.")
                                                                sys.exit()

                                                        
                                                        #špatná odpověď
                                                        else:
                                                            time.sleep(1)
                                                            print("\nŠpatná odpověď.")
                                                            sys.exit()


                                                    #špatná odpověď
                                                    else:
                                                        time.sleep(1)
                                                        print("\nŠpatná odpověď.")
                                                        sys.exit()

                                                
                                                #Nejsi připraven
                                                else:
                                                    time.sleep(1)
                                                    print("\nŘíkal jsem si, že ještě nejsi připraven, tak třeba příště...")
                                                    sys.exit()
                                                

                                            
                                            #špatná odpověď
                                            else:
                                                time.sleep(1)
                                                print("\nŠpatná odpověď, spustil jsi alarm a zde pro tebe hra končí...")
                                                sys.exit()


                                        #špatná odpověď
                                        else:
                                            time.sleep(1)
                                            print("\nŠpatná odpověď.")
                                            sys.exit()
    
                                    #levá cesta
                                    else:
                                        time.sleep(1)
                                        print("\nVydal jsi se doleva a před sebou vidíš dveře s nápisem ‘Bonus‘.")
                                        time.sleep(3)
                                        #bonus
                                        bonus = str(input("Přeješ si zodpovědět otázku a dostat bonusové peníze? (Ano/Ne): "))
                                        #chci bonus
                                        if bonus == "Ano":
                                            time.sleep(1)
                                            #otázka číslo 4 (Planeta)
                                            planeta = str(input("\nKterá planeta je nejvzdálenější od Slunce?: "))
                                            #správná odpověď
                                            if planeta == "Neptun":
                                                time.sleep(1)
                                                print("\nSprávná odpověď, získáváš bonus a vracíš se zpět na rozcestí.")
                                                continue
                                            
                                            #špatná odpověď
                                            else:
                                                time.sleep(1)
                                                print("\nŠpatná odpověď, riskovat se ti nevyplatilo.")
                                                sys.exit()
                                        
                                        
                                        #nechci bonus
                                        else:
                                            time.sleep(1)
                                            print("\nVracíš se tedy zpět.")
                                            continue

                            
                            
                            
                             #špatná odpověď
                            else:
                                time.sleep(1)
                                print("\nŠpatná odpověď.")
                                sys.exit()
                        
                        
                        #nesprávný kód
                        else:
                            time.sleep(1)
                            print("\nŠpatný kód, byl přeci na papírku.")
                            sys.exit()
                        
                    
                    #nesprávný kód
                    else:
                        time.sleep(1)
                        print("\nNesprávný kód.")
                        sys.exit()
                
                
                #špatná odpověď
                else:
                    time.sleep(1)
                    print("\nŠpatná odpověď")
                    sys.exit()
            
            #špatná volba - warehouse
            else:
                time.sleep(1)
                #room2
                print("\nProšel jsi dveřmi, ale sklad je prázdný, vracíš se tedy zpět.")


        
    #špatná odpověď
    else:
        time.sleep(1)
        print("\nŠpatná odpověď")
        sys.exit()

#špatná volba    
else:
    time.sleep(1)
    print("\nGame over!")


#readme soubor
#Úniková hra formou kvízu (historie, všeobecné otázky), ve které je cílem dostat se k trezoru s penězi a následně uniknout pryč.
#Ve hře jsou dva trezory, je jen na tobě, k jakému se vydáš. K oběma trezorům vede jiná cesta.
#Pozorně si zapisuj všechny číselné kódy, budeš je potřebovat pro otevření trezoru, protože heslo od trezoru jsou všechny dosavadní kódy zapsány za sebou.
#Jedná se o můj úplně první projekt..
