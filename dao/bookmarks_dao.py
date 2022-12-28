import json


# Класс работы с данными из bookmarks
class BookmarksDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self) -> list:
        """загрузка данных из файла"""
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def save_data(self, data: list) -> None:
        """сохранение данных data в файл"""
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file)
        return

    def get_all(self) -> list[int]:
        """возвращает все id постов, записанных в bookmarks"""
        bookmarks_posts = self.load_data()
        return bookmarks_posts

    def add_in_bookmarks(self, post_id: int):
        """добавляет post_id в bookmarks
        возвращает обновленный список id постов в bookmarks(можно не использовать)"""
        bookmarks_posts = self.load_data()
        if post_id not in bookmarks_posts:
            bookmarks_posts.append(post_id)
            self.save_data(bookmarks_posts)
        return bookmarks_posts

    def remove_from_bookmarks(self, post_id: int):
        """удаляет post_id из bookmarks
        возвращает обновленный список id постов в bookmarks(можно не использовать)"""
        bookmarks_posts = self.load_data()
        if post_id in bookmarks_posts:
            bookmarks_posts.remove(post_id)
            self.save_data(bookmarks_posts)
        return bookmarks_posts

    def get_count_bookmarks_posts(self):
        """возвращает количество id постов, записанных в bookmarks"""
        bookmarks_posts = self.load_data()
        return len(bookmarks_posts)
