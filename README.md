# book_catalog

> Примечании
>
> 1. Я не стал завёртывать всё в docker и прятать .env и db.sqlite3 чтобы были начальные данные для теста
> 2. В модельки Book есть поле seo_title с помошью которого можно перейти в метод retreive Книги.
>    Пример: [http://127.0.0.1:8000/books/a-little-life](http://127.0.0.1:8000/books/a-little-life) или как обычно по его id
> 3. swagger:  [http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger)
> 4. Не стал заморачиваться с задачей Регистрация/авторизация через через email (Прошу простить)
> 5. Весь контент добавляется через admin page и либо можете сами создать нового супер юзера либо использовать моего
>    username: admin
>    password: zxczxc123
> 6. Проследил чтобы нельзя было отправлять review или добавлять в favorite кроме как своего авторизованного пользователя
> 7. Авторизация находится по url адрессу [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/)
>    Пример: Authorization: Bearer `<ваш token>`
> 8. Тестировал манульно через DRF GUI, swagger , postman но не все методы
> 9. Если что-то пошло не так или что-то не понравилось как я сделал, то жду развёрнутый ответ от вас, заранее спасибо!

## Инструкция по запуску проекта

Следующие инструкции позволят вам запустить проект "Каталог книг" на вашей локальной машине для проверки тестогого задания.

### 1. Подготовка окружения

1. Убедитесь, что на вашей машине установлен Python 3.6 или выше. Если нет, [скачайте и установите Python](https://www.python.org/downloads/).
2. Убедитесь, что у вас установлен `pip`, менеджер пакетов Python. Если нет, [инструкции по установке pip](https://pip.pypa.io/en/stable/installing/).

### 2. Клонирование репозитория

1. Откройте командную строку или терминал.
2. Перейдите в папку, где вы хотите разместить проект:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>cd path/to/your/folder</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">cd path/to/your/folder
   </code></div></div></pre>
3. Склонируйте репозиторий с GitHub:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>git clone https://github.com/IkayevAibar/book_catalog.git</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/IkayevAibar/book_catalog.git
   </code></div></div></pre>

### 3. Установка зависимостей

1. Перейдите в папку проекта:
   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>cd book_catalog</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">cd book_catalog
   </code></div></div></pre>
2. Создайте виртуальное окружение (опционально, но рекомендуется):
   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python -m venv venv</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python -m venv venv
   </code></div></div></pre>
3. Активируйте виртуальное окружение:
   * На Windows:
     <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>venv\Scripts\activate</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">venv\Scripts\activate
     </code></div></div></pre>
   * На macOS и Linux:
     <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>source venv/bin/activate</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">source venv/bin/activate
     </code></div></div></pre>
4. Установите зависимости из файла `requirements.txt`:
   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>pip install -r requirements.txt</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
   </code></div></div></pre>

### 4. Запуск сервера

1. Запустите сервер разработки Django:
   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python manage.py runserver</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python manage.py runserver
   </code></div></div></pre>
2. Откройте веб-браузер и перейдите по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/) для доступа к проекту.

Теперь вы можете приступить к проверки проекта "Каталог книг". Удачи!
