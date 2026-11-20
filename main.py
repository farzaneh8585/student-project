from grades import calculate_avg, find_max, find_min
from status import get_status

def main():
    name = input("Enter student name: ")
    
    grades_input = input("Enter grades (separated by space): ")
    
    grades_list = []
    for g in grades_input.split():
        grades_list.append(float(g))
        
    avg = calculate_avg(grades_list)
    max_grade = find_max(grades_list)
    min_grade = find_min(grades_list)
    status = get_status(avg)
    
    print("\nstudent:", name)
    print("Avg =", avg)
    print("max =", max_grade)
    print("min =", min_grade)
    print("status =", status)

main()
