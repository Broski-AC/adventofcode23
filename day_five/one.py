def seed_to_soil(seed):
    with open("s-to-s_large.txt") as file:
        for line in file:
            dest_str, source_str, r_str = line.split(" ")
            source = int(source_str)
            dest = int(dest_str)
            r_len = int(r_str)

            end_source = source + r_len
            if seed not in range(source, end_source):
                next
            else:
                index = seed - source 
                return dest + index
    # Assumes seed is not in the range, then the values are equivalent
    return seed

def soil_to_fert(soil):
    with open("s-to-f_large.txt") as file:
        for line in file:
            dest_str, source_str, r_str = line.split(" ")
            source = int(source_str)
            dest = int(dest_str)
            r_len = int(r_str)

            end_source = source + r_len
            if soil not in range(source, end_source):
                next
            else:
                index = soil - source 
                return dest + index
    # Assumes soil is not in the range, then the values are equivalent
    return soil


def fert_to_water(fert):
    with open("f-to-w_large.txt") as file:
        for line in file:
            dest_str, source_str, r_str = line.split(" ")
            source = int(source_str)
            dest = int(dest_str)
            r_len = int(r_str)

            end_source = source + r_len
            if fert not in range(source, end_source):
                next
            else:
                index = fert - source 
                return dest + index
    # Assumes soil is not in the range, then the values are equivalent
    return fert

def water_to_light(water):
    with open("w-to-l_large.txt") as file:
        for line in file:
            dest_str, source_str, r_str = line.split(" ")
            source = int(source_str)
            dest = int(dest_str)
            r_len = int(r_str)

            end_source = source + r_len
            if water not in range(source, end_source):
                next
            else:
                index = water - source 
                return dest + index
    # Assumes soil is not in the range, then the values are equivalent
    return water


def light_to_temp(light):
    with open("l-to-t_large.txt") as file:
        for line in file:
            dest_str, source_str, r_str = line.split(" ")
            source = int(source_str)
            dest = int(dest_str)
            r_len = int(r_str)

            end_source = source + r_len
            if light not in range(source, end_source):
                next
            else:
                index = light - source 
                return dest + index
    # Assumes soil is not in the range, then the values are equivalent
    return light

def temp_to_hum(temp):
    with open("t-to-h_large.txt") as file:
        for line in file:
            dest_str, source_str, r_str = line.split(" ")
            source = int(source_str)
            dest = int(dest_str)
            r_len = int(r_str)

            end_source = source + r_len
            if temp not in range(source, end_source):
                next
            else:
                index = temp - source 
                return dest + index
    # Assumes soil is not in the range, then the values are equivalent
    return temp

def hum_to_loc(hum):
    with open("h-to-l_large.txt") as file:
        for line in file:
            dest_str, source_str, r_str = line.split(" ")
            source = int(source_str)
            dest = int(dest_str)
            r_len = int(r_str)

            end_source = source + r_len
            if hum not in range(source, end_source):
                next
            else:
                index = hum - source 
                return dest + index
    # Assumes soil is not in the range, then the values are equivalent
    return hum

def main():
    locations = []

    with open("seeds_large.txt") as file:
        seeds = file.readline()
        seeds_list = seeds.split(" ")
    
        for seed in seeds_list:
            soil_val = seed_to_soil(int(seed))
            # print("Seed: " + str(seed) + " Soil: " + str(soil_val))
            fert_val = soil_to_fert(soil_val)
            # print("Soil: " + str(soil_val) + " Fert: " + str(fert_val))
            water_val = fert_to_water(fert_val)
            # print("Fert: " + str(fert_val) + " Water: " + str(water_val))
            light_val = water_to_light(water_val)
            # print("Water: " + str(water_val) + " Light: " + str(light_val))
            temp_val = light_to_temp(light_val)
            hum_val = temp_to_hum(temp_val)
            loc_val = hum_to_loc(hum_val)

            locations.append(loc_val)
    
    print(min(locations))

if __name__ == "__main__":
    main()