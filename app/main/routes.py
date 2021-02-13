from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
listrooms=[]

@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    archivo = open("archivo.txt","a")
    a = "Usuario: " + str(form.name.data) + "  Sala: " + str(form.room.data) + " \n"
    archivo.write(str((a)))
    archivo.close()
    if form.validate_on_submit():
        if not (listrooms):
            listrooms.append(form.room.data)
        else:
            if(room_checker(form.room.data)):
                print("ya esta")
            else:
                listrooms.append(form.room.data)
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form,lista=listrooms)

def room_checker(dato):
    for a in listrooms:
        if(a==dato):
            return True
    return False

@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
