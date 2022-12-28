from dao.bookmarks_dao import BookmarksDAO
from config import PATH_TO_BOOKMARKS

import pytest


@pytest.fixture()
def bookmarks_dao():
    bookmarks_dao_instanse = BookmarksDAO(PATH_TO_BOOKMARKS)
    return bookmarks_dao_instanse


class TestBookmarksDAO:

    def test_get_all(self, bookmarks_dao):
        bookmarks = bookmarks_dao.get_all()
        assert type(bookmarks) == list, 'возвращает не список'
        if len(bookmarks) > 0:
            assert type(bookmarks[0]) == int, 'в списке не int (не id)'

    def test_get_count_bookmarks_posts(self, bookmarks_dao):
        count_bookmarks_posts = bookmarks_dao.get_count_bookmarks_posts()
        assert type(count_bookmarks_posts) == int, 'возвращает не количество'
