from queryprocessor import process_query

def test_knows_what_is_your_name():
	assert process_query("what is your name") == "Ajith Dharwar"

def test_is_case_insensitive():
	assert process_query("What is your NAME") == "Ajith Dharwar"

def test_returns_empty_string_if_cannot_process_query():
	assert process_query("xxxx") == ""
