import logging
import curlify
from requests import Response
from pytest_voluptuous import S
from model.schemas import pets_shema
from model.versions.petstore_pet import PetApi




class TestPositivePet:


    def test_create_pet(self):
        pet_api = PetApi()
        result: Response = pet_api.create_new_pet(
            pet_id=163634637, category_id=16633666,
            category_name="dog", pet_name="Stvol",
            url_photos="photo", tag_id=144034,
            tag_name="big", state="available"
        )
        logging.info(curlify.to_curl(result.request))
        logging.info(result.json())

        assert result.status_code == 200
        assert result.json()["id"] == 163634637
        assert S(pets_shema.get_single_pet) == result.json()


    def test_check_new_pet(self):
        pet_api = PetApi()
        result: Response = pet_api.get_single_pet(pet_id=163634637)
        logging.info(curlify.to_curl(result.request))
        logging.info(result.status_code)

        assert result.status_code == 200
        assert S(pets_shema.get_single_pet) == result.json()


