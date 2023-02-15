from collections import deque

elves_energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

total_energy_used = 0
total_toys = 0
counter = 0

while elves_energy and materials:
    elf_energy = elves_energy.popleft()
    if elf_energy < 5:
        continue
    counter += 1
    toy_made = False
    material = materials.pop()
    if counter % 3 != 0 and counter % 5 != 0:
        if elf_energy >= material:
            toy_made = True
            total_toys += 1
            elf_energy -= material
            elf_energy += 1
            total_energy_used += material
            elves_energy.append(elf_energy)
    elif counter % 3 == 0 and counter % 5 == 0:
        if elf_energy >= material * 2:
            toy_made = True
            elf_energy -= material * 2
            total_energy_used += material * 2
            elves_energy.append(elf_energy)
    elif counter % 3 == 0:
        if elf_energy >= material * 2:
            toy_made = True
            total_toys += 2
            elf_energy -= material * 2
            elf_energy += 1
            total_energy_used += material * 2
            elves_energy.append(elf_energy)
    elif counter % 5 == 0:
        if elf_energy >= material:
            toy_made = True
            elf_energy -= material
            total_energy_used += material
            elves_energy.append(elf_energy)
    if not toy_made:
        elf_energy *= 2
        materials.append(material)
        elves_energy.append(elf_energy)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy_used}")
if elves_energy:
    print(f"Elves left: {', '.join([str(i) for i in elves_energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(i) for i in materials])}")