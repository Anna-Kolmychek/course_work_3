from dao.comments_dao import CommentsDAO
from config import PATH_TO_COMMENTS

import pytest

@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO(PATH_TO_COMMENTS)
    return comments_dao_instance


keys_should_be = {'post_id',
                  'commenter_name',
                  'comment',
                  'pk',
                  }


class TestCommentsDAO:

    def test_get_by_post_id(self, comments_dao):
        comments = comments_dao.get_by_post_id(1)
        assert type(comments) == list, 'возвращает не список'
        if len(comments) > 0:
            assert set(comments[0].keys()) == keys_should_be, 'неверный список ключей'
            assert comments[0]['post_id'] == 1, 'возвращает неверную выборку комментов'
