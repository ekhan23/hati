import tkinter as tk

class HeartApp:
    def __init__(self, root):
        self.root = root
        root.title("Love")
        root.geometry("360x240")
        root.resizable(False, False)

        self.size = 30
        self.grow = True

        self.label = tk.Label(root, text="❤️", font=("Segoe UI Emoji", self.size))
        self.label.pack(expand=True)

        self.entry = tk.Entry(root, justify="center")
        self.entry.insert(0, "Masukkan nama")
        self.entry.pack(pady=5)

        btn = tk.Button(root, text="Kirim Cinta 💌", command=self.kirim)
        btn.pack(pady=5)

        self.animate()

    def animate(self):
        # animation: ping-pong size
        if self.grow:
            self.size += 2
            if self.size >= 58:
                self.grow = False
        else:
            self.size -= 2
            if self.size <= 30:
                self.grow = True
        self.label.config(font=("Segoe UI Emoji", self.size))
        self.root.after(120, self.animate)

    def kirim(self):
        nama = self.entry.get().strip()
        if not nama:
            nama = "Sayang"
        msg = f"Aku sayang kamu, {nama} ❤️"
        popup = tk.Toplevel(self.root)
        popup.title("Pesan")
        tk.Label(popup, text=msg, font=("Arial", 14)).pack(padx=16, pady=16)
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=(0,12))

if __name__ == "__main__":
    root = tk.Tk()
    app = HeartApp(root)
    root.mainloop()