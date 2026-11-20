def calculate_avg(grades):
    if len(grades) == 0:
        return 0
    total = sum(grades)
    return total / len(grades)

def find_max(grades):
    if len(grades) == 0:
        return 0
    return max(grades)

def find_min(grades):
    if len(grades) == 0:
        return 0
    return min(grades)
