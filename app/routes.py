from flask import render_template, url_for, flash, redirect
from app import app
from app.models import Recipe

@app.route("/")
@app.route("/home")
def home():
    recipes = Recipe.query.all()
    return render_template('home.html', recipes=recipes)

@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', title=recipe.title, recipe=recipe)
