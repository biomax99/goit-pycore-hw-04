def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = [int(line.split(',')[1]) for line in file]
        total = sum(salaries)
        average = total / len(salaries) if salaries else 0
        return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

total, average = total_salary("HW01/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
