from datetime import datetime

from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs

import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def works_log():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


def make_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.name = name
    user.surname = surname
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    session.add(user)
    session.commit()


def make_job(team_leaderid, job, work_size, collaborators, start_date, is_finished):
    job_el = Jobs()
    job_el.team_leaderid = team_leaderid
    job_el.job = job
    job_el.work_size = work_size
    job_el.collaborators = collaborators
    job_el.start_date = start_date
    job_el.is_finished = is_finished
    session.add(job_el)
    session.commit()


def main():
    global session

    db_session.global_init("db/mars_db.sqlite")
    session = db_session.create_session()

    # for user in session.query("User").filter(User.address == 'module_1'):
    #     print(user)

    # make_user('Scott', 'Ridley', 21, 'captain', 'esearch engineer', 'module_1', 'scott_chief@mars.org')
    # make_user('Balabanov', 'Fedor', 16, 'starpom', "engeneer", 'module_1', 'bfm_2003@mail.ru')
    # make_user('surn1', 'name1', 22, 'pos1', 'spec1', 'address1', 'email@email.ru')
    # make_user('surn2', 'name2', 45, 'pos2', 'spec1', 'address2', 'email2@email.ru')
    # make_user('surn3', 'name3', 66, 'pos2', 'spec3', 'address3', 'email1@email.ru')
    # make_job(1, 'deployment of residential modules 1 and 2', 15, '2, 3', datetime.now(), False)
    # make_job(2, 'deployment of residential modules 1 and 2', 1, '4, 3', datetime.now(), False)

    app.run()


if __name__ == '__main__':
    main()
