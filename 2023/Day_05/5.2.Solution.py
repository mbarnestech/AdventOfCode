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

def next_range(input_file, input_ranges):
    next_input_ranges = []
    input_output_dict = {}
    output_ranges = []
    sorted_output_ranges = []

    with open(input_file) as file:
        nums = []
        
        for line in file:
            destination, source, num = line.strip().split(' ')
            nums.extend([int(destination), int(source), int(num)])
        for i in range(0, len(nums), 3):
            next_input_ranges.append((nums[i+1], nums[i+1]+ nums[i+2] - 1))
            input_output_dict[next_input_ranges[-1]] = (nums[i], nums[i]+nums[i+2]-1)
    
    next_input_ranges = sorted(next_input_ranges)
    next_no = 0
    for input in input_ranges:
        first = input[0]
        last = input[0]
        while last < input[1]:
            last = input[1]
            while first > next_input_ranges[next_no][1]:
                next_no +=1
            if first < next_input_ranges[next_no][0] < last:
                last = next_input_ranges[next_no][0]-1
            elif first < next_input_ranges[next_no][1] < last:
                last = next_input_ranges[next_no][1]
                output_ranges.append((input_output_dict[next_input_ranges[next_no]][1] - last + first, input_output_dict[next_input_ranges[next_no]][1]))
            if first == next_input_ranges[next_no][0]:
                output_ranges.append((input_output_dict[next_input_ranges[next_no]][0], input_output_dict[next_input_ranges[next_no]][0] + last - first))
            elif last == input[1]:
                output_ranges.append((first, last))
            first = last + 1
    output_ranges = sorted(output_ranges)
    sorted_output_ranges = [output_ranges[0]]
    for destination in output_ranges[1:]:
        if destination[0] <= sorted_output_ranges[-1][1]:
            sorted_output_ranges[-1] = (sorted_output_ranges[-1][0], destination[1])
        else:
            sorted_output_ranges.append(destination)
    return sorted_output_ranges

iteration = 10
print(f'{iteration}/{len(seed_ranges)}')
soil_ranges = next_range("5.SeedToSoil.txt", [seed_ranges[iteration]])
fertilizer_ranges = next_range("5.SoilToFertilizer.txt", soil_ranges)
water_ranges = next_range("5.FertilizerToWater.txt", fertilizer_ranges)
light_ranges = next_range("5.WaterToLight.txt", water_ranges)
temperature_ranges = next_range("5.LightToTemperature.txt", light_ranges)
humidity_ranges = next_range("5.TemperatureToHumidity.txt", temperature_ranges)
location_ranges = next_range("5.HumidityToLocation.txt", humidity_ranges)

with open("5.Location.txt", "a") as file:
    file.write(f"{iteration=}\n")
    file.write(f"{location_ranges=}\n{min(location_ranges)=}\n")