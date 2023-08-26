from model.versions.base_api import BaseApi


class PetApi(BaseApi):
    base_url = "https://petstore.swagger.io/v2"
    @classmethod
    def data_filling(cls, pet_id, category_id,
               category_name, pet_name,
               url_photos, tag_id, tag_name,
               state
               ):
        body = {
            "id": pet_id,
            "category": {
                "id": category_id,
                "name": category_name
            },
            "name": pet_name,
            "photoUrls": [
                url_photos
            ],
            "tags": [
                {
                    "id": tag_id,
                    "name": tag_name
                }
            ],
            "status": state
        }
        return body

    def create_new_pet(
            self, pet_id, category_id,
               category_name, pet_name,
               url_photos, tag_id, tag_name,
               state

    ):
        path = "/pet"
        body = PetApi.data_filling(pet_id, category_id,
               category_name, pet_name,
               url_photos, tag_id, tag_name,
               state)

        post_result = self.post(self.base_url + path, body)

        return post_result


    def get_single_pet(self, pet_id):
        path = f'/pet/{pet_id}'

        get_result = self.get(self.base_url + path)

        return get_result

    def put_single_pet(
            self, pet_id, category_id,
               category_name, pet_name,
               url_photos, tag_id, tag_name,
               state

    ):
        path = "/pet"
        body = PetApi.data_filling(
            pet_id, category_id,
            category_name, pet_name,
            url_photos, tag_id, tag_name,
            state
        )

        put_result = self.put(self.base_url + path, body)

        return put_result