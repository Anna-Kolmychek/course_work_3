# Курсовая работа № 3
Разработчик: Колмычек Анна

### Краткое описание
Реализована лента постов с возможностью
поиска по контенту постов, фильтрами по разным параметрам,
добавлением/удалением повтов в закладки 
и просмотром полного текста отдельного поста.
Также проект содержит api для получения json данных по всем постам
и json данные поста по id. 

### Демо
[![Demo](https://drive.google.com/thumbnail?authuser=0&sz=w1280&id=1yn704qL7xyRA0jlTb2ReRbBKljpeMhUk)](https://drive.google.com/file/d/1yn704qL7xyRA0jlTb2ReRbBKljpeMhUk/view?usp=sharing "Demo")

### Состав

- **Главная страница (/)**
  - Выведены все посты в коротком формате.
  - Реализованы
    - стандартный набор функций работы с постами,
    - поиск по контенту,
    - переход к постам в закладках.


- **Страница поста (/posts/&lt;int:post_id&gt;/)**
  - Выведена вся информация по посту и комментарии к нему.
  - Реализованы
    - стандартный набор функций работы с постами,
    - возврат на главную,
    - переход к постам по тегу (если есть в контенте).


- **Страница поиска (/search/)**
  - Выведены посты в коротком формате, содержащие подстроку поискового запроса. Отображается количество найденных постов. Выводятся первые 10 постов. 
  - Реализованы
    - стандартный набор функций работы с постами,
    - возврат на главную,
    - новый поиск по контенту.


- **Страница постов по тегу (/tag/&lt;tag_name&gt;')**
  - Выведены посты в коротком формате, содержащие тег.
  - Реализованы
    - стандартный набор функций работы с постами,
    - возврат на главную.


- **Страница постов по автору ('/users/&lt;username&gt;/')**
  - Выведены посты в коротком формате указанного автора.
  - Реализованы
    - стандартный набор функций работы с постами,
    - возврат на главную.


- **Страница постов в закладках ('/bookmarks/')**
  - Выведены посты в коротком формате, помещенные в заклакди.
  - Реализованы
    - стандартный набор функций работы с постами,
    - возможность удалить пост из закладок,
    - возврат на главную.


- **Страница обработки ошибок 404, 500**
  - Выведен соответствующий текст ошибки. Реализован возврат на главную.


- **api для получения всех постов ('/api/posts/')**
  - Возвращает json со всеми постами.
  - Добвляется запись в логи при обращении к api.


- **api для получения поста по его id ('/api/posts/&lt;int:post_id&gt;/')**
  - Возвращает json с постом по указанному id.
  - Добвляется запись в логи при обращении к api.


> **Стандартный набор функций работы с постами**
> - добавить пост в закладки,
> - перейти ко всем постам автора,
> - перейти к полному тексту поста.


### Технологии
Python, Flask, Jinja2, Pytest, Logging. 

### Особенности
Данные берутся из json-файлов в проекте.
Пути к файлам прописаны в файле config.py
Для обработки данных реализованы классы DAO.
К классам DAO, представлениям и api разработаны тесты.