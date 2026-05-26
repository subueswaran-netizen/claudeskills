from flask import render_template, abort
from models import get_course, contact_info, courses

def index():
    return render_template('index.html', courses=courses, active_page='home')

def course(course_id):
    course_obj = get_course(course_id)
    if course_obj is None:
        abort(404)
    return render_template('course.html', course=course_obj, course_id=course_id, active_page='course')

def tutorials(course_id):
    course_obj = get_course(course_id)
    if course_obj is None:
        abort(404)
    return render_template('tutorials.html', course=course_obj, course_id=course_id)

def contact():
    return render_template('contact.html', contact=contact_info, active_page='contact')
