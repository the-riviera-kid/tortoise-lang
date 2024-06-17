from tortoise import main, get_tortoise_file, get_file_content

VALID_ARGS = ['tiny.tortoise', 'medium.tortoise', 'large.tortoise']

def test_main_is_found():
    assert main

def test_get_tortoise_file_valid_args():
    test_data = ['tortoise.py', 'tiny.tortoise']
    assert get_tortoise_file(test_data, VALID_ARGS) == 'tiny.tortoise'

def test_get_tortoise_file_no_argument():
    test_data = ['tortoise.py']
    assert get_tortoise_file(test_data, VALID_ARGS) == '\nPlease specify an argument on the command line\n'

def test_get_tortoise_file_no_valid_argument():
    test_date = ['tortoise.py', 'big.tortoise']
    assert get_tortoise_file(test_date, VALID_ARGS) == "\nThat's not an existing tortoise file\n"

def test_get_file_content():
    assert get_file_content('tiny.tortoise') == ['1. P 3', '2. U', '3. D']

def test_get_file_content_again():
    assert get_file_content('medium.tortoise') == ['1. P 3', '2. D', '3. E 2', '4. U']
