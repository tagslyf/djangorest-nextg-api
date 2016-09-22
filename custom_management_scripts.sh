#!/bin/bash
# My example bash script
python manage.py predefined_au_states # To fill up the 6 AU states in the db
python manage.py sample_units # To fill up sample units in the db for testing
python manage.py predefined_user_types # To fill up the 3 User Types of NextG
python manage.py sample_user_accounts # To fill up a sample user account in the db for testing
python manage.py sample_user_accounts_courses # To fill up a sample user with course in the db for testing
python manage.py sample_user_accounts_units # To fill up a sample user with units in the db for testing