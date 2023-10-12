#git add . - stage souborů
#git commit -m"něco" - připravit na odeslání
#git push origin master - pushnout na github
#jednoduché uvozovky- ‚‘

print("Vítej v mojí únikové hře")
#room1
volba_cesty = str(input("Jsi v první místnosti, máš na výběr ze dvou cest, z pravé a levé, napiš, kterou si přeješ zvolit. (pravá/levá): "))

#pravá cesta
if volba_cesty == "pravá":
    #konec cesty
    print("Vybral sis pravou cestu, nyní si došel na konec cesty a před tebou jsou dvoje dveře, na jedných je napsáno ‘Exit‘ a na druhých ‘Tvá cesta ještě nekončí‘")
    volba_cesty = str(input("Nyní si vyber do kterých dveří chceš vstoupit (Exit/Tvá cesta ještě nekončí): "))
    while True:
        #Výběr ze dvou dveří
        volba_cesty = str(input("Nyní si vyber do kterých dveří chceš vstoupit (Exit/Tvá cesta ještě nekončí): "))
        #dveře "Tvá cesta ještě nekončí" (správná možnost)
        if volba_cesty == "Tvá cesta ještě nekončí":
            print("Jsem rád, že si přeješ pokračovat, nyní si prošel dveřmi a objevil si se v nové místnosti.")
            #úloha číslo 1 (kraje ČR)
            odpoved = int(input("Mám tu pro tebe jednoduchou otázku, kolik krajů má Česká republika? "))
            #správná odpověď
            if odpoved == 14:
                print("Správná odpověď! Nyní získáváš klíč od dveří s názvem ‘Exit‘ a vstupuješ do další místnosti.")
                break


            #špatná odpověď
            else:
                print("Špatná odpověd, je vidět, že jsi nedával v zeměpise pozor, nyní pro tebe hra končí, program můžeš restartovat a hrát od začátku")
                break
    

        
            
            
        #exit (špatná možnost)
        else:
            print("Dveře jsou uzamčeny. Máš jen jednu možnost")
            


#levá cesta
elif volba_cesty == "levá":
    print("Vybral sis levou cestu, ")

#špatná volba    
else:
    print("Game over!")
