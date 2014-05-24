from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render_to_response

from team.models import Member, Proficiency
from team.forms import UserForm, UserProfileForm



def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('team/index.html', context_dict, context)

#def index(request):
#    return HttpResponse("Team says: Hello world! <a href='/team/about'>About</a>")
 

def about(request):
    context = RequestContext(request)
    
    context_dict = {'boldmessage': "I am bold font from the context for about page"}
    
    
    
    #return HttpResponse("Team says:Here is the about page. <a href='/team/'>Index</a>")

    #prepare an empty dictionary of proficiency from DB
    #dynamicaly extract name of proficiency from DB
    team_proficiency_dictionary = {}
    for f in Proficiency._meta.fields:
        field = f.get_attname_column()[0]
        if (field != "id") and (field != "member_id"):
            team_proficiency_dictionary[field] = {}
            for proficiency_level in (4,3,2,1,0):
                team_proficiency_dictionary[field][str(proficiency_level)]=0 
            
            
    #generate data for heatmap e.g. entry count for each proficiancy and level
    for e in Proficiency.objects.all():
        for proficiency in team_proficiency_dictionary:
            proficiency_level =  eval("e."+ proficiency)
            team_proficiency_dictionary[proficiency][str(proficiency_level)] +=1
    
    test_str = "DATA EXTRACTED\n"
    with open ('myfile', 'a') as f:
        
    #print header of heatmap
    
        f.write ('Guru,Expert,Intermediate,Novice,NA\n')
        test_str += 'Guru,Expert,Intermediate,Novice,NA\n'
        for p in team_proficiency_dictionary:
            proficiency_str = p
            for level in (4,3,2,1,0):
                proficiency_str += "," + str(team_proficiency_dictionary[p][str(level)])
            f.write(proficiency_str + "\n")
            test_str +=proficiency_str + "\n"
            
    context_dict = {'test_data':test_str}
    
    return render_to_response('team/about.html', context_dict, context)
            
            
            

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'team/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
            
            


