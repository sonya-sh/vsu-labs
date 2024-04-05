class HashTableWithoutCollisionHandling:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index] = None


# Создаем экземпляр таблицы без обработки коллизий
hash_table_no_collision = HashTableWithoutCollisionHandling(5)

# Вставляем элементы с ключами, которые дают одинаковый хеш-код (коллизия)
hash_table_no_collision.insert(5, "user5")
hash_table_no_collision.insert(10, "user10")
hash_table_no_collision.insert(15, "user15")

# Вывод содержимого таблицы
print("Table without Collision Handling:")
for i, value in enumerate(hash_table_no_collision.table):
    print(f"Bucket {i}: {value}")

# Попробуем найти элементы по разным ключам, дающим одинаковый хеш
result1 = hash_table_no_collision.search(5)
result2 = hash_table_no_collision.search(10)
result3 = hash_table_no_collision.search(15)

print("\n")
print(f"Key 5: {result1}")  # Выведет "Key 5: user10"
print(f"Key 10: {result2}")  # Выведет "Key 10: user10"
print(f"Key 15: {result3}")  # Выведет "Key 10: user10"
