# Проект CatBot

CatBot - это бот для Telegram, который присылает пользователю мемы с котами.

## Установка

1. Клонируйте репозиторий с github

2. Создайте и активируйте виртуальное окружение

```
python -m venv venv_name

Win: venv_name/Scripts/activate
```

3. Установите зависимости 

```
pip intall -r requirements.txt
```

4. Создайте файл 
`settings.py`

5. Впишите в settings.py переменные:

```
API_KEY = "Ваш API-ключ"

USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']
```

6. Запустите бота командой командой в директории проекта

```
python bot.py 
```