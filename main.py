# Словарь для хранения счетов пользователей
user_accounts = {}

# Список для хранения картинок
pictures = []

# Словарь для хранения настроек бота
bot_settings = {
    'message_frequency': 'daily',  # Возможные значения: 'daily', 'weekly', etc.
    'premium_bonus': 5  # Количество бонусов за победу в аукционе
}

# Функция для пополнения счета пользователя
def add_coins(user_id, coins):
    if user_id in user_accounts:
        user_accounts[user_id] += coins
    else:
        user_accounts[user_id] = coins

# Функция для траты монет
def spend_coins(user_id, coins):
    if user_id in user_accounts and user_accounts[user_id] >= coins:
        user_accounts[user_id] -= coins
        return True
    else:
        return False

# Функция для добавления картинок
def add_picture(picture_url):
    pictures.append(picture_url)

# Функция для отправки картинок
def send_picture(user_id, picture_index):
    if 0 <= picture_index < len(pictures):
        picture_url = pictures[picture_index]
        # Логика отправки картинки пользователю
        print(f"Sending picture to {user_id}: {picture_url}")
    else:
        print("Invalid picture index")

# Функция для изменения настроек
def set_bot_setting(setting, value):
    if setting in bot_settings:
        bot_settings[setting] = value
        print(f"Setting {setting} changed to {value}")
    else:
        print("Invalid setting")

# Пример использования всех функций
add_picture("http://example.com/pic1.jpg")
add_picture("http://example.com/pic2.jpg")
send_picture("user123", 0)  # Sending picture to user123: http://example.com/pic1.jpg

add_coins('user123', 10)
print(user_accounts)  # {'user123': 10}
spend_coins('user123', 5)
print(user_accounts)  # {'user123': 5}

set_bot_setting('message_frequency', 'weekly')
print(bot_settings)  # {'message_frequency': 'weekly', 'premium_bonus': 5}