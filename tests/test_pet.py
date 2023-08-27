import logging
import pytest
import curlify
from requests import Response
from pytest_voluptuous import S
from model.schemas import pets_schema
from model.versions.petstore_pet import PetApi




class TestPositivePet:

    @pytest.mark.parametrize("pet_id", [163634637])
    def test_create_pet(self, pet_id):
        pet_api = PetApi()
        result: Response = pet_api.create_new_pet(
            pet_id=pet_id,
            category_id=16633666,
            category_name="dog", pet_name="Stvol",
            url_photos="photo", tag_id=144034,
            tag_name="big", state="available"
        )
        logging.info(curlify.to_curl(result.request))

        assert result.status_code == 200
        assert result.json()["id"] == pet_id
        assert S(pets_schema.get_single_pet) == result.json()

    @pytest.mark.parametrize("pet_id", [163634637])
    def test_check_new_pet(self, pet_id):
        pet_api = PetApi()
        result: Response = pet_api.get_single_pet(pet_id=pet_id)

        logging.info(curlify.to_curl(result.request))
        logging.info(result.status_code)

        assert result.status_code == 200
        assert S(pets_schema.get_single_pet) == result.json()

    @pytest.mark.parametrize("pet_name", ["Shakira"])
    def test_data_filling_pet(self, pet_name):
        pet_api = PetApi()

        result: Response = pet_api.put_single_pet(
            pet_id=163634637, category_id=16633666,
            category_name="dog",
            pet_name=pet_name,
            url_photos="photo", tag_id=144034,
            tag_name="big", state="available"
        )
        logging.info(curlify.to_curl(result.request))

        assert result.status_code == 200
        assert result.json()["name"] == pet_name
        assert S(pets_schema.put_single_pet) == result.json()
    #
    #
    # # TODO: разобраться, почему не проставляется новый статус
    @pytest.mark.parametrize("pet_state", ["pending"])
    def test_data_filling_state_pet(self, pet_state):
        pet_api = PetApi()
        get_pet = pet_api.get_single_pet(pet_id=163634637)

        result: Response = pet_api.post_status_single_pet(pet_id=163634637, state=pet_state)
        # result: Response = requests.post("https://petstore.swagger.io/v2/pet/163634637?status=pending")
        logging.info(curlify.to_curl(result.request))
        logging.info(result.json())

        assert result.status_code == 200
        assert get_pet.json()["status"] == pet_state
        assert S(pets_schema.three_default_values) == result.json()


    @pytest.mark.parametrize("pet_id", [163634637])
    def test_delete_single_pet(self, pet_id):
        pet_api = PetApi()

        result: Response = pet_api.delete_single_pet(pet_id=pet_id)
        logging.info(curlify.to_curl(result.request))

        assert result.status_code == 200
        assert result.json()["message"] == str(pet_id)
        assert pet_api.get_single_pet(pet_id=pet_id).json()["message"] == "Pet not found"
        assert S(pets_schema.three_default_values) == result.json()
