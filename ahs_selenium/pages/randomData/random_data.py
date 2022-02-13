import names
import random
import string


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
    email = "".join(random.choices(string.ascii_lowercase, k=4)) + "@akvelon.com"


class FixturesInternalPerson:
    # TODO use dict for randoming
    # first_names = ["Olga"]
    # last_names = ["Shakirova"]
    # first, last = random.choice(first_names), random.choice(last_names)

    first_name = "Olga"
    last_name = "Shakirova"


class RandomPositionData:
    name = "Position UI tesing n=" + str(random.randint(0, 10000))
    orig_loc = "United States"
    comment = "This position was made by Rushat for testing"
    skill = "python"

    primary_offices = ["Kazan", "Ivanovo", "Yaroslavl"]
    primary_office = random.choice(primary_offices)

    other_offices = ["Seattle", "Belgrade (Kazan)"]
    other_office = random.choice(other_offices)