import names, random, string


class RandomPersonData:
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    context_comment = "This bot was made by Rushat"
    english_comment = "Test comment"
    skill1 = "python"
    skill2 = "java"
    other_skill1 = "sql"
    want_relocate = "United States"
    email = "".join(random.choices(string.ascii_lowercase, k=10)) + "@akvelon.com"


