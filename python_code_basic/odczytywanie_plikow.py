

text_file = open("odczytaj_to.txt", "r")
calosc = text_file.read()
print(calosc)
text_file.close()

#tworzenie nowego pliku i zapisywanie tekstu

text_file2 = open("zapisz_to.txt", "w")

text_file2.writelines("To jest pierszy wers\n")
text_file2.writelines("A to jest drugi wers\n")
text_file2.close()