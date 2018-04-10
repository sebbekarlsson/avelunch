from flask import Blueprint, render_template
from avenyn_lunch.AvenySession import AvenySession
from avenyn_lunch.constants import DAYS
import datetime


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/<day>')
@bp.route('/', defaults={'day': None})
def show(day):
    session = AvenySession()

    restaurants = session.get_restaurants()

    if not restaurants:
        return 'Failed to fetch restaurants', 500

    day = datetime.datetime.now().weekday() if not day else int(day)
    day = len(DAYS) - 1 if day < 0 else 0 if day > len(DAYS) - 1 else day

    dayname = DAYS[day]

    for restaurant in restaurants:
        restaurant.menu = restaurant.weekly_menu[day]

    return render_template(
        'index.html',
        restaurants=restaurants,
        dayname=dayname,
        day=day
    )
