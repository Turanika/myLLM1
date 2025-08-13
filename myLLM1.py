"""
13-08-2025
Turan Hajiyeva
myLLM1 –  Desktop-Anwendung für Textübersetzung mit Google Gemini

Dieses Projekt entstand im Rahmen des Mastermoduls des MA Translation Fachübersetzen und Künstliche Intelligenz (SoSe2025) 
an der Johannes Gutenberg-Universität Mainz und wurde eigenständig überarbeitet und erweitert.

Diese Anwendung ermöglicht es, beliebigen Text (max. 150 Wörter) direkt im Fenster einzugeben
und mit Hilfe des Google Gemini Modells in eine der Zielsprachen im Dropdown-Menü zu übersetzen. Die Übersetzung wird
in einem Textfeld angezeigt und kann vor dem Speichern manuell bearbeitet werden.

"""


import os
import pandas as pd
import google.generativeai as genai
from tkinter import Tk, Label, Entry, Button, StringVar, Text, messagebox, END, OptionMenu

def send_to_gemini(prompt: str, model_name: str) -> str:
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return getattr(response, "text", str(response))

def write_to_excel(input_text: str, output_text: str, output_file: str = "output.xlsx"):
    df = pd.DataFrame([{"input": input_text, "output": output_text}])
    if os.path.exists(output_file):
        existing = pd.read_excel(output_file)
        df = pd.concat([existing, df], ignore_index=True)
    df.to_excel(output_file, index=False)

def count_words(text: str) -> int:
    return len(text.strip().split())

def übersetzen():
    input_text = input_box.get("1.0", END).strip()
    target_lang = target_lang_var.get().strip()
    model_name = model_name_var.get().strip() or "gemini-2.5-flash-preview-05-20"
    api_key = api_key_var.get().strip()

    if not input_text:
        messagebox.showwarning("Fehler", "Bitte gib einen Text ein.")
        return

    if count_words(input_text) > 150:
        messagebox.showwarning("Zu viele Wörter", "Maximal 150 Wörter erlaubt.")
        return

    if not api_key:
        if os.path.exists("gemini_api_key.txt"):
            with open("gemini_api_key.txt", "r", encoding="utf-8") as f:
                api_key = f.read().strip()
        else:
            messagebox.showerror("Fehler", "API-Key fehlt.")
            return

    try:
        genai.configure(api_key=api_key)
        prompt = f"Translate this text into {target_lang}: {input_text}"
        translated = send_to_gemini(prompt, model_name)
        output_box.delete("1.0", END)
        output_box.insert("1.0", translated.strip())

    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler bei der Übersetzung:\n{e}")

def speichern():
    input_text = input_box.get("1.0", END).strip()
    edited_output = output_box.get("1.0", END).strip()

    if not input_text or not edited_output:
        messagebox.showwarning("Fehler", "Eingabe oder Ausgabe fehlt.")
        return

    try:
        write_to_excel(input_text, edited_output)
        messagebox.showinfo("Gespeichert", "Übersetzung gespeichert in 'output.xlsx'")
        input_box.delete("1.0", END)
        output_box.delete("1.0", END)
    except Exception as e:
        messagebox.showerror("Fehler", f"Konnte nicht speichern:\n{e}")

# ---------- GUI ----------
root = Tk()
root.title("myLLM1 – Übersetzen, Bearbeiten & Speichern mit Sprachauswahl")

# Texteingabe
Label(root, text="Originaltext (max. 150 Wörter):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_box = Text(root, height=6, width=60, wrap="word")
input_box.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Sprachauswahl (Picklist)
Label(root, text="Zielsprache:").grid(row=2, column=0, sticky="w", padx=10)
target_lang_var = StringVar(value="English")
languages = ["English", "German", "Russian", "Azerbaijani"]
OptionMenu(root, target_lang_var, *languages).grid(row=2, column=1, sticky="w", padx=5)

# Modellname
Label(root, text="Modellname:").grid(row=3, column=0, sticky="w", padx=10)
model_name_var = StringVar(value="gemini-2.5-flash-preview-05-20")
Entry(root, textvariable=model_name_var, width=35).grid(row=3, column=1, padx=5)

# API-Key
Label(root, text="Gemini API-Key:").grid(row=4, column=0, sticky="w", padx=10)
api_key_var = StringVar()
Entry(root, textvariable=api_key_var, width=45, show="*").grid(row=4, column=1, padx=5)

# Übersetzungsausgabe
Label(root, text="Übersetzung (bearbeitbar):").grid(row=5, column=0, padx=10, pady=(10, 2), sticky="w")
output_box = Text(root, height=6, width=60, wrap="word")
output_box.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

# Buttons
Button(root, text="Übersetzen", command=übersetzen).grid(row=7, column=0, pady=10)
Button(root, text="Speichern in Excel", command=speichern).grid(row=7, column=1, pady=10)

root.resizable(False, False)
root.mainloop()

