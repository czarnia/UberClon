cd ./test
python3 -m unittest TestHelloWorld
py.test TestHelloWorld.py --doctest-modules --pep8 coveralls -v --cov coveralls --cov-report term-missing
