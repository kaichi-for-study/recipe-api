from constants.app_constants import AppConstants


def recipe_response(result_code, recipes: list) -> dict:
    return {
        "result_code": result_code,
        "result_message": AppConstants.RESULT_MESSAGE[result_code],
        "data": {"count": len(recipes), "recipes": recipes},
    }
