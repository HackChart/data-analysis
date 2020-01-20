# Takes a data mined gen8 file and cleans the data for addition to the standard Kaggle format

def convert_to_previous_gen(filename: str) -> list:
    # List of current elemental types in Pokemon - available through gen8
    accepted_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dark", "dragon", "steel", "fairy"]

    with open(filename) as f:
        gen8_as_list = []
        for line in f:
            gen8_as_list.append(line)

    cleaned = []
    # Strip all extraneous symbols, prep for correct data typing
    for index, row in enumerate(gen8_as_list):
        if index >= 1:
            row = row.strip()
            while "[" in row:
                row = row.replace("[", "")
            while "]" in row:
                row = row.replace("]", "")
            while '"' in row:
                row = row.replace('"', "")
            while "'" in row:
                row = row.replace("'", "")
            while " " in row:
                row = row.replace (" ", "")
            row = row.split(",")
            cleaned.append(row)
        else:
            cleaned.append(row.strip().split(","))

    for i, row in enumerate(cleaned):
        if i >=1:
            for index, item in enumerate(row):
                row[index] = row[index].title()
                if index == 0 and 'g' not in row[index]:
                    row[index] = int(row[index])
                elif index == 3:
                    if item not in accepted_types:
                        row.insert(3, "NaN")
                elif index in range(4, len(row)):
                    try:
                        row[index] = int(row[index])
                    except ValueError:
                        pass
            row.append(8)
            row.append(False)
        print(row)    

    if cleaned[0][0] == "Pokedex Number":
        del(cleaned[0])

    output = []
    for row in cleaned:
        if type(row[0]) == int:
            if row[0] >= 800:
                output.append(row)
        else:
            output.append(row)

    return output

    


        
