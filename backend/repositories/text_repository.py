from pony.orm import db_session, commit
from entities.text_entry import TextEntry


class TextRepository:
    @db_session
    def create_text(self, content):
        text_entry = TextEntry(content=content)
        commit()
        return {"id": text_entry.id, "content": text_entry.content}

    @db_session
    def get_all_texts(self):
        result = []
        for text_entry in TextEntry.select():
            result.append({"id": text_entry.id, "content": text_entry.content})
        return result
