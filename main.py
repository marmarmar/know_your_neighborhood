from ui import *
from location import *
import sys


def main():
    while True:
        try:
            file = get_input("Enter the name of the file to get data from: ")
            Location.add_location(Location.read_from_csv(file))
            printing("\n\tBrowse Through Locations Program\n")
            while True:
                display_menu()
                number = get_input("Choose number: ")
                if number == "1":
                    print_table(Location.list_statistics(), ["", Location.get_province()])
                elif number == "2":
                    print_table(Location.display_three_cities_with_longest_names(), ["3 CITIES WITH LONGEST NAMES "])
                elif number == "3":
                    print_table(Location.display_county_name_with_most_communes(), ["COUNTY NAME", "NUMBER OF COMMUNES "])
                elif number == "4":
                    print_table(Location.display_locations_within_more_than_one_category(), ["Num", "LOCATIONS IN MORE "
                                                                                                    "THAN ONE CATEGORY "])
                elif number == "5":
                    print_table(Location.advanced_search(), ["LOCATION", "TYPE "])
                elif number == "0":
                    printing("Thank you for using our program. See you back soon.")
                    sys.exit()
                else:
                    printing("Please choose a number from menu.")
        except FileNotFoundError:
            printing("\nThis file wasn't found. Please try again.\n")

if __name__ == "__main__":
    main()