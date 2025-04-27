from data.recipes import RECIPE_LIST


class RecipeModel:
    # レシピのリストを初期化
    def __init__(self):
        self.recipe = RECIPE_LIST

    # レシピのリストを取得
    def find_recipes(self, ingredients: list, buget: int) -> list:

        # レシピの材料が全てingredientsに含まれている かつ 予算内であればレシピを追加
        available_recipes = []
        for recipe in self.find_recipes:
            if (
                set(recipe["ingredients"]).issubset(set(ingredients))
                and recipe["price"] <= buget
            ):
                available_recipes.append(recipe)

        return available_recipes
