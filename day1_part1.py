# ADVENT OF CODE 2022: Day 1, Part 1

def main():

    textFile = open(r"C:\Users\...")

    # Array that will store the calories carried by each Elf:
    elves = [0]
    i = 0                # Index for an Elf.

    for lineX in textFile:
        # New Line: We index the next Elf.
        if (lineX == "\n"):
            i = i+1;
            elves.append(0)
        
        else:
            caloriesLine = int(lineX)
            # Update the calories of the indexed Elf:
            if (caloriesLine>0):
                elves[i] += caloriesLine

    textFile.close()

    return max(elves)


print(main())
