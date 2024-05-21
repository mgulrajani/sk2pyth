from codetobetest import Survey
import pytest

@pytest.fixture
def survery():
    '''A survey object will be available for all the test functions'''
    question ="What language did you learn to code ?"
    survey =Survey(question)
    return survey



def test_store_single_response(survey):
    '''Test that response is stored properly.'''
    survey.store_response('Java')
    assert 'Java' in survey.responses



def test_store_multiple_responses(survey):
    '''Test that response is stored properly.'''
    
    responseslist = ['Java','C#','Python']

    for response in responseslist:
        survey.store_response(response)

    for response in responseslist:
        assert response in survey.responses


   



