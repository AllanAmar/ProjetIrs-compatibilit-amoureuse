import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Questions et options
questions = [
    "Quel est votre type de film préféré ?",
    "Quelle est votre saison préférée ?",
    "Quel est votre plat préféré ?",
    "Quel est votre passe-temps préféré ?"
]

options = [
    ["Action", "Comédie", "Drame", "Science-fiction"],
    ["Printemps", "Été", "Automne", "Hiver"],
    ["Pizza", "Sushi", "Pâtes", "Salade"],
    ["Lecture", "Sport", "Voyage", "Musique"]
]

pays = [
    "France", "Belgique", "Suisse", "Canada", "États-Unis", "Allemagne", "Espagne",
    "Italie", "Royaume-Uni", "Australie", "Japon", "Chine", "Inde", "Brésil"
]

class CompatibiliteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Compatibilité")

        # Informations personnelles
        self.info_frame = ttk.Frame(root)
        self.info_frame.pack(pady=10)

        ttk.Label(self.info_frame, text="Nom de la Personne 1:").grid(row=0, column=0, padx=5, pady=5)
        self.nom1 = ttk.Entry(self.info_frame)
        self.nom1.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Date de Naissance (Personne 1):").grid(row=1, column=0, padx=5, pady=5)
        self.dob1 = ttk.Entry(self.info_frame)
        self.dob1.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Pays (Personne 1):").grid(row=2, column=0, padx=5, pady=5)
        self.pays1 = ttk.Combobox(self.info_frame, values=pays)
        self.pays1.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Nom de la Personne 2:").grid(row=3, column=0, padx=5, pady=5)
        self.nom2 = ttk.Entry(self.info_frame)
        self.nom2.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Date de Naissance (Personne 2):").grid(row=4, column=0, padx=5, pady=5)
        self.dob2 = ttk.Entry(self.info_frame)
        self.dob2.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Pays (Personne 2):").grid(row=5, column=0, padx=5, pady=5)
        self.pays2 = ttk.Combobox(self.info_frame, values=pays)
        self.pays2.grid(row=5, column=1, padx=5, pady=5)

        # Questions
        self.questions_frame = ttk.Frame(root)
        self.questions_frame.pack(pady=10)

        self.answers1 = []
        self.answers2 = []

        for i, (question, opts) in enumerate(zip(questions, options)):
            ttk.Label(self.questions_frame, text=question).grid(row=i, column=0, padx=5, pady=5)
            ans1 = ttk.Combobox(self.questions_frame, values=opts)
            ans1.grid(row=i, column=1, padx=5, pady=5)
            self.answers1.append(ans1)
            ans2 = ttk.Combobox(self.questions_frame, values=opts)
            ans2.grid(row=i, column=2, padx=5, pady=5)
            self.answers2.append(ans2)

        # Bouton de soumission
        self.submit_button = ttk.Button(root, text="Soumettre", command=self.calculate_compatibility)
        self.submit_button.pack(pady=20)

    def calculate_compatibility(self):
        score = 0
        total_questions = len(questions)
        for ans1, ans2 in zip(self.answers1, self.answers2):
            if ans1.get() == ans2.get():
                score += 1

        compatibility_percentage = (score / total_questions) * 100

        result_text = f"Votre score de compatibilité est de {compatibility_percentage:.2f}%"

        # Affichage du résultat
        result_window = tk.Toplevel(self.root)
        result_window.title("Résultat")
        ttk.Label(result_window, text=result_text).pack(pady=20)

def main():
    root = tk.Tk()
    app = CompatibiliteApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
