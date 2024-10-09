import json

class Customer:
    def __init__(self, name, customer_id, initial_balance):
        self.name = name
        self.customer_id = customer_id
        self.balance = initial_balance
        self.transaction_history = []

    def add_transaction(self, transaction_details):
        self.transaction_history.append(transaction_details)
        self.save_transaction_to_file(transaction_details)

    def save_transaction_to_file(self, transaction_details):
        with open("transaction_history.txt", "a") as file:
            file.write(f"{self.customer_id}: {transaction_details}\n")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"ID: {self.customer_id}, Name: {self.name}, Balance: {self.balance}"


# Словник для зберігання клієнтів
customers = {}

def create_account(name, customer_id, initial_balance):
    if customer_id in customers:
        print("Account already exists.")
        return

    customer = Customer(name, customer_id, initial_balance)
    customers[customer_id] = customer
    customer.add_transaction(f"Рахунок створено з початковим балансом: {initial_balance}")
    print("Обліковий запис успішно створено!")

def deposit(customer_id, amount):
    if customer_id not in customers:
        print("Клієнта не знайдено.")
        return

    if amount <= 0:
        print("Сума депозиту має бути позитивною")
        return

    customer = customers[customer_id]
    customer.balance += amount
    customer.add_transaction(f"Депоновано: {amount}")
    print(f"Депонований {amount}. Новий баланс: {customer.get_balance()}")

def withdraw(customer_id, amount):
    if customer_id not in customers:
        print("Клієнта не знайдено.")
        return

    customer = customers[customer_id]
    if amount > customer.balance:
        print("Недостатньо коштів.")
        return

    customer.balance -= amount
    customer.add_transaction(f"Знято: {amount}")
    print(f"Знято {amount}. Новий баланс: {customer.get_balance()}")

def transfer(from_id, to_id, amount):
    if from_id not in customers:
        print("Відправника не знайдено.")
        return

    if to_id not in customers:
        print("Одержувача не знайдено.")
        return

    sender = customers[from_id]
    if amount > sender.balance:
        print("Недостатньо коштів.")
        return

    sender.balance -= amount
    recipient = customers[to_id]
    recipient.balance += amount

    sender.add_transaction(f"Перенесено {amount} до {to_id}")
    recipient.add_transaction(f"Отримано {amount} від {from_id}")

    print(f"Перенесено {amount} від {from_id} до {to_id}.")

def view_balance(customer_id):
    if customer_id not in customers:
        print("Клієнта не знайдено.")
        return

    customer = customers[customer_id]
    print(f"Поточний баланс для {customer.name} ({customer_id}): {customer.get_balance()}")

def view_transaction_history(customer_id):
    if customer_id not in customers:
        print("Клієнта не знайдено.")
        return

    customer = customers[customer_id]
    print(f"Історія транзакцій для {customer.name} ({customer_id}):")
    for transaction in customer.transaction_history:
        print(transaction)

def list_customers():
    print("Список клієнтів:")
    for customer in customers.values():
        print(customer)

# Основне меню для взаємодії з користувачем
def main():
    while True:
        print("\n1. Створити акаунт")
        print("2. депозит")
        print("3. Вилучити")
        print("4. Трансфер")
        print("5. Переглянути баланс")
        print("6. Перегляд історії транзакцій")
        print("7. Список клієнтів")
        print("8. Вихід")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Виберіть дію:")
            customer_id = input("Введіть ID: ")
            initial_balance = float(input("Введіть початковий баланс: "))
            create_account(name, customer_id, initial_balance)
        elif choice == '2':
            customer_id = input("Введіть ідентифікатор клієнта: ")
            amount = float(input("Введіть суму депозиту: "))
            deposit(customer_id, amount)
        elif choice == '3':
            customer_id = input("Введіть ідентифікатор клієнта: ")
            amount = float(input("Введіть суму для зняття: "))
            withdraw(customer_id, amount)
        elif choice == '4':
            from_id = input("Введіть ідентифікатор клієнта: ")
            to_id = input("Введіть ідентифікатор одержувача: ")
            amount = float(input("Введіть суму для переказу: "))
            transfer(from_id, to_id, amount)
        elif choice == '5':
            customer_id = input("Введіть ідентифікатор клієнта: ")
            view_balance(customer_id)
        elif choice == '6':
            customer_id = input("Введіть ідентифікатор клієнта: ")
            view_transaction_history(customer_id)
        elif choice == '7':
            list_customers()
        elif choice == '8':
            print("Вихід...")
            break
        else:
            print("Недійсний варіант. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
