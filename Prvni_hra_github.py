#git add . - stage souborů
#git commit -m"něco" - připravit na odeslání
#git push origin master - pushnout na github
#jednoduché uvozovky- ‚‘

print("\nVítej v mojí únikové hře!")
#room1
volba_cesty = str(input("Jsi v první místnosti, máš na výběr ze dvou cest, z pravé a levé, napiš, kterou si přeješ zvolit. (Pravá/Levá): "))

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
                print("\nSprávná odpověď! Nyní získáváš klíč od dveří s názvem ‘Top secret‘ a vstupuješ do další místnosti.")
                #otázka zda chceš pokračovat
                volba_cesty = str(input("Přeješ si pokračovat na tvé cestě za svobodou? (Ano/Ne): "))
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
                                    kod = str(input("\nSprávná odpověď! Teď jsi nastoupil do výtahu, vyjel o patro výš a před sebou máš dveře, které po tobě chtějí osmimciferný kód. \nOtázka zní, kdy byl upálen Mistr Jan Hus? (DD/MM/YYYY) \nJaký je tedy kód? "))
                                    #správná odpověď
                                    if kod == "06071415":
                                        #room4
                                        print("\nSprávná odpověď! Dveře se odemčely, v místnosti je na papíře napsán kód od levých dveří. Vracíš se tedy o patro níže a vstupuješ do levých dveří.")
                                        odpoved = str(input(""))
                                        break
                                    
                                    
                                    
                                    
                                    #špatná odpověď
                                    else:
                                        print("Špatná odpověď, hra pro tebe končí.")
                                        break
                                
                                #špatná odpověď
                                else:
                                    print("Špatná odpověď, hra pro tebe končí.")
                                    break

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
