#Prendre une URL en Entrée

url = input("Entrez l'URL à analyser : ")
 

#Ensuite, utilisez requests pour récupérer le contenu de la page

import requests

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de l'URL : {e}")
        return None

# Exemple d'utilisation
html_content = get_page_content(url)

#utilisez BeautifulSoup pour analyser le contenu HTML et rechercher des indicateurs de phishing 

from bs4 import BeautifulSoup

def analyze_content(html):
    if html is None:
        return "Aucun contenu à analyser."

    soup = BeautifulSoup(html, 'lxml')
    forms = soup.find_all('form')  # Recherche tous les formulaires sur la page

    # Exemple d'indicateur de phishing : présence de formulaires suspects
    if forms:
        print(f"{len(forms)} formulaire(s) trouvé(s) sur la page.")
        for form in forms:
            print(form)  # Affiche le formulaire trouvé
    else:
        print("Aucun formulaire trouvé.")

# Exemple d'utilisation
analyze_content(html_content)

# créer une interface graphique, vous pouvez utiliser Tkinter
import tkinter as tk
from tkinter import messagebox

def scan_url():
    url = entry.get()
    html_content = get_page_content(url)
    analyze_content(html_content)

app = tk.Tk()
app.title("Phishing Link Scanner")

label = tk.Label(app, text="Entrez l'URL à analyser :")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Scanner", command=scan_url)
button.pack()

app.mainloop()


#Liste d'URLs Connues pour Tester Votre Scanner
test_urls = [
    "http://example.com",  # URL sûre
    "http://malicious-link.com",  # URL malveillante (exemple fictif)
"http://login-bank.com",
    "http://192.168.1.1",
    "http://secure-login.example.com",
    "http://update-password.com",
    "http://go0gle.com"
,"http://google.com"
]

# Pour chaque URL dans votre liste, exécutez votre scanner et vérifiez si les résultats sont conformes aux attentes :


for test_url in test_urls:
    print(f"Analyse de l'URL : {test_url}")
    html_content = get_page_content(test_url)
    analyze_content(html_content)
