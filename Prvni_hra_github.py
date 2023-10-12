#git add . - stage souborů
#git commit - připravit na odeslání
#git push - pushnout na github

print("Vítej v mojí únikové hře")
#room1
volba_cesty = str(input("Jsi v první místnosti, máš na výběr ze dvou cest, z pravé a levé, napiš, kterou si přeješ zvolit. (pravá/levá): "))

#pravá cesta
if volba_cesty == "pravá":
    print("Vybral sis pravou cestu, ")

#levá cesta
elif volba_cesty == "levá":
    print("Vybral sis levou cestu, ")

#špatná volba    
else:
    print("Game over!")
