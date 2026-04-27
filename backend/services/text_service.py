from repositories.text_repository import TextRepository


class TextService:

    def __init__(self):
        self.text_repository = TextRepository()

    def create_text(self, content):
        if not content or not content.strip():
            return {"error": "content is required"}, 400
        saved_text = self.text_repository.create_text(content.strip())
        return saved_text, 201

    def get_all_text(self):
        texts = self.text_repository.get_all_texts()
        return texts, 200
