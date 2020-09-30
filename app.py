
from flask import Flask, Response, request, abort, send_from_directory, send_file, render_template
from flask_cors import cross_origin, CORS

from model.User import Base, User

from view.user_view import build_users_page

from globals import engine, Session

from config import port

app = Flask(__name__)
CORS(app)


@app.route('/users', methods=['GET'])
def users():
    session = Session()
    active_users = session.query(User).filter_by(status=True).all()
    result = build_users_page(active_users)
    session.close()
    return render_template('user.html', table=result)


@app.route('/users/by-login')
def user_by_login():
    user_login = request.args.get("login")
    if not user_login:
        abort(400, "Некорректный запрос!")

    session = Session()
    current_users = session.query(User).filter_by(login=user_login).all()
    result = build_users_page(current_users)
    session.close()

    return render_template('user.html', table=result)


@app.route('/users/by-id')
def user_by_id():
    user_id = request.args.get("id")
    if not user_id:
        abort(400, "Некорректный запрос!")

    session = Session()
    current_users = session.query(User).filter_by(id=user_id).all()
    result = build_users_page(current_users)
    session.close()

    return render_template('user.html', table=result)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(port=port)
