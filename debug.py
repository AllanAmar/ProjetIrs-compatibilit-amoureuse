
import tkinter as tk
from tkinter import ttk, messagebox

# Questions et options
questions = [
    "Quel est ton type de film préféré ?",
    "Quelle est ton saison préférée ?",
    "Quel est ton plat préféré ?",
    "Quel est ton passe-temps préféré ?"
]

options = [
    ["Action", "Comédie", "Drame", "Science-fiction", "Amour", "Romance", "Horreur" , "PEGI -18"],
    ["Printemps", "Été", "Automne", "Hiver"],
    ["Pizza", "Sushi", "Pâtes", "Salade", "Burgers","Entrecôtes+Frites","ChiliChiken"],
    ["Lecture", "Sport", "Voyage", "Musique"],
]

pays = [
    "France", "Belgique", "Suisse", "Canada", "États-Unis", "Allemagne", "Espagne",
    "Italie", "Royaume-Uni", "Australie", "Japon", "Chine", "Inde", "Brésil", "Martinique", "Maroc", "Sri-Lanka"
]

class CompatibiliteApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.person1_data = {}
        self.person2_data = {}
        self.answers1 = []
        self.answers2 = []

        self.show_initial_popup()

    def show_initial_popup(self):
        messagebox.showinfo("Information", "Veuillez entrer les informations de la 1ère personne.")
        self.ask_person1_info()

    def ask_person1_info(self):
        self.popup = tk.Toplevel()
        self.popup.title("Informations Personne 1")
        self.popup.configure(bg="#FFC0CB")

        ttk.Label(self.popup, text="Nom:", background="#FFC0CB", foreground="red").grid(row=0, column=0, padx=5, pady=5)
        self.nom1 = ttk.Entry(self.popup)
        self.nom1.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.popup, text="Date de Naissance:", background="#FFC0CB", foreground="red").grid(row=1, column=0, padx=5, pady=5)
        self.dob1 = ttk.Entry(self.popup)
        self.dob1.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.popup, text="Pays:", background="#FFC0CB", foreground="red").grid(row=2, column=0, padx=5, pady=5)
        self.pays1 = ttk.Combobox(self.popup, values=pays, state="readonly")
        self.pays1.grid(row=2, column=1, padx=5, pady=5)

        for i, (question, opts) in enumerate(zip(questions, options)):
            ttk.Label(self.popup, text=f"{question}", background="#FFC0CB", foreground="red").grid(row=3+i, column=0, padx=5, pady=5)
            ans1 = ttk.Combobox(self.popup, values=opts, state="readonly")
            ans1.grid(row=3+i, column=1, padx=5, pady=5)
            self.answers1.append(ans1)

        ttk.Button(self.popup, text="Suivant", command=self.save_person1_info).grid(row=3+len(questions), column=0, columnspan=2, pady=20)

    def save_person1_info(self):
        self.person1_data = {
            "nom": self.nom1.get(),
            "dob": self.dob1.get(),
            "pays": self.pays1.get(),
            "answers": [ans.get() for ans in self.answers1]
        }
        self.popup.destroy()
        self.show_person2_popup()

    def show_person2_popup(self):
        messagebox.showinfo("Information", "Veuillez entrer les informations de la 2ème personne.")
        self.ask_person2_info()

    def ask_person2_info(self):
        self.popup = tk.Toplevel()
        self.popup.title("Informations Personne 2")
        self.popup.configure(bg="#FFC0CB")

        ttk.Label(self.popup, text="Nom:", background="#FFC0CB", foreground="red").grid(row=0, column=0, padx=5, pady=5)
        self.nom2 = ttk.Entry(self.popup)
        self.nom2.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.popup, text="Date de Naissance:", background="#FFC0CB", foreground="red").grid(row=1, column=0, padx=5, pady=5)
        self.dob2 = ttk.Entry(self.popup)
        self.dob2.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.popup, text="Pays:", background="#FFC0CB", foreground="red").grid(row=2, column=0, padx=5, pady=5)
        self.pays2 = ttk.Combobox(self.popup, values=pays, state="readonly")
        self.pays2.grid(row=2, column=1, padx=5, pady=5)

        self.answers2 = []
        for i, (question, opts) in enumerate(zip(questions, options)):
            ttk.Label(self.popup, text=f"{question}", background="#FFC0CB", foreground="red").grid(row=3+i, column=0, padx=5, pady=5)
            ans2 = ttk.Combobox(self.popup, values=opts, state="readonly")
            ans2.grid(row=3+i, column=1, padx=5, pady=5)
            self.answers2.append(ans2)

        ttk.Button(self.popup, text="Soumettre", command=self.save_person2_info).grid(row=3+len(questions), column=0, columnspan=2, pady=20)

    def save_person2_info(self):
        self.person2_data = {
            "nom": self.nom2.get(),
            "dob": self.dob2.get(),
            "pays": self.pays2.get(),
            "answers": [ans.get() for ans in self.answers2]
        }
        self.popup.destroy()
        self.show_payment_popup()

    def show_payment_popup(self):
        self.popup = tk.Toplevel()
        self.popup.title("Paiement")
        self.popup.configure(bg="#FFC0CB")

        ttk.Label(self.popup, text="Veuillez payer 1.92€ pour envoyer votre réponse", background="#FFC0CB", foreground="red").grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        ttk.Label(self.popup, text="Nom:", background="#FFC0CB", foreground="red").grid(row=1, column=0, padx=5, pady=5)
        self.payment_nom = ttk.Entry(self.popup)
        self.payment_nom.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.popup, text="Prénom:", background="#FFC0CB", foreground="red").grid(row=2, column=0, padx=5, pady=5)
        self.payment_prenom = ttk.Entry(self.popup)
        self.payment_prenom.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.popup, text="Numéro de carte:", background="#FFC0CB", foreground="red").grid(row=3, column=0, padx=5, pady=5)
        self.payment_card_number = ttk.Entry(self.popup)
        self.payment_card_number.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.popup, text="Date expiration:", background="#FFC0CB", foreground="red").grid(row=4, column=0, padx=5, pady=5)
        self.payment_expiration_date = ttk.Entry(self.popup)
        self.payment_expiration_date.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self.popup, text="CDV:", background="#FFC0CB", foreground="red").grid(row=5, column=0, padx=5, pady=5)
        self.payment_cdv = ttk.Entry(self.popup)
        self.payment_cdv.grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(self.popup, text="Envoyer", command=self.process_payment).grid(row=6, column=0, columnspan=2, pady=20)

    def process_payment(self):
        # Simuler le traitement du paiement ici
        payment_info = {
            "nom": self.payment_nom.get(),
            "prenom": self.payment_prenom.get(),
            "card_number": self.payment_card_number.get(),
            "expiration_date": self.payment_expiration_date.get(),
            "cdv": self.payment_cdv.get()
        }

        # Afficher une confirmation et passer au calcul de compatibilité
        messagebox.showinfo("Paiement réussi", "Votre paiement a été accepté.")
        self.popup.destroy()
        self.calculate_compatibility()

    def calculate_compatibility(self):
        score = 0
        total_questions = len(questions)
        for ans1, ans2 in zip(self.person1_data['answers'], self.person2_data['answers']):
            if ans1 == ans2:
                score += 1

        compatibility_percentage = (score / total_questions) * 100
        result_text = f"Votre score de compatibilité est de {compatibility_percentage:.2f}%\n\n"

        if compatibility_percentage > 50:
            result_text += "C'est la personne de ta vie chouchou ! "
        else:
            result_text += "Trace ta route, t'es même pas compatible zebi ! "

        messagebox.showinfo("Résultat", result_text)
        self.root.destroy()

def main():
    root = tk.Tk()
    app = CompatibiliteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
