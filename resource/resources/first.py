from resource.resource import Resource


class First(Resource):
    address = "in"

    @staticmethod
    def get():
        return {
            "test": 1
        }
