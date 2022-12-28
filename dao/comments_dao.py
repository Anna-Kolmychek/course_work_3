import json


# Класс работы с комментариями из comments
class CommentsDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        """чтение данных из файла"""
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_by_post_id(self, post_id: int) -> list[dict]:
        """возвращает все комментарии к указанному post_id"""
        comments = self.load_data()
        comments_by_post_id = []
        for comment in comments:
            if comment['post_id'] == post_id:
                comments_by_post_id.append(comment)
        return comments_by_post_id
