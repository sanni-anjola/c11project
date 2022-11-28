def tell_me_more_about(a_language: str) -> str:
    languages = ("Java", "Python", "JavaScript")

    assert a_language in languages, f"Language '{a_language}' not found"

    return a_language


print(tell_me_more_about("Java"))
print(tell_me_more_about("Haskell"))
