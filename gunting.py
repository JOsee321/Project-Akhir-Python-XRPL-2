import random

# --- 1. FUNCTION (Syarat: Function) ---
def tentukan_pemenang(user, comp):
    """Fungsi untuk mengecek siapa yang menang (Percabangan)"""
    if user == comp:
        return "Seri! 🤝"
    elif (user == "🪨" and comp == "✂️") or \
         (user == "📜" and comp == "🪨") or \
         (user == "✂️" and comp == "📜"):
        return "Kamu Menang! 🎉"
    else:
        return "Kamu Kalah! 🤖"

def main():
    # --- 2. TIPE DATA (Syarat: Statis/Dinamis) ---
    nama = "Jose"                 # String
    pilihan_game = ["🪨", "📜", "✂️"] # List (Dinamis)
    skor_user = 0                 # Integer
    bermain = True                # Boolean

    print(f"Game Gunting Batu Kertas: {nama} ")
    print("🪨 = Batu | 📜 = Kertas | ✂️ = Gunting")

    # --- 3. PERULANGAN (Syarat: Perulangan) ---
    while bermain:
        print(f"\nSkor saat ini: {skor_user}")
        user_input = input("Pilih (1: Batu, 2: Kertas, 3: Gunting, 4: Keluar): ")

        # --- 4. PERCABANGAN (Syarat: Percabangan) ---
        if user_input == "4":
            print("Terima kasih sudah bermain! Sampai jumpa! 👋")
            bermain = False
        elif user_input in ["1", "2", "3"]:
            # Ubah input angka jadi emoji
            index = int(user_input) - 1
            user_pilih = pilihan_game[index]
            
            comp_pilih = random.choice(pilihan_game)
            
            print(f"Kamu: {user_pilih}  VS  Comp: {comp_pilih}")
            
            hasil = tentukan_pemenang(user_pilih, comp_pilih)
            print(hasil)
            
            if "Menang" in hasil:
                skor_user += 1
        else:
            print("Pilihan tidak ada! Pilih angka 1-4.")

# --- 5. EKSEKUSI (Total baris pas sekitar 50-55) ---
if __name__ == "__main__":
    main()