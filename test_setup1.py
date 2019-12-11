import pytest
from crunch import name, language, math_function

def test_setup1():
	assert name == 'Paul C. Nnaoji'
	assert language == 'Python'

def test_math():
	math = math_function()
	assert math is 18


 


	