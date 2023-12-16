import csv
import random


def generate_data(rows):
    data = []
    for i in range(rows):
        data.append({
            'id': i+1,
            'name': generate_name(),
            'age': generate_age(),
            'city': generate_city(),
        })
    return data


def generate_name():
    names = ['Sofia', 'Anastasia', 'Victoria', 'Ksenia', 'Arina', 'Elizaveta', 'Adelina', 'Irina', 'Elena', 'Polina']
    return random.choice(names)


def generate_age():
    return random.randint(18, 60)


def generate_city():
    cities = ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Nizhny Novogorod', 'Kazan', 'Chelyabinsk', 'Omsk', 'Samara', 'Rostov-on-Don']
    return random.choice(cities)


def write_to_csv(data, file_path):
    fieldnames = ['id', 'name', 'age', 'city']

    with open(file_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    num_rows = 100
    csv_file_path = './data/people_data.csv'

    generated_data = generate_data(num_rows)

    write_to_csv(generated_data, csv_file_path)

    print(f"CSV file '{csv_file_path}' generated successfully with {num_rows} rows.")
