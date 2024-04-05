import hashlib
import time
import zlib


def calculate_file_hash(file_path):
    # Открываем файл в бинарном режиме
    with open(file_path, 'rb') as file:
        # Читаем файл блоками и вычисляем хеш-значение CRC32
        crc32_hash = 0
        while True:
            data = file.read(4096)  # Читаем 4 КБ данных за раз
            if not data:
                break
            crc32_hash = zlib.crc32(data, crc32_hash)

    # Возвращаем хеш-значение CRC32
    return crc32_hash


def main():
    file_path = "/home/sonya/hash_file/hashfile.txt"

    # Вычисляем хеш-значение файла
    original_hash = calculate_file_hash(file_path)
    print("Хеш-значение файла:", original_hash)

    while True:
        time.sleep(3)
        recalculated_hash = calculate_file_hash(file_path)
        # print("Хеш-значение файла:", recalculated_hash)
        if recalculated_hash == original_hash:
            print("Целостность файла подтверждена.")
        else:
            print("Файл был изменен или поврежден.")
            return


if __name__ == "__main__":
    main()
