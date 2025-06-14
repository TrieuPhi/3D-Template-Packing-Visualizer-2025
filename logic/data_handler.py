import csv

def read_data_from_file(filepath):
    # Đọc dữ liệu từ file txt/csv
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                data.append(tuple(map(int, row)))
    return data

def save_data_to_file(filepath, data):
    # Lưu dữ liệu ra file txt/csv
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
