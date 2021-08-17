recipe_list = []

"""Define function to get last recipe ID. This way we can add new ID's as new recipes are added"""

def get_last_id():
    if recipe_list:
        last_recipe = recipe_list[-1]
    else:
        return 1
    return last_recipe.id + 1

class Recipe:

    """Creates recipe object based on the following parameters:
    name, description, num_of_servings, cook_time, and directions"""

    def __init__(self, name, description, num_of_servings, cook_time, directions):
        self.id = get_last_id() # Self incrementing IDs
        self.name = name
        self.description = description
        self.num_of_servings = num_of_servings
        self.cook_time = cook_time
        self.directions = directions
        self.is_publish = False # By default the recipe is set to draft (not published)

    """Define the data method for returning the data as a dictionary object"""

    @property
    def data(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "num_of_servings": self.num_of_servings,
            "cook_time": self.cook_time,
            "directions": self.directions
        }