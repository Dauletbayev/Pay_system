from database.models import UserCard
from datetime import datetime
from database import get_db


# Добавления карты
def add_card_db(user_id, card_number, card_name, balance, exp_date, card_id):
    db = next(get_db())
    new_card = UserCard(user_id=user_id, card_id=card_id, card_number=card_number, card_name=card_name,
                        balance=balance, exp_date=exp_date)
    if new_card:
        db.add(new_card)
        db.commit()
        return {'status': 1, 'message': 'Карта успешно добавлена'}
    else:
        return {'status': 0, 'message': 'Ошибка при добавлении карты'}


# Вывести все карты определенного пользователя
def get_exact_user_card_db(user_id):
    db = next(get_db())
    exact_user_card = db.query(UserCard).filter_by(user_id=user_id).first()
    if exact_user_card:
        return {'status': 1, 'message': exact_user_card}
    else:
        return {'status': 0, 'message': 'Ошибка'}


# Вывести определенную карту определенного пользователя
def get_exact_card_user_db(user_id, card_id):
    db = next(get_db())
    exact = db.query(UserCard).filter_by(user_id=user_id, card_id=card_id).first()
    if exact:
        return {'status': 1, 'message': exact}
    else:
        return {'status': 0, 'message': 'Ошибка'}


# Проверка карты на наличие в БД
def check_card_db(card_number):
    db = next(get_db())
    checker = db.query(UserCard).filter_by(card_number=card_number).first()
    if checker:
        return {'status': 1, 'message': checker}
    else:
        return {'status': 0, 'message': 'Ошибка'}


# Удаления карты
def delete_card_db(card_id):
    db = next(get_db())
    delete_card = db.query(UserCard).filter_by(card_id=card_id).first()
    if delete_card:
        db.delete(delete_card)
        db.commit()
        return {'status': 1, 'message': 'Карта успешно добавлена'}
    else:
        return {'status': 0, 'message': 'Ошибка при удалении'}
        
# Измение информаций на карте
def edit_card_info(user_id, change_info, new_info):
    db = next(get_db())

    card = db.query(UserCard).filter_by(user_id=user_id).first()
    if card:
        try:
            if card == 'card_name':
                card.card_name = new_info
                db.commit()
                return {'status': 1, 'message': 'Инфо успешно обновлена'}
            else:
                return {'status': 0, 'message': 'Не понял!'}
        except:
            return {'status': 0, 'message': 'Ошибка!'}
    else:
        return {'status': 0, 'message': 'Не найден!'}




