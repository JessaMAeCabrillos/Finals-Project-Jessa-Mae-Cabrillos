from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory recipe storage
recipes = [
    {
        "id": 1,
        "title": "Spaghetti Carbonara",
        "ingredients": "Spaghetti, Eggs, Pancetta, Parmesan, Pepper",
        "instructions": "1. Cook pasta. 2. Fry pancetta. 3. Mix eggs with Parmesan. 4. Combine all."
    },
    {
        "id": 2,
        "title": "Pancakes",
        "ingredients": "Flour, Milk, Eggs, Sugar, Butter",
        "instructions": "1. Mix ingredients. 2. Cook on a griddle. 3. Serve with syrup."
    }
]

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)
    if recipe:
        return render_template('recipe.html', recipe=recipe)
    return "Recipe not found.", 404

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')

        # Validate inputs
        if not title or not ingredients or not instructions:
            return "All fields are required!", 400

        # Create a new recipe
        new_id = len(recipes) + 1
        recipes.append({
            "id": new_id,
            "title": title.strip(),
            "ingredients": ingredients.strip(),
            "instructions": instructions.strip()
        })
        return redirect(url_for('index'))

    # Render add recipe form
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
