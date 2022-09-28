from pdfminer.high_level import extract_text
import search

class data:

    def __init__(self,name,phone,email,skill,college,dob,city,language,linkin):
        self.name=name
        self.mob_no=phone
        self.email_id=email
        self.linkedIn=linkin
        self.Skills=skill
        self.Education=college
        self.dob=dob
        self.City=city
        self.Language=language
    
def main(path):
    txt=extract_text(path)
    obj=data(search.name(txt),search.phone(txt),search.email(txt),search.skills(txt),search.college(txt),search.dob(txt),search.location(txt),search.language(txt),search.linkedin(txt))
    return obj