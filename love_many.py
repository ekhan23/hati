import random
import os

phrases = [
    "kamu adalah alasan aku tersenyum",
    "setiap hari bersamamu itu spesial",
    "hatiku selalu untukmu",
    "kamu luar biasa apa adanya",
    "aku kangen kamu",
    "bakal selalu jaga kamu"
]

def make_messages(name, n=10, out_dir="love_cards"):
    os.makedirs(out_dir, exist_ok=True)
    for i in range(1, n+1):
        p = random.choice(phrases)
        text = f"Untuk: {name}\nPesan #{i}\n\n{p}\n\n— Dari seseorang yang sayang\n"
        filename = os.path.join(out_dir, f"card_{i:02d}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"{n} pesan dibuat di folder '{out_dir}'")

if __name__ == "__main__":
    nama = input("Nama penerima: ").strip() or "Sayang"
    jumlah = input("Berapa banyak pesan? (default 10): ").strip()
    try:
        jumlah = int(jumlah) if jumlah else 10
    except:
        jumlah = 10
    make_messages(nama, jumlah)