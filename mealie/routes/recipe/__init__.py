from fastapi import APIRouter
from mealie.routes.recipe import all_recipe_routes, category_routes, comments, recipe_crud_routes, tag_routes

recipe_router = APIRouter()

recipe_router.include_router(all_recipe_routes.router)
recipe_router.include_router(recipe_crud_routes.router)
recipe_router.include_router(category_routes.router)
recipe_router.include_router(tag_routes.router)
recipe_router.include_router(comments.router)
