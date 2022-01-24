import names, random, string


class RandomPersonData:
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    recruiter = "Olga Shakirova"
    roles_list = ["SDE", "SDET", "STE", "SRE", "Starter", "PM", "TPM"]
    role = random.choice(roles_list)
    office_list = ["Kazan", "Ivanovo", "Yaroslavl"]
    office = random.choice(office_list)
    country = "Russia"
    city = "Kazan"
    context_comment = "This bot was made by Rushat"
    english_level = "Advanced"
    english_comment = "Test comment"
    skill1 = "python"
    skill2 = "java"
    grade = "Middle"
    other_skill1 = "sql"
    want_relocate = "United States"
    contact_type = "Email"
    email = "".join(random.choices(string.ascii_lowercase, k=10)) + "@akvelon.com"


