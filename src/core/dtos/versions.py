from pydantic import BaseModel, Field, NonNegativeInt


class MajorVersionDTO(BaseModel):
    major_version: NonNegativeInt = Field(default=0)


class MinorVersionDTO(BaseModel):
    minor_version: NonNegativeInt = Field(default=0)


class PatchVersionDTO(BaseModel):
    patch_version: NonNegativeInt = Field(default=0)
