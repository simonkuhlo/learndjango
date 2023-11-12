from . import models


def entry_to_dict(etnryid):
    object = models.Entry.objects.get(id=etnryid)
    answers = models.Answer.objects.filter(entry=etnryid)
    author = models.people.Person.objects.get(id=object.author.id)
    interview_dict = {}
    for answer in answers:
        question_model = models.Question.objects.get(id=answer.question.id)
        interview_dict.update({question_model.question_value : answer.answer_value})
    
    entry_dict = {
        "full_name" : f"{author.first_name} {author.last_name}",
        "about_me" : "TODO",
        "profile_picture" : "TODO",
        "interview" : interview_dict
    }
    return(entry_dict)