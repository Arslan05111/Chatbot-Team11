import random

zufallsantworten = ["Bitte wählen Sie eine der oberen Optionen"]

reaktionsantworten = {"1": "Wählen Sie eine der folgenden Optionen: Störung-Laptop, Störung-Peripherie, Störung-Lan/WLAN, Installation/Deinstallation",
                                        "störung-laptop":"Wählen Sie eine der folgende Probleme: Windows-hängt, Strom-Störung, Hardware-Defekt ",
                                                        "windows-hängt": "Die Ursache dafür sind die veraltete Treiber, die nicht kompatible mit Programmen sind.Ob Treiber-Probleme vorliegen, können Sie im Geräte-Manager prüfen. Außerdem empfehlen wir, nach Treiber-Aktualisierungen zu suchen und die neusten Windows-Updates zu installieren.",
                                                        "strom-störung": "Überprüfen Sie die Funktion des Netzgerätes,Das Notebook schaltet sich während des Betriebs plötzlich aus:Hier sollte man die Strombuchse oder das Netzteil überprüfen",
                                                        "hardware-defekt": "Bitte beschreiben Sie kurz per email: solutions.it@gmail.com, was genau bei Ihrem Gerät beschädigt wurde. Information wird weiter an unseren Techniker geleitet.",
                                        "störung-peripherie":"Wählen Sie eine der folgende Probleme: Hardware-Defekt, Display-Fehlermeldung, Hardware-Bestellung",
                                                        "hardware-defekt": "Bitte beschreiben Sie kurz per email: solutions.it@gmail.com, was genau bei Ihrem Gerät beschädigt wurde. Information wird weiter an unseren Techniker geleitet.",
                                                        "display-fehlermeldung": "Prüfen Sie den Anschlussmodus, Anzeige „Unbekannter Monitor“: installieren Sie den vom Monitorhersteller bereit gestellten Treiber",
                                                        "hardware-bestellung": "Bitte besuchen Sie unsere Onlineseite unter www.solutions.it.shop.de/search und schicken Sie uns die ausgewählte Hardware, mit entsprechendem Link und Kostenstelle",
                                        "störung-lan/wlan":"Wählen Sie eine der folgende Probleme: Schlechte-Empfang, WLAN-nicht-gefunden",
                                                        "schlechte-empfang": "den Router ausschalten und ein paar Minuten später neu starten., .Stellen Sie sicher, dass die neueste Version der Software installiert ist.",
                                                        "wlan-nicht-gefunden": "Stellen Sie dabei unbedingt sicher, dass die WLAN-Funktion am Router eigeschaltet ist und dass Sie sich mit Ihrem Computer in der Reichweite des WLAN-Signals befinden. ",
                                        "installation/deinstallation": "Folgende Iformation wird für uns benötigt werden, Allgemeine-Software oder Lizenspflichtige-Software, name der Gerätes und schicken Sie uns ein E-mail: soluitons.it@gmail.com",
                      "2":"Wählen Sie eine der folgenden Optionen: Störung-Smartphone/Tablet, Verlust-Smarthpone/Tablet",
                                        "störung-smartphone/tablet": "Wählen Sie eine der folgende Probleme: Gerät-gesperrt, Hardware-Defekt",
                                                        "gerät-gesperrt": "Entsperren kann man das Handy dann, indem man auf die Webseite des Geräte Managers geht und die Google-Kontodaten eingibt. Dort findet ihr die Option Sperren und könnt ein neues Passwort erstellen." ,
                                                        "hardware-defekt": "Bitte beschreiben Sie kurz per email: solutions.it@gmail.com, was genau bei Ihrem Gerät beschädigt wurde. Information wird weiter an unseren Techniker geleitet.",
                                        "verlust-smarthpone/tablet": "Bitte schicken Sie die folgende Information (Name, Modelle Ihres Gerätes und kurze Beschreibung dafür) an uns per E-Mail solutions.it@gmail.com. Achtung, SIM-Karte wird ab jetzt gesperrt.",
                      "3":"Wählen Sie eine der folgenden Optionen: Desktop-Phone/Support, Neuen-Durschwahl",
                                        "desktop-phone/support": "Bitte kontaktieren Sie unsere Support unter +49111111111, damit wir das Problem einmal vor Ort anschauen würden.",
                                        "neuen-durschwahl": "Folgende Iformation wird für uns benötigt werden: Name, der der Durchwahl hinterlegt werden soll und Ort Ihres Arbeitsplatzes. Unsere Kollege werden sich mit Ihnen kontaktieren. ",
                      "4": "Wählen Sie eine der folgenden Optionen: Störung-Drucker, Druckerzubehör-bestellen",
                                        "störung-drucker": "Überprüfen Sie zuerst, ob der Drucker korrekt an Ihren Computer angeschlossen ist.",
                                        "druckerzubehör-bestellen": "Folgende Iformation wird für uns benötigt werden: DEP, Seriennummer oder IP Adresse und welche Tonner farben benötigt werden.",
                      "5": "Wählen Sie eine der folgenden Optionen: IT-Bestellungen",
                                        "it-bestellungen": "Bitte besuchen Sie unsere Onlineseite unter www.solutions.it.shop.de/search und schicken Sie uns die ausgewählte Hardware, mit entsprechendem Link und Kostenstelle",
                      "6": "Wählen Sie eine der folgenden Optionen: Störung-Outlook, Störung-Versand/Empfang, Störung-Mailarchiv, Verteilerliste",
                                        "störung-outlook": "Wählen Sie in Outlook 2016 die Option Datei aus. Wählen Sie Kontoeinstellungen > Kontoeinstellungen aus. Wählen Sie auf der Registerkarte E-Mail Ihr Konto (Profil) und dann Reparieren aus.",
                                        "störung-versand/empfang": "Um dies zu überprüfen, gehen Sie zu den Kontoeinstellungen oder fügen Sie Ihr Konto erneut hinzu. Vergewissern Sie sich, dass die E-Mail-Adresse und das Passwort korrekt sind.",
                                        "störung-mailarchiv": "Bitte nutzen Sie die Online Vault als ersten Workaround. Wir werden Sie zur Behebung des Problems schnellstmöglich kontaktieren.",
                                        "verteilerliste": "Folgende Iformation wird für uns benötigt werden: Name für das Verteiler, wer als Owner eingesetzt werden soll. Unsere Kollegen werden weiter informiert.",
                      "7": "Wählen Sie eine der folgenden Optionen: Schadsoftware/Betrugsattacken",
                                        "schadsoftware/betrugsattacken": "Wählen Sie eine der folgende Probleme: Spam/Fisching",
                                                        "spam/fisching": "Spam-Mails sind unerwünschte E-Mails (z.B. Werbemails). Diese können Schadpogramme enthalten (z.B. gefälschte Bewerbung). Phishing-Mails zielen darauf ab vertrauliche Informationen zu stehlen, indem Sie Anhänge oder Links auf gefährliche Webseiten enthalten.",
                      "8": "Wir sind von 9:00 bis 15:00 unter 49-000-00-00 erreischbar."

                     }

print("Hallo und willkommen zu unserem digitalen Assistenten.")
print("Mit was kann ich heute für Sie behilflich sein?")
print("Bitte wählen Sie eine Nummer der folgenden Optionen: ")
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

print("Wir wünschen Ihnen noch einen schönen Tag. Bis zum nächsten Mal")
