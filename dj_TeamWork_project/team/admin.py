# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="sarel"
__date__ ="$May 18, 2014 6:15:49 PM$"

if __name__ == "__main__":
    print "Hello World"
    
from django.contrib import admin
from team.models import Member, Proficiency, UserProfile


admin.site.register(Member)
admin.site.register(Proficiency)

admin.site.register(UserProfile)

