def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
        return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

cats_info = get_cats_info("HW02/cats_file.txt")
print(cats_info)
