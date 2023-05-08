from pojistenec import Pojistenec
import databaze

print("=======================================")
print("        EVIDENCE POJIŠTĚNÝCH           ")
print("=======================================")

volba = "ano"

while volba == "ano":
    print("\n"
          "1 - přidat nového pojištěnce.\n"
          "2 - vyhledat pojišteného dle jména.\n"
          "3 - vypsat všechny pojištené.\n"
          "4 - ukončit aplikaci2.\n")
    
    akce = input("Vyberte volbu, kteráse máý provést:\n")
    vysledek = None

    if akce == "1":
        pridat_jmeno = input("Zadejte jméno\n")
        pridat_prijmeni = input("Zadejte příjmení\n")
        pridat_vek = input("Zadejte věk\n")
        pridat_číslo = input("Zadejte telofonní číslo\n")
        databaze.database.append(Pojistenec(pridat_jmeno, pridat_prijmeni, pridat_vek, pridat_číslo))
        print("Vámi zadané údaje byly uloženy do databáze,\n")
    elif akce == "2":
        hledane_jmeno = input("Zadejte jméno: ")
        hledane_prijmeni = input("Zadejte příjmené: ")
        for item in databaze.database:
            if hledane_jmeno == item.jmeno and hledane_prijmeni == item.prijmeni:
                vysledek = item
                print(vysledek)
        if vysledek == None:
            print("Vámi zadané jméno a přijmení neodpovída jménu v databázi")
    elif akce == "3":
        for item in databaze.database:
            print(item)
    elif akce == "4":
        print("Konec aplikace.")
        volba = False
        exit()
    else :
        print("Zadali jste neplat ou volbu/n")





   





