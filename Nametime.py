def nameMonth(month) -> str:
    if month == 1 or month == '01':
        return "jan"
    elif month == 2 or month == '02':
        return "feb"
    elif month == 3 or month == '03':
        return "mar"
    elif month == 4 or month == '04':
        return "apr"
    elif month == 5 or month == '05':
        return "may"
    elif month == 6 or month == '06':
        return "jun"
    elif month == 7 or month == '07':
        return "jul"
    elif month == 8 or month == '08':
        return "aug"
    elif month == 9 or month == '09':
        return "sep"
    elif month == 10 or month == '10':
        return "oct"
    elif month == 11 or month == '11':
        return "nov"
    elif month == 12 or month == '12':
        return "dec"
    else:
        return "invalid input"
