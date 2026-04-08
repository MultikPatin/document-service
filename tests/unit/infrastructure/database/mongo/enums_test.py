from src.infrastructure.database.mongo.enums import KeyEnum


def test_key_enum_id_value():
    """Test that KeyEnum.id returns '_id' without $ prefix."""
    assert KeyEnum.id == "_id"


def test_key_enum_gte_value():
    """Test that KeyEnum.gte returns '$gte' operator."""
    assert KeyEnum.gte == "$gte"


def test_key_enum_gt_value():
    """Test that KeyEnum.gt returns '$gt' operator."""
    assert KeyEnum.gt == "$gt"


def test_key_enum_lte_value():
    """Test that KeyEnum.lte returns '$lte' operator."""
    assert KeyEnum.lte == "$lte"


def test_key_enum_lt_value():
    """Test that KeyEnum.lt returns '$lt' operator."""
    assert KeyEnum.lt == "$lt"


def test_key_enum_match_value():
    """Test that KeyEnum.match returns '$match' operator."""
    assert KeyEnum.match == "$match"


def test_key_enum_lookup_value():
    """Test that KeyEnum.lookup returns '$lookup' operator."""
    assert KeyEnum.lookup == "$lookup"


def test_key_enum_unwind_value():
    """Test that KeyEnum.unwind returns '$unwind' operator."""
    assert KeyEnum.unwind == "$unwind"


def test_key_enum_project_value():
    """Test that KeyEnum.project returns '$project' operator."""
    assert KeyEnum.project == "$project"


def test_key_enum_set_value():
    """Test that KeyEnum.set returns '$set' operator."""
    assert KeyEnum.set == "$set"


def test_key_enum_sort_value():
    """Test that KeyEnum.sort returns '$sort' operator."""
    assert KeyEnum.sort == "$sort"


def test_key_enum_skip_value():
    """Test that KeyEnum.skip returns '$skip' operator."""
    assert KeyEnum.skip == "$skip"


def test_key_enum_limit_value():
    """Test that KeyEnum.limit returns '$limit' operator."""
    assert KeyEnum.limit == "$limit"


def test_key_enum_facet_value():
    """Test that KeyEnum.facet returns '$facet' operator."""
    assert KeyEnum.facet == "$facet"


def test_key_enum_count_value():
    """Test that KeyEnum.count returns '$count' operator."""
    assert KeyEnum.count == "$count"


def test_key_enum_all_value():
    """Test that KeyEnum.all returns '$all' operator."""
    assert KeyEnum.all == "$all"


def test_key_enum_regex_value():
    """Test that KeyEnum.regex returns '$regex' operator."""
    assert KeyEnum.regex == "$regex"


def test_key_enum_options_value():
    """Test that KeyEnum.options returns '$options' operator."""
    assert KeyEnum.options == "$options"


def test_key_enum_in_value():
    """Test that KeyEnum.in_ returns '$in' operator."""
    assert KeyEnum.in_ == "$in"


def test_key_enum_inc_value():
    """Test that KeyEnum.inc returns '$inc' operator."""
    assert KeyEnum.inc == "$inc"


def test_key_enum_string_behavior():
    """Test that KeyEnum members behave as strings since StrEnum inherits from str."""
    assert isinstance(KeyEnum.gte, str)
    assert isinstance(KeyEnum.id, str)
    assert len(KeyEnum.gte) > 0
    assert KeyEnum.gte.startswith("$")
    assert KeyEnum.id == "_id"  # Special case without $


def test_key_enum_concatenation():
    """Test that KeyEnum members can be used in string concatenation operations."""
    result = KeyEnum.gte + "_operator"
    assert result == "$gte_operator"

    path = "filter" + KeyEnum.gt
    assert path == "filter$gt"


def test_key_enum_comparison():
    """Test that KeyEnum members can be used in string comparison operations."""
    assert KeyEnum.sort == "$sort"
    assert KeyEnum.sort != "$group"
    assert KeyEnum.lte > "$lt"  # Lexicographic comparison
    assert KeyEnum.gte > "$eq"


def test_key_enum_membership():
    """Test that KeyEnum members can be used in membership tests."""
    query_operator = KeyEnum.match
    assert query_operator in ["$match", "$filter", "$project"]
    assert "$unknown" not in [KeyEnum.gte, KeyEnum.lt, KeyEnum.in_]


def test_key_enum_formatting():
    """Test that KeyEnum members can be used in string formatting operations."""
    template = "Using {} operator"
    assert template.format(KeyEnum.project) == "Using $project operator"

    f_string = f"Aggregation uses {KeyEnum.lookup}"
    assert f_string == "Aggregation uses $lookup"


def test_key_enum_iteration():
    """Test that KeyEnum members maintain string iteration behavior."""
    chars = list(KeyEnum.sort)
    assert chars == ["$", "s", "o", "r", "t"]

    assert "gte" in KeyEnum.gte  # Substring search
    assert "$" in KeyEnum.gte
    assert "_" in KeyEnum.id  # Special case with _id


def test_key_enum_all_members_present():
    """Test that all expected enum members are present in KeyEnum."""
    expected_members = [
        "id",
        "gte",
        "gt",
        "lte",
        "lt",
        "match",
        "lookup",
        "unwind",
        "project",
        "set",
        "sort",
        "skip",
        "limit",
        "facet",
        "count",
        "all",
        "regex",
        "options",
        "in_",
        "inc",
    ]

    # Get all member names from the enum
    actual_members = [member.name for member in KeyEnum]

    assert sorted(actual_members) == sorted(expected_members)


def test_key_enum_all_values_correct():
    """Test that all enum members have correct string values with $ prefix except id."""
    # Special case for id
    assert KeyEnum.id.value == "_id"

    # All other members should have $ prefix
    for member in KeyEnum:
        if member.name != "id":
            assert member.value.startswith("$"), (
                f"{member.name} value '{member.value}' should start with $"
            )

    # Verify specific mappings
    assert KeyEnum.gte.value == "$gte"
    assert KeyEnum.gt.value == "$gt"
    assert KeyEnum.lte.value == "$lte"
    assert KeyEnum.lt.value == "$lt"
    assert KeyEnum.match.value == "$match"
    assert KeyEnum.lookup.value == "$lookup"
    assert KeyEnum.unwind.value == "$unwind"
    assert KeyEnum.project.value == "$project"
    assert KeyEnum.set.value == "$set"
    assert KeyEnum.sort.value == "$sort"
    assert KeyEnum.skip.value == "$skip"
    assert KeyEnum.limit.value == "$limit"
    assert KeyEnum.facet.value == "$facet"
    assert KeyEnum.count.value == "$count"
    assert KeyEnum.all.value == "$all"
    assert KeyEnum.regex.value == "$regex"
    assert KeyEnum.options.value == "$options"
    assert KeyEnum.in_.value == "$in"
    assert KeyEnum.inc.value == "$inc"
