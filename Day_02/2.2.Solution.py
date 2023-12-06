with open("2.1.Input.txt") as file:
    with open("2.2.Output.txt", "a") as outputFile:
        total = 0
        for line in file:
            most = { 'red': 0, 
                'green': 0,
                'blue': 0}
            elements = line.split(': ')
            game = int(elements[0][5:])
            elements[len(elements)-1] = elements[len(elements)-1][:-1]
            rounds = elements[1].split('; ')
            outputFile.write(f'NEW GAME: {game}, {elements} \n')
            for round in rounds:
                bag = { 'red': 0, 
                'green': 0,
                'blue': 0}
                cubes = round.split(', ')
                for cube in cubes:
                    outputFile.write(f'{bag=}, {cube=}, {round=} \n')
                    detail = cube.split(' ')
                    bag[detail[1]] += int(detail[0])
                most['red'] = max(most['red'], bag['red'])
                most['blue'] = max(most['blue'], bag['blue'])
                most['green'] = max(most['green'], bag['green'])
            power = most['red']*most['blue']*most['green']
            total += power
            outputFile.write(f"{most['red']=}, {most['blue']=}, {most['green']=}, {power=}, {total=} \n")

        print(total)