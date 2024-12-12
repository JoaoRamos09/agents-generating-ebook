from pydantic import BaseModel, Field
from typing_extensions import Optional
from graph.models.responses.ResumeChapter import ResumeChapterResponse
class StructuringEbookResponse(BaseModel):
    chapters: Optional[list[ResumeChapterResponse]] = (Field(description="A lista de capítulos do ebook, com o título, as palavras chaves, o resumo e o número do capítulo"))
  