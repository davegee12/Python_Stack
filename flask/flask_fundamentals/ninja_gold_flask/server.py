from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html', farm_gold = "farm_gold", cave_gold = "cave_gold", house_gold="house_gold", casino_gold="casino_gold")

def convert_time():
    time = datetime.datetime.now()
    month = str(time.month)
    day = str(time.day)
    year = str(time.year)
    hour = time.hour
    minutes = str(time.minute).zfill(2)
    ampm = ' am'
    if hour > 12:
        hour = (hour - 12)
        ampm = ' pm'
    time_stamp = ' (' + month + '/' + day + '/' + year + ',' + str(hour) + ':' + minutes + ampm + ') <br>'
    return time_stamp

def game_state():
    state = 'playing'
    if session['count'] <= 15 and session['gold'] >= 200:
        state = 'won'
    elif session['count'] > 15:
        state = 'lose'
    return state

@app.route('/gold', methods=['POST'])
def process_money():
    session['count'] += 1
    print(session['count'])
    time_stamp = convert_time()
    state = game_state()

    if state == 'playing':
        if (request.form['name'] == 'farm'):
            farm_gold = int(random.randint(10,20))
            print(farm_gold)
            session['gold'] += farm_gold
            session['activities'].insert(0, '<div class="green"> Earned ' +str(farm_gold)+ ' gold pieces from your farm!' +time_stamp +'</div>')

        elif (request.form['name'] == 'cave'):
            cave_gold = int(random.randint(5,10))
            print(cave_gold)
            session['gold'] += cave_gold
            session['activities'].insert(0, '<div class="green"> Earned ' +str(cave_gold)+ ' gold pieces from your cave!' +time_stamp +'</div>')

        elif (request.form['name'] == 'house'):
            house_gold = int(random.randint(2,5))
            print(house_gold)
            session['gold'] += house_gold
            session['activities'].insert(0, '<div class="green"> Earned ' +str(house_gold)+ ' gold pieces from your house!' +time_stamp +'</div>')
        elif (request.form['name'] == 'casino'):
            casino_gold = int(random.randint(0,50))
            print(casino_gold)
            give_take = random.randint(0,1)
            if give_take == 0:
                session['gold'] -= casino_gold
                session['activities'].insert(0, '<div class="green"> Earned ' +str(casino_gold)+ ' gold pieces at the casino!' +time_stamp +'</div>')
            elif give_take == 1:
                session['gold'] += casino_gold
                session['activities'].insert(0, '<div class="red"> Lost ' +str(casino_gold)+ ' gold pieces at the casino!' +time_stamp +'</div>')

    elif state == 'won':
        session['count'] = 0
        session['gold'] = 0
        session['activities'].clear()
        session['activities'].insert(0, '<div class="win"> You earned enough gold within 15 turns. YOU WIN! </div>')
    elif state == 'lose':
        session['count'] = 0
        session['gold'] = 0
        session['activities'].clear()
        session['activities'].insert(0, '<div class="lose"> You have not earned enough gold within 15 turns. YOU LOSE! </div>')
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)