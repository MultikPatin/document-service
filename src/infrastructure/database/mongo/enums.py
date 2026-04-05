from enum import StrEnum


class KeyEnum(StrEnum):
    id = "_id"
    gte = "$gte"
    gt = "$gt"
    lte = "$lte"
    lt = "$lt"
    match = "$match"
    lookup = "$lookup"
    unwind = "$unwind"
    project = "$project"
    set = "$set"
    sort = "$sort"
    skip = "$skip"
    limit = "$limit"
    facet = "$facet"
    count = "$count"
    all = "$all"
    regex = "$regex"
    options = "$options"
    in_ = "$in"
    inc = "$inc"
