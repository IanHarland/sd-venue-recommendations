### NAME, LOCATION, SIZE, STYLE, ADDRESS ###

venues = [['Music Box', 'downtown', 'large', 'touring bands', '1337 India St, San Diego, CA 92101'], ['The Merrow', 'Hillcrest', 'medium', 'local artists', '1271 University Ave, San Diego, CA 92103'], ['Humphrey\'s By the Bay', 'point loma', 'ampitheater', 'touring bands', '2241 Shelter Island Dr, San Diego, CA 92106'], ['The Rady Shell', 'downtown', 'ampitheater', 'classical', '222 Marina Park Way, San Diego, CA 92101'], ['The Observatory', 'North Park', 'large', 'touring bands', '2891 University Ave, San Diego, CA 92104'], ['The House of Blues', 'downtown', 'large', 'touring bands', '1055 Fifth Ave, San Diego, CA 92101'], ['Quartyard', 'downtown', 'Medium(outdoors)', 'local artists', '1301 Market St, San Diego, CA 92101'], ['Brick By Brick', 'downtown', 'medium', 'metal', '1130 Buenos Ave, San Diego, CA 92110'], ['Dizzy\'s', 'downtown', 'medium', 'jazz', '1717 Morena Blvd, San Diego, CA 92110'], ['SOMA', 'point loma', 'large', 'punk', '3350 Sports Arena Blvd suite I, San Diego, CA 92110'], ['The Casbah', 'downtown', 'medium', 'rock', '2501 Kettner Blvd, San Diego, CA 92101'], ['Patrick\'s Gaslamp Pub', 'downtown', 'small', 'blues', '428 F St, San Diego, CA 92101'], ['Blackrail Kitchen & Bar', 'carlsbad', 'medium', 'jazz', '6981 El Camino Real, Carlsbad, CA 92009'], ['Seven Grand', 'north park', 'small', 'local artists', '3054 University Ave, San Diego, CA 92104'], ['Queen Bees Art and Cultural Center', 'north park', 'medium', 'local artists', '3925 Ohio St, San Diego, CA 92104'], ['The Kraken', 'cardiff', 'small', 'rock', '2531 S Coast Hwy 101, Cardiff, CA 92007'], ['Belly Up', 'solana beach', 'large', 'touring bands', '143 S Cedros Ave, Solana Beach, CA 92075'], ['Mr. Peabody\'s', 'encinitas', 'small', 'local artists', '136 Encinitas Blvd, Encinitas, CA 92024'], ['The Roxy', 'encinitas', 'medium', 'local artists', '517 S Coast Hwy 101, Encinitas, CA 92024'], ['1st St. Bar', 'encinitas', 'small', 'rock', '656 S Coast Hwy 101, Encinitas, CA 92024'], ['The Jazzy Wishbone', 'oceanside', 'small', 'jazz', '234 S Coast Hwy, Oceanside, CA 92054'], ['The Jazz Lounge', 'college area', 'small', 'jazz', '6818 El Cajon Blvd, San Diego, CA 92115'], ['Tio Leo\'s', 'downtown', 'medium', 'jazz', '5302 Napa St, San Diego, CA 92110'], ['North Island Credit Union Ampitheater', 'chula vista', 'ampitheater', 'touring bands', '2050 Entertainment Cir, Chula Vista, CA 91911'], ['Soda Bar', 'city heights', 'medium', 'local artists', '3615 El Cajon Blvd, San Diego, CA 92104'], ['Kensington Club', 'Kensington', 'medium', 'local artists', '4079 Adams Ave, San Diego, CA 92116']]

### BUILD ATTRIBUTE LISTS ###

names = []
locations = []
sizes = []
styles = []
addresses = []

for venue in venues:
    names.append(venue[0])
    if venue[1] not in locations:
        locations.append(venue[1].upper())
    if venue[2] not in sizes:
        sizes.append(venue[2].upper())
    if venue[3] not in styles:
        styles.append(venue[3].upper())
    addresses.append(venue[4])

attributes = [names, locations, sizes, styles, addresses]
attributes_string_list = ['names', 'location', 'venue size', 'musical style', 'addresses']

### VENUES CLASS TO MAKE METHODS ###

class Venues:

    def __init__(self, venues):
        self.name = "Venues"
        self.venues = venues
    
    def choose_attribute_index(self):
        user_choice = input("\nHow would you like to search?\n\n1 - Venue Location\n2 - Venue Size\n3 - Musical Style\n\n: ")
        while (user_choice.isdigit() == False) or int(user_choice)<1 or int(user_choice) > 3:
            user_choice = input("\nType 1, 2, or 3, then press Enter\n\n: ")
        user_choice = int(user_choice)
        return user_choice
    
    def choose_attribute(self, index):
        att_string = ""
        count = 1
        for item in attributes[index]:
            att_string += '\n' + str(count) + ' - ' + item
            count += 1
        user_choice = input(f"\nChoose one of the following options:\n{att_string}\n: ")
        while (user_choice.isdigit() == False) or int(user_choice)<1 or int(user_choice) > (count - 1):
            user_choice = input(f"\nType 1 - {count - 1}, then press Enter\n\n: ")
        user_choice = int(user_choice)
        return user_choice
    
    def choose_attribute_item(self, index):
        user_input_1 = input(f"\n\nType the first few letters of the {attributes_string_list[index]} you would like to search for:\n\n").upper()
        choices_list = []
        choices_string = ''
        count = 1
        for item in attributes[index]:
            if len(item) >= len(user_input_1):
                if user_input_1 == item[:len(user_input_1)]:
                    if item not in choices_list:
                        choices_list.append(item)
        if len(choices_list) != 0:
            for choices in choices_list:
                choices_string += str(count) + ' - ' + choices + '\n'
                count += 1
            user_input_2 = input(f'\nThe possible {attributes_string_list[index]}s from your search are:\n\n{choices_string}\n\nChoose a number and press enter to see the results!\n: ')
            while user_input_2.isdigit() == False:
                user_input_2 = input("Please choose a valid number and press enter.\n: ")
            if user_input_2.isdigit() == True:
                while int(user_input_2) < 1 or int(user_input_2) > count:
                    user_input_2 = input("Please choose a valid number and press enter.\n: ")
            for venue in self.venues:
                if venue[index].upper() == choices_list[int(user_input_2) - 1]:
                    print('\n' + '--- ' + venue[0] + ' ---' + '\n' + venue[4] + '\n')
        else:
            user_input_3 = input(f"\nThere are no results from your search. Would you like to search for another {attributes_string_list[index]}? ('y' or 'n')\n: ")
            if user_input_3 == 'y':
                self.choose_attribute_item(index)
        

## TESTS ##

venues_list = Venues(venues)


chosen_index = venues_list.choose_attribute_index()
venues_list.choose_attribute_item(chosen_index)