import json


# Класс работы с данными из posts
class PostsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        """загрузка данных из файла"""
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_all(self) -> list[dict]:
        """возвращает все посты"""
        posts = self.load_data()
        return posts

    def get_by_pk(self, pk: int) -> dict:
        """возвращает пост по заданному pk"""
        posts = self.load_data()
        for post in posts:
            if post['pk'] == pk:
                return self.convert_tags_in_links(post)

    def get_by_query(self, query: str) -> list[dict]:
        """возвращает все посты, содержащине в content подстроку query
        используется для страницы поиска"""
        posts = self.load_data()
        posts_by_query = []
        query = query.lower().strip()
        for post in posts:
            if query in post['content'].lower():
                posts_by_query.append(post)

        return posts_by_query

    def get_by_author(self, author: str) -> list[dict]:
        """возвращает все посты автора author"""
        posts = self.load_data()
        posts_by_author = []
        for post in posts:
            if author == post['poster_name']:
                posts_by_author.append(post)

        return posts_by_author

    def get_by_tag(self, tag: str) -> list[dict]:
        """возращает все посты, в которых есть тег tag"""
        posts = self.load_data()
        tag = f'#{tag}'
        posts_by_tag = []
        for post in posts:
            if tag in post['content'].split():
                posts_by_tag.append(post)

        return posts_by_tag

    def convert_tags_in_links(self, post: dict) -> dict:
        """возращает пост после обработки содержимого content
        меняет теги на ссылки"""
        words = post['content'].split()
        new_words = []
        for word in words:
            if word[0] == '#':
                new_words.append(f'<a href="/tag/{word[1:]}">{word}</a>')
            else:
                new_words.append(word)

        post['content'] = ' '.join(new_words)
        return post

    def get_by_list_of_id(self, list_of_id: list) -> list[dict]:
        """возращает список всех постов, pk которых находится в списке list_of_id"""
        posts = self.load_data()
        posts_by_list = []
        for post in posts:
            if post['pk'] in list_of_id:
                posts_by_list.append(post)

        return posts_by_list
