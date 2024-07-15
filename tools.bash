echo
echo ======================== PYTEST =======================
pytest
echo
echo ======================== BLACK =======================
black .
echo
echo ======================== PYLINT =======================
pylint tortoise.py tortoise_interpreter.py
echo