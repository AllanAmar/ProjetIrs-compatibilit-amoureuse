import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Questions et options
questions = [
    "Quel est ton type de film préféré ?",
    "Quelle est ton saison préférée ?",
    "Quel est ton plat préféré ?",
    "Quel est ton passe-temps préféré ?"
]

options = [
    ["Action", "Comédie", "Drame", "Science-fiction", "Amour", "Romance", "Horreur", "PEGI -18"],
    ["Printemps", "Été", "Automne", "Hiver"],
    ["Pizza", "Sushi", "Pâtes", "Salade", "Burgers", "Entrecôtes+Frites", "ChiliChiken"],
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

        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.welcome_popup = tk.Toplevel()
        self.welcome_popup.title("Bienvenue")

        # Charger l'image de fond et redimensionner
        self.background_image = Image.open("cupidon.jpg")
        # Convertir cm en pixels (1 cm = 37.7953 pixels environ)
        width, height = int(16 * 37.7953), int(10 * 37.7953)
        self.background_image = self.background_image.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        # Créer un canevas pour afficher l'image de fond
        self.canvas = tk.Canvas(self.welcome_popup, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Ajouter les widgets sur le canevas
        self.title_text = tk.Label(self.welcome_popup, text="Découvrez votre âme-soeur pour 1.92€ seulement !", fg="red", font=("Helvetica", 18, "bold"), bg="#FFC0CB")
        self.canvas.create_window(300, 20, window=self.title_text)
        self.blink_text()  # Commencer le clignotement du texte

        start_button = tk.Button(self.welcome_popup, text="💘 Démarrer le test de compatibilité 💘", font=("Helvetica", 10, "bold"), command=self.close_welcome_screen)
        self.canvas.create_window(300, 340, window=start_button)
        self.canvas.create_text(300, 365, text="By Allan AMAR, Giovanni PAPARELLA and Sarusan SIVATHASAN", fill="black", font=("Helvetica", 9, "bold"))

    def blink_text(self):
        current_color = self.title_text.cget("fg")
        next_color = "red" if current_color == "white" else "white"
        self.title_text.config(fg=next_color)
        self.welcome_popup.after(300, self.blink_text)

    def close_welcome_screen(self):
        self.welcome_popup.destroy()
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
        # Vérification si tous les champs sont remplis
        if not self.nom1.get() or not self.dob1.get() or not self.pays1.get() or any(not ans.get() for ans in self.answers1):
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis pour la 1ère personne.")
            return

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
        # Vérification si tous les champs sont remplis
        if not self.nom2.get() or not self.dob2.get() or not self.pays2.get() or any(not ans.get() for ans in self.answers2):
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis pour la 2ème personne.")
            return

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

        ttk.Button(self.popup, text="Envoyer", command=self.confirm_payment).grid(row=6, column=0, columnspan=2, pady=20)

    def confirm_payment(self):
        # Vérification si tous les champs sont remplis
        if not self.payment_nom.get() or not self.payment_prenom.get() or not self.payment_card_number.get() or not self.payment_expiration_date.get() or not self.payment_cdv.get():
            messagebox.showwarning("Attention", "Tous les champs de paiement doivent être remplis.")
            return

        response = messagebox.askquestion("Confirmation", "Voulez-vous vraiment payer 1.92€ ?", icon='warning')
        if response == 'yes':
            self.show_results()
        else:
            messagebox.showinfo("Information", "C'est soit tu payes soit ta pas ton résultat")

    def show_results(self):
        self.popup.destroy()
        compatibilite = self.calculate_compatibility()
        self.popup = tk.Toplevel()
        self.popup.title("Résultats de Compatibilité")
        self.popup.configure(bg="#FFC0CB")

        result_text = f"Compatibilité entre {self.person1_data['nom']} et {self.person2_data['nom']} : {compatibilite}%"
        ttk.Label(self.popup, text=result_text, background="#FFC0CB", foreground="red", font=("Helvetica", 14)).pack(pady=20)
        ttk.Button(self.popup, text="Fermer", command=self.popup.destroy).pack(pady=20)

    def calculate_compatibility(self):
        matches = sum(1 for a1, a2 in zip(self.person1_data["answers"], self.person2_data["answers"]) if a1 == a2)
        total_questions = len(self.person1_data["answers"])
        return (matches / total_questions) * 100

if __name__ == "__main__":
    root = tk.Tk()
    app = CompatibiliteApp(root)
    root.mainloop()
