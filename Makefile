.PHONY: build dump init test lint clean

build:
	python tools/scripts/build.py --src src/configuration --out out/cf

dump:
	python tools/scripts/dump.py --ib ./ib --out src/configuration

init:
	python tools/scripts/init.py

test:
	python tools/scripts/run_tests.py

lint:
	bsl-language-server analyze --src src

clean:
	rm -rf out
	rm -rf ib
