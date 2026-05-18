import pymysql
from pymysql.cursors import DictCursor


# config = {
#     'host': 'ich-db.edu.itcareerhub.de',
#     'user': 'ich1',
#     'password': 'password',
#     'cursorclass': DictCursor,
# }
#
# connection = pymysql.connect(**config)
# with connection.cursor() as cursor:
#     cursor.execute("SHOW DATABASES")
#     for db in cursor:
#         print(db)
#
#     print('-' * 50)
#     cursor.execute("USE hr")
#     cursor.execute("SHOW TABLES")
#     for table in cursor:
#         print(table)
#
#     print('-' * 50)
#     cursor.execute("SELECT * FROM departments")
#     for department in cursor:
#         print(department)




config = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
    'cursorclass': DictCursor,
}
connection = pymysql.connect(**config)

# with connection.cursor() as cursor:
#     cursor.execute("CREATE DATABASE IF NOT EXISTS market")
#     cursor.execute("USE market")
#
#     cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS customers (
#                     id INT AUTO_INCREMENT PRIMARY KEY,
#                     name VARCHAR(100),
#                     balance DECIMAL(10, 2) NOT NULL CHECK (balance >= 0)
#                 )
#                 """)
#
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS products (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(100),
#             price DECIMAL(10, 2),
#             stock INT NOT NULL CHECK (stock >= 0)
#         )
#     """)
#
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS purchases (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             customer_id INT,
#             product_id INT,
#             purchase_date DATE,
#             FOREIGN KEY (customer_id) REFERENCES customers(id),
#             FOREIGN KEY (product_id) REFERENCES products(id)
#             )
#     """)
#
#     cursor.execute("DELETE FROM purchases")
#     cursor.execute("DELETE FROM customers")
#     cursor.execute("DELETE FROM products")
#     cursor.executemany(
#     "INSERT INTO customers (name, balance) VALUES (%s, %s)",
#     [("Alice", 20.00), ("Bob", 200.00)]
#     )
#     cursor.executemany(
#     "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
#     [("Headphones", 99.99, 3), ("Mouse", 25.00, 5)]
#     )
#     connection.commit()


with connection.cursor() as cursor:
    cursor.execute("USE market")
    cursor.execute("SELECT * FROM customers")
    for row in cursor.fetchall():
        print(row)

    try:
        # Получаем товар
        cursor.execute("SELECT id, price, stock FROM products WHERE name = %s",
                       ("Headphones",)
                       )
        product = cursor.fetchone()
        product_id, price, stock = product["id"], product["price"], product["stock"]
        # Если товар в наличии списываем его
        if product['stock'] < 1:
            raise ValueError("Out of stock")

        cursor.execute("UPDATE products SET stock = stock - 1 WHERE id = %s", (product_id,))

        # Получаем клиента
        cursor.execute("SELECT id, balance FROM customers WHERE name = %s", ("Alice",))
        customer_id, balance = cursor.fetchone().values()

        # Если баланса хватает списываем оплату
        if balance < price:
            raise ValueError("Insufficient funds")

        cursor.execute("UPDATE customers SET balance = balance - %s WHERE id = %s", (price, customer_id))
        # Фиксируем покупку в таблице purchases
        cursor.execute("""INSERT INTO purchases (customer_id, product_id, purchase_date)
                          VALUES (%s, %s, CURDATE())""",
                       (customer_id, product_id))

        connection.commit()  # При отсутствии ошибок завершаем транзакцию
        print("Purchase successful.")
    except Exception as e:
        connection.rollback()












