
rm -rf .coverage
coverage run --parallel-mode classes/tests/game_tests.py
coverage run --parallel-mode classes/tests/magic_tests.py
coverage run --parallel-mode classes/tests/inventory_tests.py
coverage combine
coverage report
coverage xml
