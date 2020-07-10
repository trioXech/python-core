def is_leap(year):
    """
    This function checks a year is Leap or not

    :param year: type integer
    :return: True or False
    """

    leap = False

    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                leap = True
        else:
            leap = True

    return leap

year = int(input())
print(is_leap(year))
