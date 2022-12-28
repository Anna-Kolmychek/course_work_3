from flask import Flask, render_template, request, jsonify, redirect
import logging
from dao.posts_dao import PostsDAO
from dao.comments_dao import CommentsDAO
from dao.bookmarks_dao import BookmarksDAO


# Задаем настройки для логгера
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler = logging.FileHandler('./logs/api.log', encoding='utf-8')
handler.setFormatter(formatter)

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


# Иницилизируем приложение и добавляем настройки
app = Flask(__name__)

app.config.from_pyfile('config.py')
app.json.ensure_ascii = False


# Объявляем dao для работы с постами, комментами и закладками
posts_dao = PostsDAO(app.config.get('PATH_TO_POSTS'))
comments_dao = CommentsDAO(app.config.get('PATH_TO_COMMENTS'))
bookmarks_dao = BookmarksDAO(app.config.get('PATH_TO_BOOKMARKS'))


# Представление главной страницы
@app.route('/')
def page_index():
    posts = posts_dao.get_all()
    count_bookmarks_posts = bookmarks_dao.get_count_bookmarks_posts()
    return render_template('index.html', posts=posts, count_bookmarks_posts=count_bookmarks_posts)


# Представление страницы поста
@app.route('/posts/<int:post_id>/')
def page_post(post_id):
    post = posts_dao.get_by_pk(post_id)
    comments = comments_dao.get_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)


# Представление страницы поиска
@app.route('/search/')
def page_search():
    query = request.args.get('s')
    posts = posts_dao.get_by_query(query)
    return render_template('search.html', posts=posts)


# Представление страницы постов пользователя
@app.route('/users/<username>/')
def page_user_feed(username):
    posts = posts_dao.get_by_author(username)
    return render_template('user-feed.html', posts=posts)


# Представление страницы постов по тегам
@app.route('/tag/<tag_name>')
def page_tag(tag_name):
    posts = posts_dao.get_by_tag(tag_name)
    return render_template('tag.html', posts=posts, tag_name=tag_name)


# Обработка добавления поста в закладки
@app.route('/bookmarks/add/<int:post_id>')
def add_in_bookmarks(post_id):
    bookmarks_dao.add_in_bookmarks(post_id)
    return redirect("/", code=302)


# Обработка удаления поста из закладок
@app.route('/bookmarks/remove/<int:post_id>')
def remove_from_bookmarks(post_id):
    bookmarks_dao.remove_from_bookmarks(post_id)
    return redirect("/", code=302)


# Представление страницы с постами из закладок
@app.route('/bookmarks/')
def page_bookmarks():
    bookmarks_posts = bookmarks_dao.get_all()
    posts = posts_dao.get_by_list_of_id(bookmarks_posts)
    return render_template('bookmarks.html', posts=posts)


# Представление api для получения json всех постов
@app.route('/api/posts/')
def get_all_posts_json():
    posts = posts_dao.get_all()
    logger.info('Запрос /api/posts')
    return jsonify(posts)


# Представление api для получения json поста с указанным id
@app.route('/api/posts/<int:post_id>/')
def get_post_by_id_json(post_id):
    post = posts_dao.get_by_pk(post_id)
    logger.info(f'Запрос /api/posts/{post_id}')
    return jsonify(post)


# Обработка ошибки 404
@app.errorhandler(404)
def page_not_found(e):
    message = 'Страница не найдена'
    return render_template('error.html', message=message)


# Обработка ошибки 500
@app.errorhandler(500)
def page_not_found(e):
    message = 'Ошибка на сервере'
    return render_template('error.html', message=message)


if __name__ == '__main__':
    app.run()
