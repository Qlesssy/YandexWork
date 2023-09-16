# Олеся Лапшина, 8-я когорта — Финальный проект. Инженер по тестированию плюс

from data import order_body
from sender_stand_request import create_order, get_information_order

def test_order_creation_and_get_information():
    response_create = create_order(order_body)
    assert response_create.status_code == 201, "Получили ожидаемый ответ 201"

    track_number = response_create.json().get("track")
    assert track_number, "Трек номер не найден в запросе"

    response_retrieve = get_information_order(track_number)
    assert response_retrieve.status_code == 200, "Получили ожидаемый ответ 200"