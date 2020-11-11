from datetime import date
from app.followers_repository import row_to_dict, rows_to_list_of_dict


def test_row_to_dict():
    row = (date(2020, 11, 2), 102)
    result = row_to_dict(row)
    assert result.get("followers") == 102
    assert result.get("as_of_date") == date(2020, 11, 2)

def test_row_to_list_dict():
    row1 = (date(2020, 11, 2), 102)
    row2 = (date(2020, 11, 3), 103)
    rows = [row1, row2]
    result = rows_to_list_of_dict(rows)
    assert len(result) == 2
    assert result[0].get("followers") == 102
    assert result[0].get("as_of_date") == date(2020, 11, 2)
    assert result[1].get("followers") == 103
    assert result[1].get("as_of_date") == date(2020, 11, 3)