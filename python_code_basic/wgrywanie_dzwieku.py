
from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

pocisk_sound = games.load_sound('pocisk.wav') # za pomocą funkcji load_sound - można ładować tylko pliki WAV

games.music.load('temat.mid')

choice = None
while choice != '0':

    print(
        """
        Dźwięk i muzyka
        
        0 - zakończ
        1 - odtwórz dźwięk pocisku
        2 - odtwarzaj cyklicznie dźwiek pocisku
        3 - zatrzymaj odtwarzanie dźwięku pocisku
        4 - odtwórz temat muzyczny
        5 - odtwarzaj cyklicznie temat muzyczny
        6 - zatrzymaj odtwarzanie tematu myzycznego
        """
    )
    choice = input("Wybieram: ")
    print()

    if choice == '0':
        print("Żegnaj")
    elif choice == '1':
        pocisk_sound.play()
        print("Odtworzenie dźwięku pocisku.")
    elif choice == '2':
        loop = int(input("Ile razy chcesz odtworzyć ten dźwięk? "))
        pocisk_sound.play(loop) # jeżeli zamiast 2 wstaiwmy wartość -1, odtwarzanie będzie trwało bez końca
        print("Odtworzenie cykliczne dźwięku.")
    elif choice == '3':
        pocisk_sound.stop()
        print("Zatrzymanie odtwarzania.")
    elif choice == '4':
        games.music.play()
        print("Odtworzenie tematu muzycznego.")
    elif choice == '5':
        loop = int(input("Ile razy chcesz odtworzyć temat muzyczny? "))
        games.music.play(loop)
        print("Odtworzenie cykliczne tematu muzycznego.")
    elif choice == '6':
        games.music.stop()
        print("Zatrzymanie odtwarzania tematu muzycznego.")
    else:
        print(f"Niestety wybór {choice}, nie jest prawidłowym wyborem.")

input("\nAby zakończyć, naciśnij enter.")