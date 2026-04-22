# TDEE-kalkylator
# Beräknar användarens Totala Dagliga Energiutgifter
# med Mifflin-St Jeor-formeln och aktivitetsnivå

# Funktioner
def hamta_kon():
    """
    Frågar användaren om kön via en meny.
    Returnerar: str: 'man' eller 'kvinna' beroende på användarens val.
    Felhantering sker om användaren skriver något annat än 1 eller 2,
    då visas ett felmeddelande och användaren får försöka igen.
    """
    while True:
        print("Välj kön:")
        print("1. Man")
        print("2. Kvinna")
        val = input("Ange ditt val 1 eller 2 : ")
        if val == "1":
            return "Man"
        elif val == "2":
            return "Kvinna"
        else:
            print("Ogiltigt val. Välj 1 eller 2.")


def hamta_vikt():
    """
    Frågar användaren om vikt i kilogram.
    Returnerar: float: vikt i kg, alltid positiv.
    Felhantering sker om användaren skriver bokstäver eller negativt tal,
    då visas ett felmeddelande och användaren får försöka igen.
    """
    while True:
        try:
            vikt = float(input("Ange din vikt i kg: "))
            if vikt > 0:
                return vikt
            else:
                print("Vikt måste vara ett positivt tal.")
        except ValueError:
            print("Ogiltig inmatning. Vänligen ange en giltig vikt.")


def hamta_langd(): 
    """
    Frågar användaren om längd i centimeter.
    Returnerar: float: längd i cm, alltid positiv.
    Felhantering sker om användaren skriver bokstäver eller negativt tal,
    då visas ett felmeddelande och användaren får försöka igen.
    """ 
    while True:
        try:
            langd = float(input("Ange din längd i cm: "))
            if langd > 0:
                return langd
            else:
                print("Längd måste vara ett positivt tal.")
        except ValueError:
            print("Ogiltig inmatning. Vänligen ange en giltig längd.")


def hamta_alder():
    """
    Frågar användaren om ålder i år.
    Returnerar: int: ålder i år, alltid positivt heltal.
    Felhantering sker om användaren skriver bokstäver eller negativt tal,
    då visas ett felmeddelande och användaren får försöka igen.
    """
    while True:
        try:
            alder = int(input("Ange din ålder i år: "))
            if alder > 0:
                return alder
            else:
                print("Ålder måste vara ett positivt heltal.")
        except ValueError:
            print("Ogiltig inmatning. Vänligen ange en giltig ålder.")

def hamta_aktivitetsniva():
    """
    Frågar användaren om aktivitetsnivå via en meny.
    Returnerar: tuple: (aktivitetsfaktor (float), aktivitetsbeskrivning (str))
    Felhantering sker om användaren skriver något annat än 1-5,
    då visas ett felmeddelande och användaren får försöka igen.
    """
    while True:
        print("Välj din aktivitetsnivå:")
        print("1. Stillasittande (liten eller ingen träning)")
        print("2. Lätt aktiv (lätt träning/sport 1-3 dagar/vecka)")
        print("3. Måttligt aktiv (måttlig träning/sport 4-5 dagar/vecka)")
        print("4. Mycket aktiv (hård träning/sport 6-7 dagar/vecka)")
        print("5. Extremt aktiv (mycket hård träning/sport & fysiskt jobb eller träning 2x/dag)")
        val = input("Ange ditt val (1-5): ")
        if val == "1":
            return 1.2, "Stillasittande (liten eller ingen träning)"
        elif val == "2":
            return 1.375, "Lätt aktiv (1-3 dagar/vecka)"
        elif val == "3":
            return 1.55, "Måttligt aktiv (4-5 dagar/vecka)"
        elif val == "4":
            return 1.725, "Mycket aktiv (6-7 dagar/vecka)"
        elif val == "5":
            return 1.9, "Extremt aktiv (2x/dag eller mycket fysisk aktivitet)"
        else:
            print("Ogiltigt val. Välj ett nummer mellan 1 och 5.")

def berakna_BMR(kon, vikt, langd, alder):
    """
    Beräknar Basal Metabolic Rate (BMR) med Mifflin-St Jeor-formeln.
    Parametrar:
        kon (str): 'man' eller 'kvinna'
        vikt (float): vikt i kg
        langd (float): längd i cm
        alder (int): ålder i år
    Returnerar: float: BMR i kcal
    """
    if kon == "man":
        BMR = 10 * vikt + 6.25 * langd - 5 * alder + 5
    else:
        BMR = 10 * vikt + 6.25 * langd - 5 * alder - 161
    return BMR

def berakna_TDEE(BMR, aktivitetsfaktor):
    """
    Beräknar Totala Dagliga Energiutgifter (TDEE).
    Parametrar:
        BMR (float): Basal Metabolic Rate i kcal
        aktivitetsfaktor (float): aktivitetsfaktor baserat på användarens val
    Returnerar: float: TDEE i kcal
    """
    TDEE = BMR * aktivitetsfaktor
    return TDEE

