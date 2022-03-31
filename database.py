
import argparse
from sqlite3 import connect
from contextlib import closing
from sys import argv, stderr
from classes import Class
from course import Course

DATABASE = 'file:reg.sqlite?mode=rw'
SQL_BASE_STRING = "SELECT classes.classid, crosslistings.courseid, "
SQL_BASE_STRING += "crosslistings.dept, crosslistings.coursenum, "
SQL_BASE_STRING += "courses.title, courses.area FROM classes, "
SQL_BASE_STRING += "courses, crosslistings "
SQL_BASE_STRING += "WHERE courses.courseid = crosslistings.courseid "
SQL_BASE_STRING += "AND classes.courseid = courses.courseid"

SQL_CLASSES_STR = "SELECT * FROM classes WHERE classid = ?"
SQL_COURSES_STR = "SELECT * FROM courses WHERE courseid = ?"
SQL_CROSSLIST_STR = "SELECT * FROM crosslistings WHERE courseid = ?"
SQL_COURSEPROF_STR = "SELECT * FROM coursesprofs WHERE courseid = ?"
SQL_PROFS_STR = "SELECT * FROM profs WHERE profid = ?"


def handle_all_courses(query):
    args = argparse.Namespace(
        d=query.dept, n=query.num, a=query.area, t=query.title)
    try:
        with connect(DATABASE, isolation_level=None, uri=True) as conn:
            with closing(conn.cursor()) as cursor:
                # Helper search function

                search_query(args, cursor)

                row = cursor.fetchone()
                list = []
                output = []
                while row is not None:
                    list.append(row)
                    row = cursor.fetchone()
                list.sort(key=lambda x: (x[2], x[3], x[0]))
                for line in list:
                    course = Course([line[0], line[2],
                                     line[3], line[5], line[4]])
                    output.append(course)

                return "", output
    except argparse.ArgumentTypeError as ex1:
        print(argv[0]+": "+str(ex1), file=stderr)
        return str(ex1), None

    except Exception as ex:
        print(argv[0]+": "+str(ex), file=stderr)
        return """A server error occurred.
                         Please contact the system 
                        administrator.""", None


# Does same thing as regdetails.py, except it returns a
# list of Classs objects for the course


def handle_specific_course(query):
    args = argparse.Namespace(classid=query.classid)
    try:
        with connect(DATABASE, isolation_level=None, uri=True) as conn:
            with closing(conn.cursor()) as cursor:

                # Querying classes table
                classes = query_classes(cursor,
                                        args)

                # Querying crosslistings table
                depts = query_crosslistings(cursor, classes)

                # Querying courses table
                courses_list = query_courses(cursor, classes)

                # Querying coursesprofs table
                profs = query_course_profs(cursor, classes)

                clas = Class(classes, depts, courses_list, profs)
                return "", clas
    except argparse.ArgumentTypeError as ex1:
        print(argv[0]+": "+str(ex1), file=stderr)
        return str(ex1), None
    except Exception as ex:
        print(argv[0]+": "+str(ex), file=stderr)
        return """A server error occurred.
                         Please contact the system 
                        administrator.""", None


def search_query(args, cursor):
    search = SQL_BASE_STRING
    search_args = []
    base_expr = True
    # if no arguments, don't change the base string
    if args.d is not None:  # Search by department
        search += " AND crosslistings.dept LIKE ? "
        placeholder = str(args.d).replace(
            '%', r'\%').replace('_', r'\_')
        search_args.append('%'+placeholder+'%')
        base_expr = False
    if args.n is not None:  # Search by course num
        search += " AND crosslistings.coursenum LIKE ? "
        placeholder = str(args.n).replace(
            '%', r'\%').replace('_', r'\_')
        search_args.append('%'+placeholder+'%')
        base_expr = False
    if args.a is not None:  # Search by area
        search += " AND courses.area LIKE ? "
        placeholder = str(args.a).replace(
            '%', r'\%').replace('_', r'\_')
        search_args.append('%'+placeholder+'%')
        base_expr = False
    if args.t is not None:  # search by title
        search += " AND courses.title LIKE ? "
        placeholder = str(args.t).replace(
            '%', r'\%').replace('_', r'\_')
        search_args.append('%'+placeholder+'%')
        base_expr = False

    if not base_expr:
        cursor.execute(search + "ESCAPE '\\'", search_args)
    else:
        cursor.execute(search, search_args)


def query_classes(cursor, args):
    # Querying classes table
    cursor.execute(SQL_CLASSES_STR, [args.classid])
    classes = cursor.fetchone()
    if classes is None:
        raise argparse.ArgumentTypeError(
            f'no class with classid {args.classid} exists')

    return classes


def query_crosslistings(cursor, classes):
    # Querying crosslistings table
    cursor.execute(SQL_CROSSLIST_STR, [classes[1]])
    course_cross = cursor.fetchone()
    list = []
    while course_cross is not None:
        list.append(course_cross)
        course_cross = cursor.fetchone()
    # Sort list of depts and nums
    list.sort(key=lambda x: (x[1], x[2]))

    return list


def query_courses(cursor, classes):
    # Querying courses table
    cursor.execute(SQL_COURSES_STR, [classes[1]])
    courses = cursor.fetchone()

    return courses


def query_course_profs(cursor, classes):
    # Querying coursesprofs table
    cursor.execute(SQL_COURSEPROF_STR, [classes[1]])
    prof_id = cursor.fetchone()
    list = []
    while prof_id is not None:
        list.append(prof_id)
        prof_id = cursor.fetchone()

    # Match every Professor id to Professor's name
    # using the profs table
    professors = []
    for id_num in list:
        cursor.execute(SQL_PROFS_STR, [id_num[1]])
        prof = cursor.fetchone()
        professors.append(prof[1])

    # Sort the professors list and print
    professors.sort()

    return professors
