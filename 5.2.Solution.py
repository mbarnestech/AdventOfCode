seed_to_soil_map = {}
soil_to_fertilizer_map = {}
fertilizer_to_water_map = {}
water_to_light_map = {}
light_to_temperature_map = {}
temperature_to_humidity_map = {}
humidity_to_location_map = {}

seed_ranges = []

with open("5.Seeds.txt") as file:
    for line in file:
        nums = [int(num) for num in line.strip().split(' ')]
    for i in range(0, len(nums), 2):
        seed_ranges.append((nums[i], nums[i]+ nums[i+1] - 1))
    seed_ranges = sorted(seed_ranges)

def next_range(input, input_ranges):
    next_seed_ranges = []
    seed_soil_dict = {}
    soils = []
    ns = []

    with open(input) as file:
        nums = []
        
        for line in file:
            soil, seed, num = line.strip().split(' ')
            nums.extend([int(soil), int(seed), int(num)])
        for i in range(0, len(nums), 3):
            next_seed_ranges.append((nums[i+1], nums[i+1]+ nums[i+2] - 1))
            seed_soil_dict[next_seed_ranges[-1]] = (nums[i], nums[i]+nums[i+2]-1)
        print(seed_soil_dict)
    
    next_seed_ranges = sorted(next_seed_ranges)
    next_no = 0
    for x in input_ranges:
        first = x[0]
        last = x[0]
        while last < x[1]:
            last = x[1]
            while first > next_seed_ranges[next_no][1]:
                next_no +=1
            if first < next_seed_ranges[next_no][0] < last:
                last = next_seed_ranges[next_no][0]-1
            elif first < next_seed_ranges[next_no][1] < last:
                last = next_seed_ranges[next_no][1]
                soils.append((seed_soil_dict[next_seed_ranges[next_no]][1] - last + first, seed_soil_dict[next_seed_ranges[next_no]][1]))
            if first == next_seed_ranges[next_no][0]:
                soils.append((seed_soil_dict[next_seed_ranges[next_no]][0], seed_soil_dict[next_seed_ranges[next_no]][0] + last - first))
            elif last == x[1]:
                soils.append((first, last))
            first = last + 1
    soils = sorted(soils)
    ns = [soils[0]]
    for soil in soils[1:]:
        if soil[0] <= ns[-1][1]:
            ns[-1] = (ns[-1][0], soil[1])
        else:
            ns.append(soil)
    return ns

soil_ranges = next_range("5.SeedToSoil.txt", seed_ranges)
fertilizer_ranges = next_range("5.SoilToFertilizer.txt", soil_ranges)
water_ranges = next_range("5.FertilizerToWater.txt", fertilizer_ranges)
light_ranges = next_range("5.WaterToLight.txt", water_ranges)
temperature_ranges = next_range("5.LightToTemperature.txt", light_ranges)
humidity_ranges = next_range("5.TemperatureToHumidity.txt", temperature_ranges)
location_ranges = next_range("5.HumidityToLocation.txt", humidity_ranges)

print(location_ranges)