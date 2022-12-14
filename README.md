<div align="center">
<img src="https://user-images.githubusercontent.com/81159301/193612153-e085ffb7-230b-413c-a7b2-c450536cd397.png" alt="Logo" width="200"><br><br>

# SUTE Schedule Bot

[![Python 3.6+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## [English version](README.md)
Бот для зручного перегляду розкладу пар в [ДТЕУ](https://mia1.knute.edu.ua).<br>
*\*Ви також можете налаштувати цього бота для відображення розкладу інших університетів, що використовують систему АСУ МКР\**<br>
Бот доступний для використання по [посиланню](https://t.me/dteubot)<br>

</div>

# Скріншоти
![Скріншот бота](https://user-images.githubusercontent.com/81159301/193561985-2414eafb-3423-4ef6-b149-24926831df7a.png)

# Команди

* **/today**<br>
    пари сегодні
* **/tomorrow**<br>
    пари завтра
* **/left**<br>
    час до кінця/початку пари
* **/calls**<br>
    розклад дзвінків
* **/menu**<br>
    відкрити меню
* **/settings**<br>
    відкрити налаштування
* **/select \<groupId?: `number`\>**<br>
    вибрати групу
* **/lang \<lang?: `[en/uk/ru]`\>**<br>
    вибрати мову

? - необов'язковий параметр
<br><br>

# Запуск

Бота можна запустити двома способами: через Docker та напряму

## 1. Звичайний спосіб

> :warning: Для цього способу вам потрібен **Python** версії **3.7+**

1. Завантажте цей репозиторій та відкрийте в ньому командний рядок.<br>
   Для завантаження, нажміть зелену кнопку **<span style="color: lightgreen;"><> Code</span> > Download ZIP**<br>
   або виконайте команду
   ```shell
   git clone https://github.com/angron42/sute-schedule-bot
   ```
2. Установіть бібліотеки:
   ```shell
   pip install -r requirements.txt
   ```
3. Налаштуйте файл `.env` по прикладу `.env.example`
4. Запустіть бота наступною командою
   ```shell
   python .
   ```

Цей бот також підтримує роботу в іншій директорії: потрібно створити в ній файл .env та виконати команду `python "/шлях/до/папки/з/ботом"`<br>
Якщо ж файл не створити, програма буде шукати його в своїй кореневій директорії.

## 2. Docker

1. Установіть Docker
2. Створіть директорію, в якій будуть зберігатися дані бота
3. В цій директорії створіть файл `.env` та заповніть його за прикладом файла [.env.example](.env.example)
4. Виконайте наступну команду:
    - Для Windows:
        ```shell
        docker run -d -v ${PWD}:/data --name schedule-bot angron42/sute-schedule-bot
        ```
    - Для Linux:
        ```shell
        docker run -d -v $(pwd):/data --name schedule-bot angron42/sute-schedule-bot
        ```

Щоб зупинити, виконайте команду
```shell
docker stop schedule-bot
```

