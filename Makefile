all: build

install:
	pip install pyinstaller

build: install
	pyinstaller src/tetris.py
	ln -s dist/tetris/tetris tetris

clean:
	-rm -r build dist tetris.spec tetris

