from . import models


def entry_to_dict(etnryid):
    object = models.Entry.objects.get(id=etnryid)
    answers = models.Answer.objects.filter(entry=etnryid)
    print(answers[0].entry)