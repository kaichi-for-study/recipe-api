def recipe_response(recipes: list) -> dict:
    return {
        "result_code": RESULT_CODE_SUCCESS,
        "result_message": MESSAGE_SUCCESS,
        "data": {"count": len(recipes), "recipes": recipes},
    }
