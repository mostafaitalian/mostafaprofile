import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, get_user_model
from django.core import serializers

# Create your views here.

# @login_required()
def dashboard(request):
    user = get_user_model().objects.get(id=1)
    profile = user.profile
    # personal_skills = profile.personl_skills.all()
    # experiences = profile.experiences.all()
    # languages = profile.languages.all()
    # profile_json = serializers.serialize('json', profile.personal_skills.all(), use_natural_foreign_keys=True)
    # profile_obj_ser = json.loads(profile_json)
    return render(request, 'myprofile/dashboard.html', {'profile': profile})

