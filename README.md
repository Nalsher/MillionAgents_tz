task1.py - Созданы все классы экранирования(emailshielding, numbershielding, skypeshielding)

/task2 - Сервис по укорачиванию ссылок. Для запуска сервиса необходимо зайти в директорию task2 и прописать комманду в консоль
## uvicorn app:app --reload
Для создания ссылки нужно отправить POST запрос и в body отправить ссылку.
В ответ сервер пришлёт ответ с укороченной ссылкой, по ней можно перейти и вас перенаправит на изначальную ссылку.Ссылки сохраняются в storage.txt файл.
Защита от перебора реализована небольшим таймаутом.

2.1 task - SQL запрос на задание 2.1

2.2 task - SQL запрос на задание 2.2
