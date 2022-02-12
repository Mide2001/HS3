from HS3 import app, db
from flask import render_template, jsonify,json, request, make_response, flash
from HS3.models import Survey
from HS3.forms import SubmitForm,SiteForm, EditForm
import requests


@app.route("/", methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    form_data = SubmitForm()

    if form_data.validate_on_submit():
        print("working")
    if form_data.errors != {}:
        for err_msg in form_data.errors.values():
            print(f'There was an error with creating a user: {err_msg}')

    return render_template('home.html',form_data=form_data )

@app.route("/survey", methods=['GET', 'POST'])
def survey_page():
    if request.method == 'POST':

        data = Survey.query.get_or_404(request.form["site"])

        survey = Survey.query.all()
        if request.files:
            file = request.files["video"]
            print(file)
            #api_data = requests.post("http://127.0.0.1:5000//test")
            api_data = requests.post("https://739e-82-15-80-198.ngrok.io/defect", files={"video":file})
            print('This is the data:')
            print(api_data)
            api_data = json.loads(api_data.text)
            print('This is the data:')
            print(api_data)
            #for data in api_data['defect_detection']:
                #print(data)

        else:
            print('No file')
        return render_template('survey.html', survey=survey,api_data=api_data['defect_detection'],data=data)
    else:
        form_data = SubmitForm()
        return render_template('home.html',form_data=form_data )

@app.route("/site", methods=['GET', 'POST'])
def site_page():

    form = SiteForm()

    if form.validate_on_submit():

        new_data = Survey(name=form.name.data, site=form.site.data, date=form.date.data, road=form.road.data,
                          town=form.town.data, county=form.county.data, phone=form.phone.data, email=form.email.data,
                          pipe_use=form.pipe_use.data, year_laid=form.year_laid.data, pipe_length=form.pipe_length.data,
                          pipe_shape=form.pipe_shape.data, pipe_size=form.pipe_size.data,
                          pipe_material=form.pipe_material.data)
        db.session.add(new_data)
        db.session.commit()
        print('Data Added')
        form_data = SubmitForm()
        return render_template('home.html',form_data=form_data)

    if form.errors != {}:
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')

    return render_template('site.html', form=form)

@app.route("/edit", methods=['GET', 'POST'])
def edit_page():
    form = EditForm()

    if 'submit_delete' in request.form:
        print("Deleted")
        print(request.form["site_select"])
        Survey.query.filter_by(id=request.form["site_select"]).delete()
        db.session.commit()
        return render_template('edit.html', form=form)

    if 'submit_update' in request.form:
        data = Survey.query.filter_by(id=request.form["site_select"]).first()
        #print(data.name)
        return render_template('edit.html', form=form, data=data, show=True)
    if 'submit_commit' in request.form:
        new_data=Survey.query.get_or_404(request.form["site_select"])
        new_data.name = form.name.data
        new_data.site = form.site.data
        new_data.date = form.date.data
        new_data.road = form.road.data
        new_data.town = form.town.data
        new_data.county = form.county.data
        new_data.phone = form.phone.data
        new_data.email = form.email.data
        new_data.pipe_use = form.pipe_use.data
        new_data.year_laid = form.year_laid.data
        new_data.pipe_length = form.pipe_length.data
        new_data.pipe_shape = form.pipe_shape.data
        new_data.pipe_size = form.pipe_size.data
        new_data.pipe_material = form.pipe_material.data

        print(form.name.data)
        db.session.commit()


    return render_template('edit.html', form=form )



def read_data():
    f = open('HS3/static/data.json')

    data = json.load(f)

    f.close()
    return data

@app.route("/test", methods=['GET', 'POST'])
def mockapi():
    return read_data()