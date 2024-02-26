def days_passed(birthday):
    """

    :param birthday: The birthday in the format "DD-MM-YYY"
    :return: how many days have passed since your birthday (without counting the days in your birth year and the current year, so just whole years).
    """
    year = int(birthday[6:])
    modified = year + 1 #mosify so it does not count the days of the year you were born in
    return(2024- modified)

print(days_passed("11/04/2021"))