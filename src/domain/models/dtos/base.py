from pydantic import BaseModel, Field, NegativeInt

from src.domain.utils import hash_md5


class HashDTO(BaseModel):
    hash: str = Field(default="", min_length=8, max_length=255)
    ref_count: NegativeInt = Field(default=0)

    def can_be_deleted(self) -> bool:
        return self.ref_count == 0

    def calculate_hash(self) -> str:
        return hash_md5(self.model_dump(exclude={"hash", "id", "ref_count"}))

    def refresh_hash(self) -> None:
        exclude = {"hash", "id", "ref_count"}
        self.hash = hash_md5(self.model_dump(exclude=exclude))

    def get_hash(self) -> str:
        self.refresh_hash()
        return self.hash

    def set_hash(self) -> None:
        self.hash = self.calculate_hash()
