class TestViews:

    def test_main(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код главной страницы неверный'

    def test_post(self, test_client):
        response = test_client.get('/posts/1', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы поста неверный'

    def test_search(self, test_client):
        response = test_client.get('/search', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы поиска неверный'

    def test_user_feed(self, test_client):
        response = test_client.get('/users/leo', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы постов пользователя неверный'

    def test_teg(self, test_client):
        response = test_client.get('/tag/еда', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы постов пользователя неверный'

    def test_click_bookmarks(self, test_client):
        response = test_client.get('/bookmarks/1', follow_redirects=True)
        assert response.status_code == 200, 'Статус-код страницы постов пользователя неверный'
