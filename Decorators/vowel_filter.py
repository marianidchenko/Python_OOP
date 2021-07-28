def vowel_filter(function):
    def wrapper():
        letters = function()
        vowels = [x for x in letters if x.lower() in "aeiou"]
        return vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())
