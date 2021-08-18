from flask import Flask
from flask_restful import Api

from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource

app = Flask(__name__)
api = Api(app)

"""Add resource routing by passing in the URL. 
This will route directly to our resources for easiest management. 
Each resource will have its own HTTP method defined"""

api.add_resource(RecipeListResource, "/recipes")
api.add_resource(RecipeResource, "/recipes/<int:recipe_id>")
api.add_resource(RecipePublishResource, "/recipes/<int:recipe_id>/publish")

if __name__ == "__main__":
    app.run()