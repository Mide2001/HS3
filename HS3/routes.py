from HS3 import app, db
from flask import render_template, jsonify,json, request, make_response, flash
from HS3.models import Survey
from HS3.forms import SubmitForm,SiteForm, EditForm, Surveyform, Model2form
import requests
import pdfkit
#import weasyprint

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')


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
    form = Surveyform()
    #pdfkit.from_url("http://127.0.0.1:5000/survey ", "output1.pdf", configuration=config)

    #if request.method == 'GET' and form.validate_on_submit():
    #pdfkit.from_file("C:/Users/abdul/PycharmProjects/HS3 Deployment/HS3/templates/survey.html", 'Test3.pdf', configuration=config)

    if request.method == 'POST' and request.form["site"]:

        data = Survey.query.get_or_404(request.form["site"])

        survey = Survey.query.all()

        if request.files:
            file = request.files["video"]
            print(file)
            print(request.form['email'])
            myobj = {'video':file,'email': request.form['email']}
            head = {"Content-Type":"multipart/form-data"}
            vid = requests.post("http://project-hs3.eu-west-2.elasticbeanstalk.com/video_uploaded" ,headers =head ,data = myobj)
            print(vid.status_code)
            print(vid.content)
            ##api_data = requests.post("http://127.0.0.1:5000//test")
            ##api_data = json.loads(api_data.text)
            #print('This is the data:')
            #print(api_data)
            #for data in api_data['defect_detection']:
                #print(data)

        else:
            print('No file')


        #response = make_response(pdf)
        #response.headers['Content-Type'] = 'application/pdf'
        #return response
        #response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
        #res = render_template('survey.html', survey=survey,api_data=api_data['defect_detection'],data=data,form=form)
        #pdfkit.from_url('http://127.0.0.1:5000/survey', 'Test7.pdf', configuration=config)
        #pdfkit.from_string(res, 'Test5.pdf', configuration=config)

        return render_template('upload.html', status= vid.status_code)
        ##return render_template('survey.html', survey=survey,api_data=api_data['defect_detection'],data=data,form=form)
            #print("Get request sent")
            # print(request)
    #if form.validate_on_submit():
        #pdfkit.from_file("C:/Users/abdul/PycharmProjects/HS3 Deployment/HS3/templates/survey.html", 'Test.pdf',configuration=config)

    else:
        print("Here")
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

@app.route("/model2", methods=['GET', 'POST'])
def model2_page():
    form = Model2form()
    if 'show' in request.form:
        print('Show toggle ')
        #return render_template('model2.html', form=form,show=True )
    if 'submit' in request.form:
        #print("This is the tmax")
        #print(request.form["tmax"])
        myobj = {'wind_direction': request.form['wind_direction'], 'pipe_size': request.form['pipe_size'],
                 'total_sewer_length': request.form['total_sewer_length'],
                 'flow_current_travel_time': request.form['flow_current_travel_time'],
                 'population': request.form['population'], 'FreeFlowSpeed': request.form['free_flow_speed'],
                 'CurrentFreeFlowSpeed': request.form['current_free_flow_speed'],
                 'CurrentTravelTime': request.form['current_travel_time'],
                 'FreeFlowTravelTime': request.form['free_flow_travel_time'],
                 'Confidence': request.form['confidence'],
                 'Insp_Length': request.form['insp_length'], 'tavg': request.form['tavg'],
                 'tim': request.form['tim'], 'tmax': request.form['tmax'],
                 'prcp': request.form['prcp'], 'snow': request.form['snow'], 'wspd': request.form['wspd'],
                 'pres': request.form['pres']}

        predict_data = requests.post("https://2920-82-15-80-198.ngrok.io/predict_defect",data = myobj)
        #print(request.form)
        data = predict_data.text
        print('This is the data:')
        print(data)
        #return render_template('model2result.html',data=data )
        return render_template('model2.html', data=data,form=form)


    return render_template('model2.html', form=form,show=False )

def read_data():
    f = open('HS3/static/data.json')

    data = json.load(f)

    f.close()
    return data

@app.route("/test", methods=['GET', 'POST'])
def mockapi():
    return read_data()