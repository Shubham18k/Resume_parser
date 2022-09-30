import search

class data:

    def __init__(self,name,phone,email,skill,college,dob,city,language,linkedin):
        self.name=name
        self.mob_no=phone
        self.email_id=email
        self.LinkedIn=linkedin
        self.Skills=skill
        self.Education=college
        self.dob=dob
        self.City=city
        self.Language=language
    
def main(txt):
    obj=data(search.name(txt),search.phone(txt),search.email(txt),search.skills(txt),search.college(txt),search.dob(txt),search.location(txt),search.language(txt),search.linkedin(txt))
    return obj