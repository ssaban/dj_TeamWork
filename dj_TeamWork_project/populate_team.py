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
    
    for x in range(0,999+1):
        member = add_Member(str(x) + "-first", str(x) +"-last")
        
        c_p= random_proficiancy()
        cpp_p= random_proficiancy()
        java_p= random_proficiancy()
        perl_p= random_proficiancy()
        python_p= random_proficiancy()
        ruby_p= random_proficiancy()
        git_p= random_proficiancy()
        svn_p= random_proficiancy()
        gradle_p= random_proficiancy()
        maven_p= random_proficiancy()
        jenkins_p= random_proficiancy()
        objective_c_p= random_proficiancy()
        android_p= random_proficiancy()
        DSP_p= random_proficiancy()
        mac_IOS_p= random_proficiancy()
        mySql_p= random_proficiancy()
        PHP_p= random_proficiancy()
        member_p = member
        
        add_Proficiency(c_p ,cpp_p, java_p, perl_p, python_p, ruby_p, git_p, svn_p, 
                gradle_p, maven_p, jenkins_p, objective_c_p, android_p, DSP_p, mac_IOS_p, 
                mySql_p, PHP_p, member_p)
        

def add_Member(first_name, last_name):
    m = Member.objects.get_or_create(first=first_name, last=last_name)[0]
    return m

def add_Proficiency(c_p ,cpp_p, java_p, perl_p, python_p, ruby_p, git_p, svn_p, 
    gradle_p, maven_p, jenkins_p, objective_c_p, android_p, DSP_p, mac_IOS_p, 
    mySql_p, PHP_p, member_p):
        
    p = Proficiency.objects.get_or_create(c=c_p ,cpp=cpp_p, java=java_p, 
                perl=perl_p, python=python_p, ruby=ruby_p, git=git_p, svn=svn_p, 
                gradle=gradle_p, maven=maven_p, jenkins=jenkins_p, 
                objective_c=objective_c_p, android=android_p, DSP=DSP_p, 
                mac_IOS=mac_IOS_p, mySql=mySql_p, PHP=PHP_p, member=member_p)[0]
    
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Team population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_TeamWork_project.settings')
    from team.models import Member, Proficiency
    populate()
