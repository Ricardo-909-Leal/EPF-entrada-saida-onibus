lint:
	pylint --disable=all --enable=trailing-whitespace,line-too-long,missing-final-newline .

run:
	python main.py

install-requirements:
	pip3 install -r requirements.txt
