.PHONY: clean system-packages-debian system-packeges-arch python-packages python-packages-pipenv install-debian install-arch create-db tests run all-debian all-arch

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . -type f -name '.pytest_cache' -delete

system-packages-debian:
	sudo apt install python-pip -y

system-packeges-arch:
	sudo pacman -S python
	sudo pacman -S python-pip

python-packages:
	pip install -r requirements.txt

python-packages-pipenv:
	pipenv install Pipfile

install-debian: system-packages-debian python-packages

install-arch: system-packeges-arch python-packages

create-db:
	python manage.py db init
	python manage.py db migrate --message "Init db migration"
	python manage.py db upgrade

test:
	export BERGHEM_ENV=test
	python manage.py test

run:
	export BERGHEM_ENV=dev
	python manage.py run

all-debian: clean install-debian create-db tests run

all-arch: clean install-arch create-db tests run
