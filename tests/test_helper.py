# encoding: utf-8
from datetime import date

from freezegun import freeze_time
from unittest import TestCase, main

from helper import get_days_ago, convert_dict_to_pascalcase


class TestLogger(TestCase):
    @freeze_time("2017-01-10")
    def test_get_days_ago(self):
        self.assertEqual(get_days_ago(5), date(2017, 1, 5))

    def test_get_days_ago_send_reference_day(self):
        result = get_days_ago(5, reference_day=date(2017, 2, 5))
        self.assertEqual(result, date(2017, 1, 31))

    def test_simple_convert_dict_to_pascalcase(self):
        base = {
            "object": 1,
            "my_object": 2,
            "my_object_name": "Jonh test"
        }
        result = {
            "object": 1,
            "myObject": 2,
            "myObjectName": "Jonh test"
        }
        self.assertEqual(convert_dict_to_pascalcase(base), result)

    def test_complex_convert_dict_to_pascalcase(self):
        base = {
            "id": 1,
            "my_id": 2,
            "my_id_name": "John test",
            "object": {
                "id": 1,
                "my_id": 2,
                "my_id_name": "John test",
                "sub_object": {
                    "id": 1,
                    "my_id": 2,
                    "my_id_name": "John test"
                }
            }
        }
        result = {
            "id": 1,
            "myId": 2,
            "myIdName": "John test",
            "object": {
                "id": 1,
                "myId": 2,
                "myIdName": "John test",
                "subObject": {
                    "id": 1,
                    "myId": 2,
                    "myIdName": "John test"
                }
            }
        }
        self.assertEqual(convert_dict_to_pascalcase(base), result)


if __name__ == '__main__':
    main()
