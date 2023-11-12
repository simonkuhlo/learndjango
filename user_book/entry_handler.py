from . import models


def entry_to_dict(etnryid):
    object = models.Entry.objects.get(id=etnryid)
    answers = models.Answer.objects.filter(entry=etnryid)
    interview_dict = {}
    for answer in answers:
        question_model = models.Question.objects.get(id=answer.question)
        interview_dict.update({question_model.question_value : answer.answer_value})
    
    entry_dict = {
        "about_me" : "TODO",
        "profile_picture" : "TODO",
        "interview" : interview_dict
    }
    print(entry_dict)