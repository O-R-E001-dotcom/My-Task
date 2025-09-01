import data
import utils
data.add_stiudents("Ore", "AI Engineering")
data.add_stiudents("Favour", "Ai Development")

for s in data.get_students():
    print(utils.format_students(s))

    # Ore is learning AI Engineering at NCC Digital Industrial park, Abeokuta.
    # Favour is learning Ai Development at NCC Digital Industrial park, Abeokuta.