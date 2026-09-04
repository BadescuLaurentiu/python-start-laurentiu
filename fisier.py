# Să citești și să scrii fișiere
with open("fisier.txt", "w") as f:
    f.write("Salutare, lume!\n")
    f.write("Acesta este un fisier text in care promit solemn ca voi invata Python.\n")
    f.write("Sper sa fie cu noroc de data asta.\n")

with open("fisier.txt", "r") as f:
    print(f.read())