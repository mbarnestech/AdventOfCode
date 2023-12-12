with open('10.Input.txt') as file:
    with open('10.2.PaddedInput.txt', 'a') as file2:
        file2.write(f"{'#'*281}\n")
        for line in file:
            file2.write(f'#{"&".join(char for char in line[:-1])}#\n')
            file2.write(f"#{'&'*279}#\n")

