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
    day = datetime.datetime.now().weekday() if not day else int(day)
    dayname = DAYS[day]

    for restaurant in restaurants:
        restaurant.menu = restaurant.weekly_menu[day]

    return render_template(
        'index.html',
        restaurants=restaurants,
        dayname=dayname,
        day=day
    )
