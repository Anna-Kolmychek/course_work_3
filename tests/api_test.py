keys_should_be = {'poster_name',
                  'poster_avatar',
                  'pic',
                  'content',
                  'views_count',
                  'likes_count',
                  'pk',
                  }


class TestAPI:

    def test_api_posts(self, test_client):
        response = test_client.get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, 'возвращает не список'
        assert set(response.json[0].keys()) == keys_should_be, 'неверный список ключей'

    def test_api_post_by_id(self, test_client):
        response = test_client.get('api/posts/1', follow_redirects=True)
        assert type(response.json) == dict, 'возвращает не словарь (не пост)'
        assert set(response.json.keys()) == keys_should_be, 'неверный список ключей'
