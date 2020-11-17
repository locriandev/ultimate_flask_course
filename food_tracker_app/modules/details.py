from modules import food
from modules.dates import get_date_id


def get_daily_food(date):
    date_id = get_date_id(date)
    food_for_date = food.get_food_for_date(date_id)
    return [food.get_food_from_food_id(food_id)
            for food_id in food_for_date]
