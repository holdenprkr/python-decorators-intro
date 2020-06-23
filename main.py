def kids(sentence_func):
    def chore_complete(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"{original_sentence} by the kids"
    return chore_complete


def parents(sentence_func):
    def chore_complete(*args, **kwargs):
        original_sentence = sentence_func(*args, **kwargs)
        return f"{original_sentence} by the parents"
    return chore_complete


@kids
def laundry():
    return "The dirty laundry was cleaned"


@parents
def garbage():
    return "The garbage was taken out"


@kids
def dust():
    return "The house was dusted"


@parents
def groom():
    return "The dog was brushed"


print(laundry())
print(garbage())
print(dust())
print(groom())
