# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="sarel"
__date__ ="$May 20, 2014 10:30:24 PM$"

import os
from random import randint

def random_proficiancy():
    return randint(0,4)

def populate():
    
    for x in range(1,1000):
        member = add_Member(str(x) + "-first", str(x) +"-last")
        p_c = random_proficiancy()
        p_cpp = random_proficiancy()
        p_java = random_proficiancy()
        p_perl = random_proficiancy()
        p_python = random_proficiancy()
        p_ruby = random_proficiancy()
        p_git = random_proficiancy()
        p_member = member
        add_Proficiency(p_c, p_cpp, p_java, p_perl, p_python, p_ruby, p_git, p_member)
        

def add_Member(first_name, last_name):
    m = Member.objects.get_or_create(first=first_name, last=last_name)[0]
    return m

def add_Proficiency(p_c, p_cpp, p_java, p_perl, p_python, p_ruby, p_git, p_member):
    
    p = Proficiency.objects.get_or_create(
                                    c=p_c, cpp=p_cpp, java=p_java, perl=p_perl,
                                    python=p_python, ruby=p_ruby, git=p_git, 
                                    member=p_member)[0]
    
    
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Team population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_TeamWork_project.settings')
    from team.models import Member, Proficiency
    populate()
