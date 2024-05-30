# Запуск приложения
1. Клонируем репозиторий - git clone https://github.com/MadiKamyrov/electronic_gradebook.git
2. Скачать и установить Python - https://www.python.org/downloads/
3. Обновить pip командой pip3 install -- upgrade pip
4. В директории с исходниками создать виртуальную среду разработки командой - python3 -m venv venv
5. Активировать виртуальную среду - source venv/bin/activate
6. Установить зависимости командой - pip install -r requirements.txt
7. Запуск приложения - uvicorn main:app --reload

# API EndPoints
- `POST /students/`: Создать нового студента.
- `GET /students/{student_id}`: Получить информацию о студенте с указанным ID.
- `PATCH /students/{student_id}`: Обновить информацию о студенте с указанным ID.
- `DELETE /students/{student_id}`: Удалить студента с указанным ID.
- `POST /scores/`: Добавить оценку студенту.
- `GET /scores/{score_id}`: Получить информацию об оценке с указанным ID.
- `PATCH /scores/{score_id}`: Обновить информацию об оценке с указанным ID.
- `DELETE /scores/{score_id}`: Удалить оценку с указанным ID.
