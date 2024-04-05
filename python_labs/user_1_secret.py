import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

try:
    # Загрузка закрытого ключа USER_1
    with open('/home/sonya/ЭЦП_пример/USER_1/private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )

    file_to_sign = '/home/sonya/ЭЦП_пример/USER_1/IMPORTANT_DOC.txt'

    # Чтение содержимого файла и хеширование его данных
    with open(file_to_sign, 'rb') as file:
        data_to_sign = file.read()
        hash_value = hashes.Hash(hashes.SHA256())
        hash_value.update(data_to_sign)
        digest = hash_value.finalize()

    # Создание подписи
    signature = private_key.sign(
        digest,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    file_for_signature = '/home/sonya/ЭЦП_пример/USER_1/signature.txt'
    # Сохранение подписи в файл signature.txt
    with open(file_for_signature, 'wb') as signature_file:
        signature_file.write(signature)

    print(f"Подпись успешно создана и сохранена в файл {file_for_signature}")
except Exception as e:
    print(f"Произошла ошибка при создании подписи: {e}")
