from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_subject
import pytest

def test_get_determiner():

    # Singular test
    single_determiners = ["a", "one", "the"]
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners

    #Plural
    plural_determiners = ["some", "many", "the"]
    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners

def test_get_noun():
    # singular nouns
    singular_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(10):
        noun = get_noun(1)
        assert noun in singular_nouns
    
    # Plural nouns
    plural_nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    for _ in range(10):
        noun = get_noun(3)
        assert noun in plural_nouns

def test_get_verb():
    # Past verbs
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(15):
        verb = get_verb(1,"Past")
        assert verb in past_verbs
    
    # Singular present verbs
    singular_present_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(15):
        verb = get_verb(1, "Present")
        assert verb in singular_present_verbs

    # Plural present verbs
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(15):
        verb = get_verb(5, "Present")
        assert verb in plural_present_verbs

    # Future verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(15):
        verb = get_verb(6, "Future")
        assert verb in future_verbs

def test_get_preposition():
    
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(25):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    # Local list
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]


    """ ### Test the singular phrases ### """
    # Test the number of returned words
    singular_phrase = get_prepositional_phrase(1).split(" ")
    assert len(singular_phrase) == 3

    # Lists for the singular phrases
    singular_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    single_determiners = ["a", "one", "the"]

    assert singular_phrase[0] in prepositions
    assert singular_phrase[1] in single_determiners
    assert singular_phrase[2] in singular_nouns



    """ ### Test the plural phrases ### """
    # Test the number of returned words
    plural_phrase = get_prepositional_phrase(2).split(" ")
    assert len(plural_phrase) == 3

    # Lists for plural phrases
    plural_nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    plural_determiners = ["some", "many", "the"]

    assert plural_phrase[0] in prepositions
    assert plural_phrase[1] in plural_determiners
    assert plural_phrase[2] in plural_nouns


""" Exceeds requirements """
def test_get_subject():
    singular_subject = get_subject(1).split()
    plural_subject = get_subject(2).split()

    assert len(singular_subject) == 2
    assert len(singular_subject) != 1
    assert len(plural_subject) != 1
    assert len(plural_subject) != 4

    # Confirm if it is returning plurals
    plural_nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    plural_determiners = ["some", "many", "the"]

    assert plural_subject[0].lower() in plural_determiners
    assert plural_subject[1].lower() in plural_nouns

    # # Confirm if it is returning plurals
    singular_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    single_determiners = ["a", "one", "the"]

    assert singular_subject[0].lower() in single_determiners
    assert singular_subject[1].lower() in singular_nouns


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
