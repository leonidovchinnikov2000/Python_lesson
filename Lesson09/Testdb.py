from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:123@localhost:5432/QA1"
db = create_engine(db_connection_string)


def test_add_user():
    """Тест на добавление пользователя без mappings()."""
    test_email = "testuser@example.com"
    test_subject_id = 1

    with db.connect() as connection:
        # Добавляем тестового пользователя
        connection.execute(
            text(
                "INSERT INTO users (user_email, subject_id) VALUES (:email, :subject_id)"
            ),
            {"email": test_email, "subject_id": test_subject_id},
        )
        connection.commit()

        # Проверяем, что пользователь добавился
        result = connection.execute(
            text("SELECT * FROM users WHERE user_email = :email"),
            {"email": test_email},
        )
        rows = result.all()  # без mappings()

        # Доступ по индексам (нужно знать порядок колонок в таблице)
        # Предположим: 0 - user_id, 1 - user_email, 2 - subject_id
        assert len(rows) == 1, "Пользователь не был добавлен"
        assert rows[0][1] == test_email, "Email не совпадает"
        assert rows[0][2] == test_subject_id, "subject_id не совпадает"

        # Очищаем тестовые данные
        connection.execute(
            text("DELETE FROM users WHERE user_email = :email"),
            {"email": test_email},
        )
        connection.commit()


def test_update_user():
    """Тест на редактирование пользователя без mappings()."""
    test_email = "nuwuser@example.com"
    new_email = "updateduser@example.com"
    test_subject_id = 3
    new_subject_id = 4

    with db.connect() as connection:
        # Создаем пользователя
        connection.execute(
            text(
                "INSERT INTO users (user_email, subject_id) VALUES (:email, :subject_id)"
            ),
            {"email": test_email, "subject_id": test_subject_id},
        )
        connection.commit()

        # Редактируем
        connection.execute(
            text(
                "UPDATE users SET user_email = :new_email, subject_id = :new_subject_id WHERE user_email = :test_email"
            ),
            {
                "new_email": new_email,
                "new_subject_id": new_subject_id,
                "test_email": test_email,
            },
        )
        connection.commit()

        # Проверяем обновление
        result = connection.execute(
            text("SELECT * FROM users WHERE user_email = :email"),
            {"email": new_email},
        )
        rows = result.all()

        assert len(rows) == 1, "Пользователь не найден после обновления"
        assert rows[0][1] == new_email, "Email не обновился"
        assert rows[0][2] == new_subject_id, "subject_id не обновился"

        # Старый email не должен существовать
        result = connection.execute(
            text("SELECT * FROM users WHERE user_email = :email"),
            {"email": test_email},
        )
        old_user = result.all()
        assert len(old_user) == 0, "Старый email все еще существует"

        # Очищаем
        connection.execute(
            text("DELETE FROM users WHERE user_email = :email"),
            {"email": new_email},
        )
        connection.commit()


def test_delete_user():
    """Тест на удаление пользователя без mappings()."""
    test_email = "deleteuser@example.com"
    test_subject_id = 1

    with db.connect() as connection:
        # Добавляем тестового пользователя
        connection.execute(
            text(
                "INSERT INTO users (user_email, subject_id) VALUES (:email, :subject_id)"
            ),
            {"email": test_email, "subject_id": test_subject_id},
        )
        connection.commit()

        # Проверяем, что пользователь добавился
        result = connection.execute(
            text("SELECT * FROM users WHERE user_email = :email"),
            {"email": test_email},
        )
        rows = result.all()  # без mappings()

        # Доступ по индексам (нужно знать порядок колонок в таблице)
        # Предположим: 0 - user_id, 1 - user_email, 2 - subject_id
        assert len(rows) == 1, "Пользователь не был добавлен"
        assert rows[0][1] == test_email, "Email не совпадает"
        assert rows[0][2] == test_subject_id, "subject_id не совпадает"

        # Очищаем тестовые данные
        connection.execute(
            text("DELETE FROM users WHERE user_email = :email"),
            {"email": test_email},
        )
        connection.commit()
