# simple-bot-for-yc-function
Cloud Functions
Перейдите в раздел Cloud Functions

Создайте новую функцию c названием, например, python-tg-bot.

Укажите язык python и выберите самую последнюю версию.

В настройках функции загрузите код бота. В переменные окружения добавьте поле TOKEN и вставьте токен. После обязательно нажмите Создать версию, чтобы запустить функцию.

Запомним идентификатор функции (первая строка)

API-Gateway
Чтобы мы смогли получить доступ к нашей функции, нужно настроить API-Gateway.

Перейдите в раздел API-Gateway

Создайте новый шлюз и настройте его. Скопируйте конфигурацию и замените YOUR_FUNCTION_ID на идентификатор функции, полученный ранее.

openapi: 3.0.0
info:
 title: for-python-tg-bot
 version: 1.0.0
paths:
 /:
   post:
     x-yc-apigateway-integration:
       type: cloud-functions
       function_id: YOUR_FUNCTION_ID
     operationId: tg-webhook-function

Запомним ссылку, по которой можно вызвать нашу функцию

Регестрируем вэбхук:

https://api.telegram.org/botTOKEN/setWebhook?url=URL_API_GATEWAY
