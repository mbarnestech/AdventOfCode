seeds = set()

with open("5.Seeds.txt") as file:
    for line in file:
        nums = [int(num) for num in line.strip().split(' ')]
    for i in range(0, len(nums), 2):
        seeds.add((nums[i], nums[i]+ nums[i+1] - 1))

locations = []

with open("5.HumidityToLocation.txt") as file:
    for line in file:
        location, _, num = [int(n) for n in line.strip().split(' ')]
        locations.append([location, location + num -1])
    locations = sorted(locations)

for location in locations:
    
    


