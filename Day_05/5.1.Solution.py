

seeds = set()
soils = set()
fertilizers = set()
waters = set()
lights = set()
temperatures = set()
humidities = set()
locations = set()

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

def make_map_line(line):
    return [int(num) for num in line[:len(line)-1].strip().split()]

def make_dict(input_set, return_set, return_dict, map):
    for num in input_set:
        found = False
        for row in map:
            dest_start, source_start, range_len = [n for n in row]
            if num in range(source_start, source_start + range_len):
                return_dict[num] = dest_start + num - source_start
                return_set.add(return_dict[num])
                found = True
                break
        if not found:
            return_dict[num] = num
            return_set.add(num)

with open("5.Input.txt") as file:
    stage = 0
    for line in file:
        if stage == 0:
            if line[:5] == "seeds":
                nums = line[6:len(line)-1].strip().split()
                seeds = set([int(num) for num in nums])
            if line[:5] == "seed-":
                stage +=1
                map = []
        elif stage == 1:
            if line[0].isdigit():
                map.append(make_map_line(line))
            if line[0].isalpha():
                make_dict(seeds, soils, seed_to_soil, map)
                stage +=1
                map = []
        elif stage == 2:
            if line[0].isdigit():
                map.append(make_map_line(line))
            if line[0].isalpha():
                make_dict(soils, fertilizers, soil_to_fertilizer, map)
                stage +=1
                map = []
        elif stage == 3:
            if line[0].isdigit():
                map.append(make_map_line(line))
            if line[0].isalpha():
                make_dict(fertilizers, waters, fertilizer_to_water, map)
                stage +=1
                map = []
        elif stage == 4:
            if line[0].isdigit():
                map.append(make_map_line(line))
            if line[0].isalpha():
                make_dict(waters, lights, water_to_light, map)
                stage +=1
                map = []
        elif stage == 5:
            if line[0].isdigit():
                map.append(make_map_line(line))
            if line[0].isalpha():
                make_dict(lights, temperatures, light_to_temperature, map)
                stage +=1
                map = []
        elif stage == 6:
            if line[0].isdigit():
                map.append(make_map_line(line))
            if line[0].isalpha():
                make_dict(temperatures, humidities, temperature_to_humidity, map)
                stage +=1
                map = []
        elif stage == 7:
            if line[0].isdigit():
                map.append(make_map_line(line))
            else:
                make_dict(humidities, locations, humidity_to_location, map)


print(min(locations))
