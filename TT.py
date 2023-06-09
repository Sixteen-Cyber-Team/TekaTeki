import random
from termcolor import colored
import os

tts = [
    {"soal": "Rel,Rel apa yang paling sakit?", "jawaban": "Rela-in aku pergi bersama yang lain"},
    {"soal": "Siapa yang buat Script Ini?", "jawaban": "Manusia"},
    {"soal": "Apa yang bisa berdiri sendiri namun tidak bisa berjalan?", "jawaban": "rumah"},
    {"soal": "Apa yang bisa terbang tanpa sayap?", "jawaban": "waktu"},
    {"soal": "Apa yang selalu ada di depan mata tetapi tidak pernah terlihat?", "jawaban": "masa depan"}
]

def main():
    os.system('clear')
    tts_acak = random.choice(tts)
    soal = tts_acak["soal"]
    jawaban = tts_acak["jawaban"]

    gambar = """
        _______
      //      \\
     ||       @\\
     ||      \@/
     ||     \@'
     ||    \@'
     ||   \@'
     ||  \@'
     || \@'
     ||@/'
     ||/'
     ||
    /||\\
   //|| \\
  // ||  \\
 //  ||   \\
//   ||    \\
"""

    author = "Author : Arel"
    nama_tts = "TT"

    print(colored(gambar.replace('_', nama_tts), 'green'))
    print(colored("AUTHOR : AREL", 'yellow'))
    print(colored("Selamat Datang Di Game TT", 'yellow'))
    print(colored("Tebak Teka Teki berikut ini:", 'yellow'))
    print(colored(soal, 'cyan'))

    tebakan = input(colored("Jawaban: ", 'magenta'))

    if tebakan.lower() == jawaban:
        print(colored("Selamat, jawaban Anda benar!", 'green'))
    else:
        print(colored("Maaf, jawaban Anda salah. Jawabannya adalah", 'red'), colored(jawaban, 'cyan'))

    ulang = input(colored("Apakah Anda ingin mengulang soal? (y/n) ", 'magenta'))

    if ulang.lower() == 'y':
        main()
    else:
        print(colored(author, 'yellow'))

if __name__ == '__main__':
    main()
