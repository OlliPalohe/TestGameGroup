def peli():
    kysymykset = [("Onko tuli kuumaa?": ["Kyllä": "Yes"], ("Onko vesi märkää?": ["Ei": "No"])("Kuinka monta jalkaa on kissalla?", ["neljä", "4"]), ("Missä kaupungissa sijaitsee Näsinneula?", ["Tampere", "Tampereella"]), ("Minä vuonna Suomi itsenäistyi?", ["1917"])]
    
    pelaaja = input("Anna nimi: ")
    score = 0

    while True:
        print("Valitsemalla 1 katso pistetilanne. Valitsemalla 2 lopeta peli.")
        for kysymys, vastaukset in kysymykset:
            vastaus = input(kysymys + " ")

            if vastaus.lower() in [v.lower() for v in vastaukset]:
                print("Oikein!")
                score += 1
            elif vastaus == "1":
                print(f"{pelaaja}n pistetilanne on {score}")
                continue
            elif vastaus == "2":
                print(f"Pisteet yhteensä {score}. Kiitos pelistä, {pelaaja}!")
                return
            else:
                print(f"Väärin. Oikea vastaus on {vastaukset[0]}.")
peli()
