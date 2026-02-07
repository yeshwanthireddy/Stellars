import tkinter as tk
from tkinter import messagebox, scrolledtext

from crew_engine import run_phishguard


# -------- Main App --------

def analyze():

    text = text_box.get("1.0", tk.END).strip()
    url = url_box.get().strip()

    if not text:
        messagebox.showerror("Error", "Enter message text")
        return


    output = run_phishguard(text, url)


    result_box.delete("1.0", tk.END)

    result_box.insert(
        tk.END,
        f"Text Risk   : {output['text']}\n"
    )

    result_box.insert(
        tk.END,
        f"URL Risk    : {output['url']}\n"
    )

    result_box.insert(
        tk.END,
        f"Sender Risk : {output['sender']}\n\n"
    )

    result_box.insert(
        tk.END,
        "AI Decision:\n"
    )

    result_box.insert(
        tk.END,
        output["result"]
    )


# -------- GUI Setup --------

root = tk.Tk()
root.title("PhishGuard - CrewAI Desktop App")
root.geometry("700x600")


# Message Input
tk.Label(root, text="Email / Message").pack()

text_box = scrolledtext.ScrolledText(
    root,
    height=8,
    width=80
)
text_box.pack(pady=5)


# URL Input
tk.Label(root, text="URL (Optional)").pack()

url_box = tk.Entry(root, width=80)
url_box.pack(pady=5)


# Button
tk.Button(
    root,
    text="Analyze",
    command=analyze,
    bg="#007bff",
    fg="white",
    height=2
).pack(pady=10)


# Output
tk.Label(root, text="Result").pack()

result_box = scrolledtext.ScrolledText(
    root,
    height=15,
    width=80
)
result_box.pack(pady=5)


root.mainloop()
