import tkinter as tk
from tkinter import messagebox

# İşlem fonksiyonu
def islem_yap():
    try:
        # Kullanıcıdan inputları al
        sayi1 = float(entry1.get())
        sayi2 = float(entry2.get())
        islem = operation_var.get()

        # İşlemi kontrol et
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
            else:
                messagebox.showerror("Hata", "Bir sayı 0'a bölünemez!")
                return
        else:
            messagebox.showerror("Hata", "Geçersiz işlem seçildi!")
            return

        # Sonucu ekranda göster
        result_label.config(text=f"Sonuç: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")

# Pencere oluştur
pencere = tk.Tk()
pencere.title("Tkinter Hesap Makinesi")
pencere.geometry("300x300")

# Kullanıcı girişleri
label1 = tk.Label(pencere, text="Birinci Sayı:")
label1.pack()

entry1 = tk.Entry(pencere)
entry1.pack()

label2 = tk.Label(pencere, text="İkinci Sayı:")
label2.pack()

entry2 = tk.Entry(pencere)
entry2.pack()

# İşlem seçimi
operation_var = tk.StringVar(value="+")  # Varsayılan işlem
operation_menu = tk.OptionMenu(pencere, operation_var, "+", "-", "*", "/")
operation_menu.pack()

# Hesapla butonu
hesapla_button = tk.Button(pencere, text="Hesapla", command=islem_yap)
hesapla_button.pack()

# Sonuç etiketi
result_label = tk.Label(pencere, text="Sonuç: ")
result_label.pack()

# Pencereyi çalıştır
pencere.mainloop()