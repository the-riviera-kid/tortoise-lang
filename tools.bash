echo
echo ======================== PYTEST =======================
pytest
echo
echo ======================== BLACK =======================
black .
echo
echo ======================== PYLINT =======================
pylint *.py
echo