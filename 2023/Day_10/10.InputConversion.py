with open('10.Input.txt') as file:
    with open('10.PaddedInput.txt', 'a') as file2:
        file2.write(f"{'.'*142}\n")
        for line in file:
            file2.write(f'.{line[:-1]}.\n')
        file2.write(f"{'.'*142}\n")

