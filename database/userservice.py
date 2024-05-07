from database import get_db
from database.models import User

from datetime import datetime

def register_user_db(name, surname, email, phone_number, country, password, reg_date):
    try:
        db = next(get_db())

        new_user = User(name=name, surname=surname, email=email, phone_number=phone_number, country=country,
                        password=password, reg_date=datetime.now())
        db.add(new_user)
        db.commit()

        return {'status': 1, 'message': 'Регистрация прошла успешно'}
    except:
        return {'status': 0, 'message': 'Ошибка!'}

def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return {'status': 1, 'message': 'Такого юзера нету'}

def get_all_user_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return {'status': 1, 'message': all_users}

def check_phone_number(phone_number):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return {'status': 1, 'message': checker}
    else:
        return {'status': 0, 'message': 'Ошибка!'}

def edit_user_db(user_id, changeable_info, new_info):
    db = next(get_db())

    user = db.query(User).filter_by(id=user_id).first()

    if user:
        try:
            if changeable_info == 'name':
                user.name = new_info
                return 'Имя успешно обновлена'
            elif changeable_info == 'surname':
                user.birthday = new_info
                return 'День рождения успешно обновлена'
            elif changeable_info == 'phone_number':
                user.phone_number = new_info
                return 'Номер успешно обновлен'
            elif changeable_info == 'email':
                user.email = new_info
                return 'Почта успешно обновлена'
            elif changeable_info == 'password':
                user.password = new_info
                return 'Пароль успешно обновлена'
            elif changeable_info == 'country':
                user.user_city = new_info
                return 'Место прооживания успешно обновлена'
            db.commit()
            return {'status': 1, 'message': 'Инфо успешно обновлен'}
        except:
            return {'status': 0, 'message': 'Ошибка при обновлении'}
    return {'status': 0, 'message': 'Юзер не найден'}

def delete_user_db(user_id):
    db = next(get_db())

    user = db.query(User).filter_by(id=user_id).first()

    if user:
        db.delete(user)
        db.commit()
        return {'status': 1, 'message': 'Юзер успешно удален'}
    else:
        return {'status': 0, 'message': 'Ошибка'}


