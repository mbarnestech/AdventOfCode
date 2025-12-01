with open("2.1.Input.txt") as file:
    with open("2.1.Output.txt", "a") as outputFile:
        total = 0
        for line in file:
            bag = { 'red': 12, 
                    'green': 13, 
                    'blue': 14}
            elements = line.split(': ')
            game = int(elements[0][5:])
            possible = True
            elements[len(elements)-1] = elements[len(elements)-1][:-1]
            rounds = elements[1].split('; ')
            outputFile.write(f'NEW GAME: {game}, {elements} \n')
            for round in rounds:
                bag = { 'red': 12, 
                'green': 13, 
                'blue': 14}
                cubes = round.split(', ')
                for cube in cubes:
                    outputFile.write(f'{bag=}, {cube=}, {round=} \n')
                    detail = cube.split(' ')
                    bag[detail[1]] -= int(detail[0])
                    if bag[detail[1]] < 0:
                        possible = False
                        outputFile.write(f'false: {game} \n')
                        break
                if not possible:
                    break
            if possible:
                total += game
                outputFile.write(f'{game=}, {total=} \n')

        print(total)