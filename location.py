class Location:
    locations = []

    def __init__(self, province, county, commune, commune_type, name, typ):
        self.province = province
        self.county = county
        self.commune = commune
        self.commune_type = commune_type
        self.name = name
        self.typ = typ

    @staticmethod
    def get_province():
        """Returns province as string"""
        return Location.locations[0].name

    @staticmethod
    def add_location(data):
        """
        Adds data to list.
        Args: data (list of lists)
        """
        for item in data:
            location = Location(item[0], item[1], item[2], item[3], item[4], item[5])
            Location.locations.append(location)

    @staticmethod
    def read_from_csv(file):
        """
        Reads from csv and appends to list.
        Args: file (csv file)
        Returns: list of list
        """
        import csv
        with open(file) as f:
            next(f)
            data = []
            for line in csv.reader(f, delimiter='\t'):
                data.append(list(line))
        return data

    @staticmethod
    def list_statistics():
        """
        Lists statistics.
        Returns: stats_listed (list of lists)
        """
        statistics = {}
        stats_listed = []
        for item in Location.locations:
            if item.typ not in statistics:
                statistics[item.typ] = 1
            else:
                statistics[item.typ] += 1
            if item.typ == "miasto na prawach powiatu":
                statistics["powiat"] += 1
        for key, value in statistics.items():
            stats_listed.append([str(value), key])
        return stats_listed

    @staticmethod
    def display_three_cities_with_longest_names():
        """
        Displays three cities with longest names.
        Returns: three_cities (list of lists)
        """
        cities = []
        three_cities = []
        for item in Location.locations:
            if item.commune_type == "4":
                cities.append(item.name)
        cities = sorted(cities, key=lambda x: len(x), reverse=True)
        three_cities.append([cities[0]])
        three_cities.append([cities[1]])
        three_cities.append([cities[2]])
        return three_cities

    @staticmethod
    def display_county_name_with_most_communes():
        """
        Displays county name with the largest amount of communes.
        Returns: the_county (list of lists)
        """
        counties = []
        for item in Location.locations:
            if item.commune == "" and not item.county == "":
                counties.append(item)
        amount = [-1] * len(counties)
        n = 0
        for county in counties:
            for item in Location.locations:
                if item.county == county.county and (item.commune_type == "1" or item.commune_type == "2"
                                                     or item.commune_type == "3" or item.commune_type == "4"
                                                     or item.commune_type == "5"):
                    amount[n] += 1
            n += 1
        county_and_commune_amount = []
        x = 0
        for item in counties:
            county_and_commune_amount.append([item.name, amount[x]])
            x += 1
        county_and_commune_amount = sorted(county_and_commune_amount, key=lambda i: i[1], reverse=True)
        county_and_commune_amount[0] = county_and_commune_amount[0][0], str(county_and_commune_amount[0][1])
        the_county = [county_and_commune_amount[0]]
        return the_county

    @staticmethod
    def display_locations_within_more_than_one_category():
        """
        Displays locations within more than one category.
        Returns: to_display_in_table (list of lists)
        """
        name_and_commune = []
        for item in Location.locations:
            name_and_commune.append([item.name, item.commune])
        every = []
        repeating = []
        for item in name_and_commune:
            if item in every:
                repeating.append(item)
            else:
                every.append(item)
        one_from_repeating = []
        for data in repeating:
            if data not in one_from_repeating:
                one_from_repeating.append(data)
        to_display_in_table = []
        n = 1
        for stuff in one_from_repeating:
            to_display_in_table.append([str(n), stuff[0]])
            n += 1
        return to_display_in_table

    @staticmethod
    def advanced_search():
        """
        Allows to search for location.
        Returns: search_effect (list of lists)
        """
        search_effect = []
        search = input("Name location: ")
        search = search.lower()
        for item in Location.locations:
            if search in item.name:
                search_effect.append([item.name, item.typ])
            elif search.title() in item.name:
                search_effect.append([item.name, item.typ])
        search_effect = sorted(search_effect, key=lambda x: (x[0].lower(), x[1]))
        return search_effect


