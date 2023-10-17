#git add . - stage souborů
#git commit -m"něco" - připravit na odeslání
#git push origin master - pushnout na github
#jednoduché uvozovky- ‚‘
import sys


print("\nVítej v mojí únikové hře! Cílem hry je dostat se do trezoru plného peněz a uniknout z budovy.\nV této hře jsou dva trezory, je jen na tobě, ke kterému se vydáš.\nPozorně si zapisuj všechny číselné kódy, budeš je potřebovat pro otevření trezoru.")
#room1
volba_cesty = str(input("Nacházíš se v první místnosti, máš na výběr ze dvou cest, z pravé a levé, každá vede k jednomu trezoru, napiš, kterou si přeješ zvolit. (Pravá/Levá): "))

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
            print("\nJsem rád, že si přeješ pokračovat, nyní si prošel dveřmi a objevil si se v nové místnosti.")
            #úloha číslo 1 (kraje ČR)
            odpoved = int(input("Mám tu pro tebe jednoduchou otázku, kolik krajů má Česká republika? "))
            #správná odpověď
            if odpoved == 14:
                #room3
                print("\nSprávná odpověď! Nyní získáváš klíč od dveří s názvem ‘Top secret‘, vracíš se tedy k nim a vstupuješ do další místnosti.")
                #otázka zda chceš pokračovat
                volba_cesty = str(input("Přeješ si pokračovat na tvé cestě za bohatstím? Už nebude cesty zpět (Ano/Ne): "))
                if volba_cesty == "Ano":
                    #otázka číslo 2 (Einstein)
                    odpoved = str(input("\nMám tu pro tebe již poněkud těžší otázku... Kde se narodil Albert Einstein? Máš na výběr, zvol jedno z písmen: \n a) Rakousko \n b) Německo \n c) Švýcarsko \n Správná odpověď: "))
                    #správná odpověď
                    if odpoved == "b":
                        print("\nSprávně!")
                        while True:
                            volba_cesty = str(input("Před sebou máš dvoje dveře, do kterých si přeješ vstoupit? (Pravé/Levé): "))
                            #pravé dveře
                            if volba_cesty == "Pravé":
                                #otázka číslo 3 (Vodní plocha)
                                odpoved = (str(input("\nJak se jmenuje největší vodní plocha na území ČR? ")))
                                #správná odpověď
                                if odpoved == "Lipno":
                                    #otázka číslo 4 (Jan Hus)
                                    kod = str(input("\nSprávná odpověď! Teď jsi nastoupil do výtahu, vyjel o patro výš a před sebou máš dveře, které po tobě chtějí osmimciferný kód. \nOtázka zní, kdy byl upálen Mistr Jan Hus? (DDMMYYYY) \nJaký je tedy kód? "))
                                    #správná odpověď
                                    if kod == "06071415":
                                        #room4
                                        print("\nSprávná odpověď! Dveře se odemčely, v místnosti je na papíře napsán kód od levých dveří.\nKód:12345\nVracíš se tedy o patro níže a musíš zadat kód od dveří, které jsou hned vedle tebe.")
                                        kód = int(input("kód: "))
                                        #kód od levých dveří
                                        if kód == 12345:
                                            print("\nDveře se otevřely a vstupuješ do dlouhé chodby, na konci vidíš křižovatku se dvěmi možnými cestami.")
                                            volba_cesty = (str(input("Kam si přeješ pokračovat? (Doleva/Rovně): ")))
                                            #Cesta doleva
                                            if volba_cesty == "Doleva":
                                                #otázka číslo 5 (Amerika)
                                                print("\nVydal si se doleva a dále pokračuješ chodbou, na konci vejdeš do místnost, kde na stole leží notebook, ten však vyžaduje čtyřmístné heslo.")
                                                Heslo = int(input("Na obrazovce je napsána otázka: Kdy byla objevena Amerika? (YYYY)\nHeslo: "))
                                                if Heslo == 1492:
                                                    print("\nDostal jsi se do počítače, kde je kus plánku, na kterém je zobrazena část cesty k trezoru, tam je však nakresleno, že se musíš vrátit zpět a pokračovat rovně,\ntam tě čekají další dveře s heslem. Dále tě tam bude čekat další křižovatka, u které když se vydáš doleva, tak dojdeš do místnosti,\nkterá také nikam nevede a už se nebudeš moct vrátit zpět.\nVracíš se tedy zpět a pokračuješ rovně.")
                                                    sys.exit()
                                            
                                            
                                            
                                            
                                            #Cesta rovně
                                            elif volba_cesty == "Rovně":
                                                print("\nPokračuješ tedy rovně a před tebou jsou další bezpečnostní dveře, které chtějí tříciferný kód.")
                                                #otázka číslo 6 (Západořímská říše)
                                                kód = int(input("Kdy se rozpadla Západořímská říše? (YYY): "))
                                                if kód == 476:
                                                    print("Správně!")
                                                    volba_cesty = str(input("Nyní před sebou máš další rozcestí, jedna cesta vede doleva a druhá rovně, na dveřích nalevo je napsáno ‘Trap‘, kam si tedy přeješ pokračovat? (Doleva/Rovně): "))
                                                    #správná cesta
                                                    if volba_cesty == "Rovně":
                                                        print("Správná možnost!")
                                                        sys.exit()
                                                    #špatná cesta (past)
                                                    else:
                                                        print("Měl jsi poslouchat značení, odtud se už nedostaneš.")
                                                        sys.exit()
                                                
                                                
                                                #špatná odpověď
                                                else:
                                                    print("Špatná odpověď")
                                                    sys.exit()

                                            #špatná možnost
                                            else:
                                                print("Špatná možnost")
                                                sys.exit()
                                        
                                        
                                        #špatná odpověď
                                        else:
                                            print("Neumíš ani zadat kód? V tom případě nemá cenu abys pokračoval.")
                                            sys.exit()
                                    
                                    
                                    
                                    
                                    #špatná odpověď
                                    else:
                                        print("Špatná odpověď, hra pro tebe končí.")
                                        sys.exit()
                                
                                #špatná odpověď
                                else:
                                    print("Špatná odpověď, hra pro tebe končí.")
                                    sys.exit()

                            #levé dveře (špatná možtnost)         
                            else:
                                print("\nOd dveří nemáš prozatím kód, musíš tedy pokračovat do pravých dveří.")
                                continue
                                
                            


                    #špatná odpověď
                    else:
                        print("\nŠpatná odpověď! Nyní pro tebe hra končí, program můžeš restartovat a hrát od začátku.")
                        break

                else:
                    print("\nUvidíme se příště") 
                    break 
            #špatná odpověď
            else:
                print("Špatná odpověd, je vidět, že jsi nedával v zeměpise pozor, nyní pro tebe hra končí, program můžeš restartovat a hrát od začátku.")
                break
        #Top secret (špatná možnost)
        else:
            print("\nDveře jsou uzamčeny. Máš jen jednu možnost.")
            
            


#levá cesta
elif volba_cesty == "Levá":
    print("Vybral sis levou cestu, ")

#špatná volba    
else:
    print("Game over!")
