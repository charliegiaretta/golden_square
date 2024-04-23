from lib.string_builder import *

def test_string_builder_add():
    stringbuilder = StringBuilder()
    stringbuilder.add('Hello')
    assert stringbuilder.output() == "Hello"

def test_string_builder_size():
    stringbuilder = StringBuilder()
    stringbuilder.add('Hello')
    assert stringbuilder.size() == 5

def test_string_builder_strings_join():
    stringbuilder = StringBuilder()
    stringbuilder.add('Hello')
    stringbuilder.add(' ')
    stringbuilder.add('World')
    assert stringbuilder.output() == "Hello World"

def test_string_builder_strings_join_total_size():
    stringbuilder = StringBuilder()
    stringbuilder.add('Hello')
    stringbuilder.add(' ')
    stringbuilder.add('World')
    assert stringbuilder.size() == 11