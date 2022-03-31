
from flask import Flask, request, make_response
from flask import render_template
import database
from query import Query


app = Flask(__name__, template_folder='.')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    html = render_template('index.html', err_message="")
    response = make_response(html)
    return response


@app.route('/searchresults', methods=['GET'])
def search_form():
    dept = request.args.get('dept')
    num = request.args.get('num')
    area = request.args.get('area')
    title = request.args.get('title')

    if dept is None:
        dept = ""

    if num is None:
        num = ""

    if area is None:
        area = ""

    if title is None:
        title = ""

    query = Query(True, dept, num, area, title)
    error, courses = database.handle_all_courses(query)

    if error != "":
        html = render_template('error.html',
                           error=error)
    else:
        html = render_template('table.html',
                           courses=courses)

    response = make_response(html)
    return response

@app.route('/regdetails', methods=['GET'])
def search_results():

    classid = request.args.get('classid')
    if (classid is None) or (classid.strip() == ''):
        error_message = "missing classid"
        html = render_template('regdetails.html',
                               err_message=error_message)
    elif not classid.isdigit():
        error_message = "non-integer classid"
        html = render_template('regdetails.html',
                               err_message=error_message)
    else:
        query = Query(False, classid=classid)
        error, course = database.handle_specific_course(query)

        if error != "":
            html = render_template('regdetails.html',
                                   err_message=error)
        else:
            html = render_template('regdetails.html',
                                   depts=course.get_depts(),
                                   classid=classid,
                                   classes=course.get_classes(),
                                   courses=course.get_courses(),
                                   profs=course.get_profs(),
                                   err_message=error)

    response = make_response(html)
    return response
