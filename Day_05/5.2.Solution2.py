buckets = set()

with open("5.Seeds.txt") as file:
    for line in file:
        nums = [int(num) for num in line.strip().split(' ')]
    for i in range(0, len(nums), 2):
        buckets.add((nums[i], nums[i]+ nums[i+1] - 1))

def next_range(input_file, buckets):
    new_buckets = set()
    with open(input_file) as file:
        for line in file:
            destination, source, num = [int(n) for n in line.strip().split(' ')]
            for bucket in buckets:
                if bucket[0] <= source <= bucket[1]:
                    # print(f'Ends in bucket: {destination=}, {destination + num - 1=}, {source=}, {source + num - 1=}, {bucket=}')

                    if bucket[0] != source:
                        new_buckets.add((bucket[0], source-1))
                    elif bucket[1] == source:
                        new_buckets.add((destination, destination))
                        bucket = (bucket[0], bucket[1]-1)
                    if bucket[1] <= source + num - 1:
                        new_buckets.add((destination, destination + bucket[1]- source))
                        bucket = (-5,-5)
                    elif bucket[1] > source + num - 1:
                        new_buckets.add((destination, destination + num - 1))
                        bucket = (source + num -1, bucket[1])
                    # print(f'{new_buckets=}, {bucket=}')
                elif bucket[0] <= source + num - 1 <= bucket[1]:
                    # print(f'Begins in Bucket: {destination=}, {destination + num - 1=}, {source=}, {source + num - 1=}, {bucket=}')
                    new_buckets.add(((destination + num - 1) - (source + num - 1) + bucket[0], destination + num - 1))
                    if source + num - 1 == bucket[1]:
                        bucket = (-5,-5)
                    elif source + num - 1 < bucket[1]:
                        bucket = (source + num, bucket[1])
                    # print(f'{new_buckets=}, {bucket=}')

            for bucket in buckets:
                new_buckets.add(bucket)
            new_buckets.discard((-5, -5))
            bucket_list = sorted(list(new_buckets))
            final = [bucket_list[0]]
            for bucket in bucket_list[1:]:
                if final[-1][1] >= bucket[0]:
                    final[-1] = (final[-1][0],bucket[1])
                else:
                    final.append(bucket)
        
            
    return set(final)

soil_ranges = next_range("5.SeedToSoil.txt", buckets)
fertilizer_ranges = next_range("5.SoilToFertilizer.txt", soil_ranges)
water_ranges = next_range("5.FertilizerToWater.txt", fertilizer_ranges)
light_ranges = next_range("5.WaterToLight.txt", water_ranges)
temperature_ranges = next_range("5.LightToTemperature.txt", light_ranges)
humidity_ranges = next_range("5.TemperatureToHumidity.txt", temperature_ranges)
location_ranges = next_range("5.HumidityToLocation.txt", humidity_ranges)

print(f"******{min(location_ranges)=}")    
