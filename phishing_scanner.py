#Take a URL as Input

url = input("Enter the URL to analyze : ")
 

#Then use requests to retrieve the contents of the page

import requests

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de l'URL : {e}")
        return None

# Example of use
html_content = get_page_content(url)

#use BeautifulSoup to analyze HTML content for phishing indicators

from bs4 import BeautifulSoup

def analyze_content(html):
    if html is None:
        return "Aucun contenu à analyser."

    soup = BeautifulSoup(html, 'lxml')
    forms = soup.find_all('form')  # Search all forms on the page

   # Example of a phishing indicator: presence of suspicious forms
    if forms:
        print(f"{len(forms)} formulaire(s) trouvé(s) sur la page.")
        for form in forms:
            print(form)  # Displays the found form
    else:
        print("Aucun formulaire trouvé.")

# Example of use
analyze_content(html_content)

# create a GUI, you can use Tkinter
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


#List of Known URLs to Test Your Scanner
test_urls = [
    "http://example.com",  #Safe URL
    "http://malicious-link.com",  # Malicious URL (fictitious example)
"http://login-bank.com", 
    "http://secure-login.example.com", # Malicious URL (fictitious example)
    "http://update-password.com", # Malicious URL (fictitious example)
    "http://go0gle.com" #Safe URL
,"http://facebook.com" #Safe URL
]

# For each URL in your list, run your scanner and check if the results are as expected:


for test_url in test_urls:
    print(f"Analyse de l'URL : {test_url}")
    html_content = get_page_content(test_url)
    analyze_content(html_content)
