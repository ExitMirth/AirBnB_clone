#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

    def test_str_method(self):
        my_model = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(
                my_model.id,
                my_model.__dict__
                )
        self.assertEqual(expected_output, str(my_model))

    def test_save_method(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        self.assertEqual(my_model_json['__class__'], "BaseModel")
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertIn('id', my_model_json)
        self.assertIn('created_at', my_model_json)
        self.assertIn('updated_at', my_model_json)


if __name__ == '__main__':
    unittest.main()
