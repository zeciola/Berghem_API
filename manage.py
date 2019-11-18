import os
from tkinter.tix import Shell
from unittest import TestLoader, TextTestRunner

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import transactions
from app.main import model

app = create_app(os.getenv('BERGHEM_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=model)

@manager.command
def routes():
    result = app.url_map
    return result

@manager.command
def run():
    app.run()


@manager.command
def test():
    tests = TestLoader().discover('app/test', pattern='test*.py' or '*test.py')
    result = TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
