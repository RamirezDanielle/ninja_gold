from flask import Flask, request, render_template, redirect, session

import datetime
import random


app = Flask(__name__)
app.secret_key ="Hack the Planet!"


@app.route('/')
def index():
    if 'golds' and 'activities' and 'loss' not in session:
        session['golds'] = 0
        session['activities'] = []
        session['loss']=[]
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if 'farm' == request.form['ninja_gold']:
        golds = random.randint(10, 20)
        session['golds'] += golds
        print(golds)
        session['activities'].append(f"Earned {golds} golds from the farm!")
        print(session['activities'])
        return redirect('/')
    
    if 'cave' == request.form['ninja_gold']:
        golds = random.randint(5, 10)
        session['golds'] += golds
        session['activities'].append(f"Earned {golds} golds from the cave!")
        print(session['activities'])
        return redirect('/')
    
    if 'house' == request.form['ninja_gold']:
        golds = random.randint(2, 5)
        session['golds'] += golds
        session['activities'].append(f"Earned {golds} golds from the house!")
        print(session['activities'])
        return redirect('/')
    
    if 'casino' == request.form['ninja_gold']:
        golds = random.randint(-50, 50)
        session['golds'] += golds
        if golds > 0:
            session['activities'].append(f"Entered a casino and earned {golds} golds!" )
        else:
            session['loss'].append(f"Entered a casino and lost {golds} golds...OUCH!" )
        print(session['activities'])
        print(session['loss'])
        print(golds)
        return redirect('/')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)