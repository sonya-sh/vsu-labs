import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

try:
    # Загрузка открытого ключа, полученного от USER_1, сгенерированного им же
    with open('/home/sonya/ЭЦП_пример/USER_2/public_key.pem', 'rb') as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )

    file_to_sign = '/home/sonya/ЭЦП_пример/USER_2/IMPORTANT_DOC.txt'

    # Чтение содержимого файла и хеширование его данных
    with open(file_to_sign, 'rb') as file:
        data_to_sign = file.read()
        hash_value = hashes.Hash(hashes.SHA256())
        hash_value.update(data_to_sign)
        digest = hash_value.finalize()

    # Загрузка подписи
    with open('/home/sonya/ЭЦП_пример/USER_2/signature.txt', 'rb') as signature_file:
        signature = signature_file.read()

    # Попытка проверки подписи
    try:
        public_key.verify(
            signature,
            digest,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("Подпись верна. Документ подлинный.")
    except cryptography.exceptions.InvalidSignature:
        print("Подпись не верна. Документ может быть изменен или поддельный.")

except Exception as e:
    print(f"Произошла ошибка при проверке подписи: {e}")
