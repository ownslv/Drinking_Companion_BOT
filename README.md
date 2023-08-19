
<h1 align="center">Hi there, I'm <a href="https://daniilshat.ru/" target="_blank">drinking companion</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>







Клонируем проект: 
```
git clone 
```
Создайте и активируйте виртуальное окружение
```
python3 -m venv venv
source venv/bin/activate
```
Установите все зависимости
```
pip3 install --upgrade pip
python3 -m pip install -r requirements.txt
```

В домашней директории проекта создать файл .env:

  ```
  sudo touch .env
  ```


Заполните .env. Для примера используйте .env.example
   ```
sudo nano .env
TOKEN=your_token_bot
   ```
Вам потребуется узнать user id нашего алкаша.
Узнать можно в телеграмме с помощью бота
   ```
@userinfobot
   ```
Подставьте полученое значение user id добавьте в .env
   ```
sudo nano .env
DRUNKARD=user_id
   ```
Создайте файл list.py в домашней директории проекта. В этом файле накидайте N-кол-во фраз для бота в формате списка
   ```
tlist = [#Здесь список ваших фраз]
   ```


# Проверка работоспособности
После того, как все готово, перейдите в домашнюю директорию проекта и запустите zxc.py

  ```
python3 zxc.py
  ```
Добавьте бота в беседу, где сидит одинокий алкаш и наслаждайтесь
