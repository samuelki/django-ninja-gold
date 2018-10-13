from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0

    if 'activities_list' not in req.session:
        req.session['activities_list'] = []

    return render(req, 'ninja_gold/index.html')

def process_money(req):
    if req.method != 'POST':
        return redirect('/')

    building = req.POST['building']
    
    if building == 'farm':
        rand = random.randrange(10,21)
        req.session['gold'] += rand
        activity = {
            'content': "Earned " + str(rand) + " golds from the farm! (" + datetime.now().strftime("%Y/%m/%d %I:%M %p") + ")",
            'color': "green"
        }
    elif building == 'cave':
        rand = random.randrange(5,11)
        req.session['gold'] += rand
        activity = {
            'content': "Earned " + str(rand) + " golds from the cave! (" + datetime.now().strftime("%Y/%m/%d %I:%M %p") + ")",
            'color': "green"
        }
    elif building == 'house':
        rand = random.randrange(2,6)
        req.session['gold'] += rand
        activity = {
            'content': "Earned " + str(rand) + " golds from the house! (" + datetime.now().strftime("%Y/%m/%d %I:%M %p") + ")",
            'color': "green"
        }
    elif building == 'casino':
        if req.session['gold'] >= 50:
            rand = random.randrange(-50,51)
            req.session['gold'] += rand
            if rand < 0:
                activity = {
                    'content': "Entered a casino and lost " + str(abs(rand)) + " golds...Ouch! (" + datetime.now().strftime("%Y/%m/%d %I:%M %p") + ")",
                    'color': "red"
                }
            elif rand >= 0:
                activity = {
                    'content': "Earned " + str(rand) + " golds from the casino! (" + datetime.now().strftime("%Y/%m/%d %I:%M %p") + ")",
                    'color': "green"
                }
        else:
            activity = {
                'content': "Not enough golds to enter the casino! You must have at least 50. (" + datetime.now().strftime("%Y/%m/%d %I:%M %p") + ")",
                'color': "red"
            }
    
    req.session['activities_list'].insert(0, activity)
    req.session.modified = True

    return redirect('/')

def reset(req):
    if 'gold' in req.session:
        del req.session['gold']

    if 'activities_list' in req.session:
        del req.session['activities_list']

    return redirect('/')