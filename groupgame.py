score = 0

kysymykset = {
    "Onko tuli kuumaa?": {"Kyllä": "Yes"},
    "Onko vesi märkää?": {"Ei": "No"} 
}

while 
    print(kysymys)
    user_answer = input("Vastauksesi: ")

    if user_answer.lower() in [vastaus.lower() for vastaus in vastaukset.keys()]:
        print("Correct/Oikein!")
        score += 1
        kysymys_index += 1
    else:
        print("Väärin! Peli loppuu.")
        break

print(f"\nPisteet: {score}/{len(kysymykset)}") 
