def heading(char, number_of_signs=1):
    return f"{'#' * min(6, max(number_of_signs, 1))} {char}"
