from dao.posts_dao import PostsDAO
from config import PATH_TO_POSTS

import pytest

@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO(PATH_TO_POSTS)
    return posts_dao_instance

keys_should_be = {'poster_name',
                  'poster_avatar',
                  'pic',
                  'content',
                  'views_count',
                  'likes_count',
                  'pk',
                  }

class TestPostsDAO:

    def test_get_all(self, posts_dao):
        posts = posts_dao.get_all()
        assert type(posts) == list, 'возвращается не список'
        assert len(posts) > 0, 'возвращается пустой список'
        assert set(posts[0].keys()) == keys_should_be, 'неверный список ключей'

    def test_get_by_pk(self, posts_dao):
        post = posts_dao.get_by_pk(1)
        assert type(post) == dict, 'возвращается не словарь (не пост)'
        assert post['pk'] == 1, 'возвращается неправильный пост'
        assert set(post.keys()) == keys_should_be, 'неверный список ключей'

    def test_get_by_query(self, posts_dao):
        posts = posts_dao.get_by_query('кот')
        assert type(posts) == list, 'возвращается не список'
        if len(posts) > 0:
            assert set(posts[0].keys()) == keys_should_be, 'неверный список ключей'
            assert 'кот' in posts[0]['content'].lower(), 'неверная выборка потов'

    def test_get_by_author(self, posts_dao):
        posts = posts_dao.get_by_author('leo')
        assert type(posts) == list, 'возвращается не список'
        if len(posts) > 0:
            assert set(posts[0].keys()) == keys_should_be, 'неверный список ключей'
            assert posts[0]['poster_name'] == 'leo', 'неверная выборка постов'

    def test_get_by_tag(self, posts_dao):
        posts = posts_dao.get_by_tag('еда')
        assert type(posts) == list, 'возвращает не список'
        if len(posts) > 0:
            assert set(posts[0].keys()) == keys_should_be, 'неверный список ключей'
            assert '#еда' in posts[0]['content'], 'неверная выборка постов'

    def test_get_by_list_of_id(self, posts_dao):
        posts = posts_dao.get_by_list_of_id([1, 2])
        assert type(posts) == list, 'возвращает не список'
        if len(posts) > 0:
            assert set(posts[0].keys()) == keys_should_be, 'неверный список ключей'
            assert posts[0]['pk'] in [1, 2], 'неверная выборка постов'


