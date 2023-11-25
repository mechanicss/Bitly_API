# Bitly_API
 
## Урок 2. Посчитайте клики по ссылкам
Проект сокращяет ссылки с помощю сервиса Bitly, а также
отображает количество переходов  сделаных по сокращенной ссылке.


## Зависимости
```
python-dotenv==1.0.0
requests==2.31.0
```


## Переменные окружения
Создаем файл .env и помещяем в него переменную с API токеном.
```
echo BITLY_TOKEN=fa387498802363as08c511970ab9e4df797d0afd > .env
```
### Как получить
Получить токен можно после регистрации на сайте сервиса 
```
https://bitly.com/pages/why-bitly/integrations-api
```

## Запуск
Клонируем репозиторий к себе на компьютер и переходим в папку проекта.
```
git clone https://github.com/mechanicss/Bitly_API.git
cd Bitly_API
```
Создаем виртуальное окружение.
```
python3 -m venv venv
```
Активируем его.
```
source venv/bin/activate
```
Устанавливаем зависимости проекта.
```
pip install -r requirements.txt
```
Запуск приложения.
```
python3 check_for_short_link.py
```
Если все сделано правельно - вы должны увидеть предложение ввести ссылку.


## Примечания
Ссылка для сокращения указываеться в полном формате. Пример - `https://ya.ru`

Ссылка Bitlink указываеться в сокращенном формате . Пример - `bit.ly/40myIrB`
