from codetobetest import Survey

question = "what language did you first learn to code ?"
language_survey  =Survey(question)

#show the quest and store the responses

language_survey.show_question()
print('Enter  q to quit \n')

while True:
    response = input("Language ")
    if response == 'q':
        break
    language_survey.store_response(response)

print('\n Thank you for participating in the survey')
language_survey.show_results()


