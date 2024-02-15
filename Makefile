all: build

install:
	pip install -r requirements.txt

install-dev:
	pip install -r dev-requirements.txt

build: install
	pyinstaller --onefile src/__main__.py -n tetris
	ln -s dist/tetris tetris

clean:
	-rm -r build dist tetris.spec tetris

format:
	black src

test: install-dev
	python -m pytest
