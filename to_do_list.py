# Lista cu obiective
task = input("Adaugă primul obiectiv: ")

with open("taskuri.txt", "a") as f:
    f.write(task + "\n")

print("Task adăugat cu succes!")