transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


def filter_by_currency(transactions: list, currency: str) -> dir:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    if len(transactions) > 1:
        for operation_in_transaction in transactions:
            if operation_in_transaction.get("operationAmount").get("currency").get("name") == currency:
                yield operation_in_transaction
        yield "Нет значений"


usd_transactions = filter_by_currency(transactions, "USD")
for i in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list) -> str:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    # Проверяем, если список пустой
    if not transactions:
        yield "Нет значений"

    for transaction in transactions:
        description = transaction.get("description")
        # Если описание отсутствует, можем возвращать некоторое сообщение или просто пропустить
        if description:
            yield description
        else:
            yield "Описание отсутствует"


descriptions = transaction_descriptions(transactions)
for i in range(2):
    print(next(descriptions))


def card_number_generator(start: int, stop: int):
    """Генератор, который выдает номера банковских карт в формате: XXXX XXXX XXXX XXXX"""
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
            8:12
        ] + " " + f"{number:016d}"[12:]


for card_number in card_number_generator(1, 5):
    print(card_number)
