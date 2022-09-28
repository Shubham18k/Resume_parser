from colorsys import ONE_THIRD
import re
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk import sent_tokenize
import datefinder
import locationtagger
from datetime import date

def name(txt):
    person=[]
    nltk_results = ne_chunk(pos_tag(word_tokenize(txt)))
    for nltk_result in nltk_results:
        if type(nltk_result) == Tree:
            name = ''
            for nltk_result_leaf in nltk_result.leaves():
                name += nltk_result_leaf[0] + ' '
            person.append(name)

    return person[0]

def phone(txt):
    PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9.\-\(\)]{8,}[0-9]')
    phone = re.findall(PHONE_REG,txt)
    if phone:
        number=''.join(phone[0])
        if txt.find(number)>=0 and len(number)<=16:
            return number
    return None

def email(txt):
    EMAIL_REG = re.compile(r'[a-zA-Z_0-9\.\-+]+@[a-z0-9\.\-+]+\.[a-z]+')
    email = re.findall(EMAIL_REG,txt)
    return set(email)

def linkedin(txt):
    p=[]
    line=txt.split('\n')
    for i in line:
        if 'linkedin' in i:
            p.append(i)
    if len(p)>0:
        return p
    else:
        return None
    

def skills(txt):
    S=['Machine Learning','IOT','Data Egineer','Automation','cloud computing','python','R language','Node js','SQL','Mongodb','React Js','Angular JS','Java','Javascript','MS word','MS excel','Express Js',]
    SKILLS_DB=[x.lower() for x in S]
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(txt)
    filtered_tokens = [w for w in word_tokens if w not in stop_words]
    filtered_tokens = [w for w in word_tokens if w.isalpha()]
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
    found_skills = set()
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
 
    return found_skills

'''
def skills(txt):
    S=[
    'Machine Learning','Data Egineer','Automation','cloud computing','python','R language','Node js','SQL','Mongodb','React Js','Angular JS','Java','Javascript','MS word','MS excel','Express Js',
    ]
    S=[x.lower() for x in S]
    content=txt.split('\n')
    list=[]
    for i in content:
        i=i.lower()
        for j in S:
            if j in i:
                list.append(j)
    l=set(list)
    return l
'''

def college(txt):
    RESERVED_WORDS = [
    'school',
    'college',
    'univers',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'Schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',
    ]
    RESERVED_WORDS=[m.capitalize() for m in RESERVED_WORDS]+[m.upper() for m in RESERVED_WORDS]+RESERVED_WORDS
    line=txt.split('\n')
    edu=[]
    for i in line:
        for j in RESERVED_WORDS:
            if j in i:
                edu.append(i)
    
    return edu

def dob(txt):
    dates = datefinder.find_dates(txt)
    today=date.today()
    for i in dates:
        diff=today.year - i.date().year
        if diff>=18 :
            return i.date()
    return None
    
        

def location(txt):
    place= locationtagger.find_locations(text = txt)
    cities=place.cities
    return cities[0]

def language(txt):
    lang=['English','Marathi','Telugu','Hindi','Malayalam','Kannada','Tamil','Spanish','French','Urdu','Bengalis','Punjabi','Gujarati']
    lang=[m.capitalize() for m in lang]+[m.lower() for m in lang]+lang
    line=txt.split('\n')
    lan=[]
    for i in line:
        for j in lang:
            if j in i:
                lan.append(i)
    
    if len(lan)>0:
        return set(lan)
    else:
        return None

    





               


