from app.auth import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
    print('logging in')