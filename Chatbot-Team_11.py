import random

zufallsantworten = ["Bitte wählen Sie eine der oberen Optionen"]

reaktionsantworten = {"computer/laptops": "Wählen Sie eine der folgenden Optionen: Störung-Laptop, Störung-Peripherie, Störung-Lan/WLAN, Installation/Deinstallation",
                                        "störung-laptop":"Wählen Sie eine der folgende Probleme: Störung-Stromversorgung, ",
                                        "störung-peripherie":"Test",
                                        "störung-lan/wlan": "Test",
                                        "installation/deinstallation": "Test",
                      "mobile-geräte":"Wählen Sie eine der folgenden Optionen: Störung-Smartphone/Tablet, Verlust-Smarthpone/Tablet",
                                        "störung-smartphone/tablet": "Test",
                                        "verlust-smarthpone/tablet": "Test",
                      "telefonie":"Wählen Sie eine der folgenden Optionen: Desktop-Phone/Support, Neuen-Durschwahl",
                                        "desktop-phone/support": "Test",
                                        "neuen-durschwahl": "Test",
                      "drucken/scannen": "Wählen Sie eine der folgenden Optionen: Störung-Drucker, Druckerzubehör-bestellen",
                                        "störung-drucker": "Test",
                                        "druckerzubehör-bestellen": "Test",
                      "bestellung": "Wählen Sie eine der folgenden Optionen: IT-Bestellungen",
                                        "it-bestellungen": "Test",
                      "e-mail": "Wählen Sie eine der folgenden Optionen: Störung-Outlook, Störung-Versand/Empfang, Störung-Mailarchiv, Verteilerliste",
                                        "störung-outlook": "Test",
                                        "störung-versand/empfang": "Test",
                                        "störung-mailarchiv": "Test",
                                        "verteilerliste": "Test",
                      "sicherheit": "Wählen Sie eine der folgenden Optionen: Schadsoftware/Betrugsattacken",
                                        "schadsoftware/betrugsattacken": "Test",
                      "support.kontakt": "Wir sind von 9:00 bis 15:00 unter 49-000-00-00 erreischbar."

                     }

print("Hallo und willkommen zu unserem digitalen Assistenten.")
print("Mit was kann ich heute für Sie behilflich sein?")
print("Bitte wählen Sie eine der folgenden Optionen: ")
print("")
print("|", "Computer/Laptops", "|", "Mobile-Geräte", "|", "Telefonie", "|", "Drucken/Scannen", "|", "Bestellung",
      "|")
print("|", "Support.Kontakt", "|", "E-Mail", "|", "Sicherheit", "|")
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