def hamta_mal():
    """
    Frågar användaren om mål med sin kost (viktminskning, underhåll eller viktökning).
    Returnerar: str: 'viktminskning', 'underhåll' eller 'viktökning' beroende på användarens val.
    Felhantering sker om användaren skriver något annat än 1-3,
    då visas ett felmeddelande och användaren får försöka igen.
    """
    while True:
        print("\nVad är ditt mål med din kost?")
        print("1. Viktminskning")
        print("2. Underhåll")
        print("3. Viktökning")
        val = input("Ange ditt val (1-3): ")
        if val == "1":
            return "viktminskning"
        elif val == "2":
            return "underhåll"
        elif val == "3":
            return "viktökning"
        else:
            print("Ogiltigt val. Välj ett nummer mellan 1 och 3.")

def justera_kalorier(TDEE, mal):
    """
    Justerar TDEE baserat på användarens mål.
    Parametrar:
        TDEE (float): Totala Dagliga Energiutgifter i kcal
        mal (str): 'viktminskning', 'underhall' eller 'viktökning'
    Returnerar: float: justerade kalorier i kcal
    """
    if mal == "viktminskning":
        return TDEE - 500  # Minska 500 kcal för viktminskning
    elif mal == "viktökning":
        return TDEE + 500  # Öka 500 kcal för viktökning
    else:
        return TDEE  # Ingen justering för underhåll

# Huvudprogram med while-loop
print("Välkommen till TDEE-kalkylatorn!")
print("Denna kalkylator hjälper dig att beräkna ditt TDEE (Totala Dagliga Energiutgifter) baserat på kön, ålder, vikt, längd och aktivitetsnivå.\n")

# Skapa tom lista för att spara flera personers data
personer = []

while True:
    # Hämta användarens uppgifter
    kon = hamta_kon()
    vikt = hamta_vikt()
    langd = hamta_langd()
    alder = hamta_alder()
    aktivitetsfaktor, aktivitetsbeskrivning = hamta_aktivitetsniva()

    # Beräkna
    BMR = berakna_BMR(kon, vikt, langd, alder)
    TDEE = berakna_TDEE(BMR, aktivitetsfaktor)

    # Skapa en dictionary som innehåller all data för en person
    person = {
    "kon": kon,
    "vikt": vikt,
    "langd": langd,
    "alder": alder,
    "aktivitetsbeskrivning": aktivitetsbeskrivning,
    "BMR": BMR,
    "TDEE": TDEE
    }
    # Lägg till dictionaryn i listan över personer
    personer.append(person)

    # Skriv ut resultat
    print("\n--- Resultat ---")
    print(f"Kön: {kon}")
    print(f"Vikt: {vikt} kg, Längd: {langd} cm, Ålder: {alder} år")
    print(f"Aktivitetsnivå: {aktivitetsbeskrivning}")
    print(f"BMR: {BMR:.2f} kcal – energi kroppen behöver i vila per dag")
    print(f"TDEE: {TDEE:.2f} kcal – total energi inklusive fysisk aktivitet kroppen behöver per dag")
    print("----------------\n")


    # MENYLOOP
    while True:
        print("\nVad vill du göra nu?")
        print("1. Justera kalorier baserat på mål för senaste personen")
        print("2. Lägg till en ny person")
        print("3. Visa alla personers data")
        print("4. Avsluta programmet")

        val = input("Ange ditt val (1-4): ")

        if val == "1":
            mal = hamta_mal()
            kalorimal = justera_kalorier(personer[-1]["TDEE"], mal)
            print(f"Rekommenderat kaloriintag för {mal}: {kalorimal:.2f} kcal")

        elif val == "2":
            print("\n--- Lägg till en ny person ---")
            break  # Bryt MENYLOOPEN → huvudloopen startar om och sparar ny person

        elif val == "3":
            # Säkerhetskontroll: listan är aldrig tom i nuvarande flöde
            # men detta gör koden robust om programmet byggs ut i framtiden
            if not personer:
                print("Inga personer sparade ännu, lägg till en först")
            else:
                print("\n--- Alla sparade personer ---")
                # Loopa igenom alla sparade personer
                # enumerate() ger två värden: i = index, p = personen (dictionaryn)
                # i används för att skriva ut "Person 1", "Person 2" osv
                for i, p in enumerate(personer):
                    print(f"\nPerson {i+1}")
                    print(f"Kön: {p['kon']}")
                    print(f"Ålder: {p['alder']} år")
                    print(f"Vikt: {p['vikt']} kg")
                    print(f"Längd: {p['langd']} cm")
                    print(f"BMR: {p['BMR']:.2f} kcal")
                    print(f"TDEE: {p['TDEE']:.2f} kcal")
                    print(f"Aktivitetsnivå: {p['aktivitetsbeskrivning']}")

        elif val == "4":
            print("Tack för att du använde TDEE-kalkylatorn!")
            exit()

        else:
            print("Ogiltigt val, försök igen.")