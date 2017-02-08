
def printing(content):
    """Prints output"""
    print(content)


def get_input(inputs):
    """Takes input from user."""
    return input(inputs)


def display_menu():
    """Prints menu"""
    print("""\nWhat would you like to do?:
                      (1) List statistics
                      (2) Display 3 cities with longest names
                      (3) Display county's name with the largest number of communities
                      (4) Display locations, that belong to more than one category
                      (5) Advanced search
                      (0) Exit program""")


def print_table(table, title_list):
    """Displays data in a formatted table"""
    table.insert(0, title_list)
    for row_index, row in enumerate(table):
        for col_index, col in enumerate(row):
            if (type(col) == float) or (type(col) == int):
                table[row_index][col_index] = str("{0:,.2f}".format(col))
    widths = [max(map(len, col)) for col in zip(*table)]
    sum_of_widths = sum(widths) + len(table[0]) * 3 - 1
    for row in table:
        print("-" * sum_of_widths)
        print("|" + "  ".join((val.ljust(width) + "|" for val, width in zip(row, widths))))
    print("-" * sum_of_widths)
