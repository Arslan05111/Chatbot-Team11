import random

zufallsantworten = ["Bitte wählen Sie eine der oberen Optionen"]

reaktionsantworten = {"1": "Wählen Sie eine der folgenden Optionen: Störung-Laptop, Störung-Peripherie, Störung-Lan/WLAN, Installation/Deinstallation",
                                        "störung-laptop":"Wählen Sie eine der folgende Probleme: Störung-Stromversorgung, ",
                                        "störung-peripherie":"Test",
                                        "störung-lan/wlan": "Test",
                                        "installation/deinstallation": "Test",
                      "2":"Wählen Sie eine der folgenden Optionen: Störung-Smartphone/Tablet, Verlust-Smarthpone/Tablet",
                                        "störung-smartphone/tablet": "Test",
                                        "verlust-smarthpone/tablet": "Test",
                      "3":"Wählen Sie eine der folgenden Optionen: Desktop-Phone/Support, Neuen-Durschwahl",
                                        "desktop-phone/support": "Test",
                                        "neuen-durschwahl": "Test",
                      "4": "Wählen Sie eine der folgenden Optionen: Störung-Drucker, Druckerzubehör-bestellen",
                                        "störung-drucker": "Test",
                                        "druckerzubehör-bestellen": "Test",
                      "5": "Wählen Sie eine der folgenden Optionen: IT-Bestellungen",
                                        "it-bestellungen": "Test",
                      "6": "Wählen Sie eine der folgenden Optionen: Störung-Outlook, Störung-Versand/Empfang, Störung-Mailarchiv, Verteilerliste",
                                        "störung-outlook": "Test",
                                        "störung-versand/empfang": "Test",
                                        "störung-mailarchiv": "Test",
                                        "verteilerliste": "Test",
                      "7": "Wählen Sie eine der folgenden Optionen: Schadsoftware/Betrugsattacken",
                                        "schadsoftware/betrugsattacken": "Test",
                      "8": "Wir sind von 9:00 bis 15:00 unter 49-000-00-00 erreischbar."

                     }

print("Hallo und willkommen zu unserem digitalen Assistenten.")
print("Mit was kann ich heute für Sie behilflich sein?")
print("Bitte wählen Sie eine der folgenden Optionen: ")
print("")
print("|", "1-Computer/Laptops", "|", "2-Mobile-Geräte", "|", "3-Telefonie", "|", "4-Drucken/Scannen", "|", "5-Bestellung",
      "|")
print("|", "6-Support.Kontakt", "|", "7-E-Mail", "|", "8-Sicherheit", "|")
print("")
print("Zum beenden bitte 'bye' eintippen")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Ihre Frage/Antwort: ")

    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
        
    print("")

print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")
