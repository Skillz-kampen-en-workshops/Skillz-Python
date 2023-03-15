# OPDRACHT: gegeven een lijst, waar mogelijk sommige getallen dubbel voorkomen,
# verwijder de duplicaten en geef de lijst terug. Je moet telkens het eerste
# voorkomen van een getal laten staan. Al de andere voorkomens moeten verwijderd
# worden.

def verwijder_duplicaten(lijst):
    """
    Verwijdert alle duplicaten uit een lijst. Het eerste voorkomen van een getal moet blijven staan.
    Al de andere voorkomens moeten verwijderd worden. Gebruik een return statement om de lijst terug te geven.
    :param lijst: een lijst met getallen die mogelijk duplicaten bevat
    :return: een lijst met alle duplicaten verwijderd
    """
    pass


#################################################
# DE CODE HIERONDER TEST JE PROGRAMMA ###########
# NIET AANPASSEN ################################

def check_antwoord(lijst, antwoord):
    try:
        uitkomst = verwijder_duplicaten(lijst.copy())
        assert uitkomst == antwoord
        # print in het groen
        print("\033[92m" + f"OK: verwijder_duplicaten({lijst}) geeft {uitkomst}" + "\033[0m")
    except AssertionError:
        # print in het rood
        print("\033[91m" + f"FOUT: verwijder_duplicaten({lijst}) geeft {uitkomst} maar moet {antwoord} geven" + "\033[0m")
    except Exception as e:
        # print in rood
        print("\033[91m" + f"ERROR: verwijder_duplicaten({lijst}) geeft een fout: {e}" + "\033[0m")
    print("")

# voorbeelden van lijsten
voorbeelden = [
    [], [20], [2, 3, 2, 5, 2, 3, 7],
    [2, 3, 2, 5, 2, 7, 2, 8, 2],
    [2, 2, 5, 4, 7, 8, 1],
    [10, 10, 10, 10, 10]
]

oplossingen = [
    [], [20], [2, 3, 5, 7],
    [2, 3, 5, 7, 8],
    [2, 5, 4, 7, 8, 1],
    [10]
]

for voorbeeld, oplossing in zip(voorbeelden, oplossingen):
    check_antwoord(voorbeeld, oplossing)