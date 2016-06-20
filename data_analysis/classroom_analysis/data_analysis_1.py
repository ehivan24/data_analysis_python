import unicodecsv as csv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def parse_date(date):
    if date =='':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')


def parse_int(i):
    if i == '':
        return None
    else:
        return int(i)


def parse_int_from_float(i):
    if i =='':
        return None
    else:
        return int(float(i))


def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)


def round_minutes(mins):
    if mins=='':
        return None
    else:
        return round(float(mins))


def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students


def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data


def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data


def described_data(data):
    print "Mean: ", np.mean(data)
    print "Standard Deviation: ", np.std(data)
    print "Maximum: ", np.max(data)
    print "Minimum: ", np.min(data)
    plt.hist(data)


def run_plt(data):
    plt.hist(data, bins=8)
    plt.xlabel("Number of Days: ")
    plt.title("Data Analysis ")
    plt.ylabel("Number of students")
    plt.show()


print ""
print ""
enrollments = read_csv('enrollments.csv')
#print enrollments[0]

daily_engagements = read_csv('daily_engagement.csv')
#print daily_engagements[0]

project_submissions = read_csv('project_submissions.csv')
print project_submissions[0]

for enrollment in enrollments:
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    enrollment['cancel_date'] = parse_date( enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_int(enrollment['days_to_cancel'])
    enrollment['account_key'] = parse_int(enrollment['account_key'])
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'

#print "Enrollments: ", enrollments[0]
print "Enrolled Students ", len(enrollments)


for daily_engagement in daily_engagements:
    daily_engagement['lessons_completed'] = parse_int_from_float(daily_engagement['lessons_completed'])
    daily_engagement['num_courses_visited'] = parse_int_from_float(daily_engagement['num_courses_visited'])
    daily_engagement['total_minutes_visited'] = round_minutes(daily_engagement['total_minutes_visited'])
    daily_engagement['projects_completed'] = parse_int_from_float(daily_engagement['projects_completed'])
    daily_engagement['acct'] = parse_int(daily_engagement['acct'])
    daily_engagement['utc_date'] = parse_date(daily_engagement['utc_date'])

#print "Daily engagements: ", daily_engagements[0]
print "Daily engagements: ", len(daily_engagements)

for project_submission in project_submissions:
    project_submission['lesson_key'] = parse_int(project_submission['lesson_key'])
    project_submission['account_key'] = parse_int(project_submission['account_key'])
    project_submission['creation_date'] = parse_date(project_submission['creation_date'])
    project_submission['completion_date'] = parse_date(project_submission['completion_date'])

#print "Project Submissions: ", project_submissions[0]
print "Project Submissions: ", len(project_submissions)

print ""
unique_enrolled_student = set()
for enrollment in enrollments:
    unique_enrolled_student.add(enrollment['account_key'])

print "Unique Enrolled Students: ", len(unique_enrolled_student)

unique_daily_engagement = set()
for daily_engagement in daily_engagements:
    unique_daily_engagement.add(daily_engagement['acct'])

print "Unique Daily Engagement: ", len(unique_daily_engagement)

unique_project_submission = set()
for project_submission in project_submissions:
    unique_project_submission.add(project_submission['account_key'])

print "Unique Project Submissions: ", len(unique_project_submission)


for engagement_record in daily_engagements:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

print "Unique Daily Engagement After Cleaning them Up: ", len(daily_engagements)

get_unique_students_enrollments = get_unique_students(enrollments)
get_unique_students_daily_engagement = get_unique_students(daily_engagements)
get_unique_students_project_submission = get_unique_students(project_submissions)

print ""
print "Unique Students Enrollments: ", len(get_unique_students_enrollments)
print "Unique Daily Engagements: ", len(get_unique_students_daily_engagement)
print "Unique Project Submissions: ", len(get_unique_students_project_submission)

print ""


for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_daily_engagement:
        print "Student: ", student
        break


student_num_of_problems = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_daily_engagement and enrollment['join_date'] != enrollment['cancel_date']:
        student_num_of_problems += 1
        #if not enrollment['is_udacity']:
         #   print enrollment

print "Student: ", (student_num_of_problems)

#
# how many students have canceled
#
students_canceled = list()
for enrollment in enrollments:
    if enrollment['is_canceled']:
        students_canceled.append(enrollment['account_key'])


print "Students Canceled: ", len(students_canceled)
print "Students who not canceled: ", len(unique_enrolled_student) - len(students_canceled)


students_less_than_one_week_to_cancel = 0
for enrollment in enrollments:
    if enrollment['days_to_cancel'] < 7:
        students_less_than_one_week_to_cancel += 1

print ""
print "Students less than a week to cancel: ", students_less_than_one_week_to_cancel


udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])

print "Udacity Test account: ", len(udacity_test_accounts)


def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data


unique_set_none_udacity_enrollments = remove_udacity_accounts(enrollments)
unique_set_none_udacity_daily_engagement = remove_udacity_accounts(daily_engagements)
unique_set_none_udacity_project_submissions = remove_udacity_accounts(project_submissions)


print len(enrollments), "  ",         "Not Uacity test accounts: ", len(unique_set_none_udacity_enrollments)
print len(project_submissions), "  ", "Not Uacity test accounts: ", len(unique_set_none_udacity_project_submissions)
print len(daily_engagements), "  ",   "Not Uacity test accounts: ", len(unique_set_none_udacity_daily_engagement)


#
#
#
paid_students = {}
for enrollment in unique_set_none_udacity_enrollments:
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:

        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']

        if account_key not in paid_students or enrollment_date > paid_students[account_key]:
            paid_students[account_key] = enrollment_date


print "Paid Students: ", len(paid_students)


def with_one_week(join_date, engagement_date):
    time_delta = join_date - engagement_date
    return time_delta.days < 7 and  time_delta.days >= 0


def remove_free_trials_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)

    return new_data


paid_enrollments = remove_free_trials_cancels(unique_set_none_udacity_enrollments)
paid_daily_engagements = remove_free_trials_cancels(unique_set_none_udacity_daily_engagement)
paid_project_submissions = remove_free_trials_cancels(unique_set_none_udacity_project_submissions)

print "Paid Enrollments ", len(paid_enrollments)
print "Paid Daily Engagements", len(paid_daily_engagements)
print "Paid Project ", len(paid_project_submissions)

paid_engagement_in_first_week = []
for engagement_record in paid_daily_engagements:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if with_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print "Paid Engagement in first Week: ", len(paid_engagement_in_first_week)


engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)

print "Engagement By Account: ", len(engagement_by_account)

total_minutes_by_account = {}

for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes

total_minutes = total_minutes_by_account.values()
print ""
described_data(total_minutes_by_account.values())

student_with_maximum_minutes = None
max_minutes = 0

for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_maximum_minutes = student

print "Maximum Mins: ", max_minutes

day_number = 0
for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] == student_with_maximum_minutes:
        day_number += 1
        print day_number, " ", engagement_record

print ""
number_lessons_completed = 0
number_lessons_not_completed = 0
for engagement_record in unique_set_none_udacity_daily_engagement:
    #student_account = engagement_record['account_key']
    if engagement_record['lessons_completed']:
        number_lessons_completed += 1
    else:
        number_lessons_not_completed += 1

print "Lessons Not Completed: ", number_lessons_not_completed
print "Lessons Completed ", number_lessons_completed

print ""

total_minutes_by_account = sum_grouped_items(engagement_by_account, 'total_minutes_visited')
described_data(total_minutes_by_account.values())
print ""
number_lessons_completed_by_account = sum_grouped_items(engagement_by_account, 'lessons_completed')
described_data(number_lessons_completed_by_account.values())

print ""

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['num_courses_visited'] > 0:
        engagement_record['has_visited'] = 1
    else:
        engagement_record['has_visited'] = 0


number_of_courses_visited = sum_grouped_items(engagement_by_account, 'has_visited')
described_data(number_of_courses_visited.values())

print ""

subway_project_lesson_key = [746169184, 3176718735]

pass_subway_project = set()
for submission in paid_project_submissions:
    project = submission['lesson_key']
    rating = submission['assigned_rating']

    if project in subway_project_lesson_key and (rating == 'PASSED' or rating == 'DISTINCTION'):
        pass_subway_project.add(submission['account_key'])

print "Students who Passed the project: ", len(pass_subway_project)


passing_engagement = []
non_passing_engagement = []

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print ""
print "Passed: ", len(passing_engagement)
print "Not passed: ", len(non_passing_engagement)

passing_engagement_by_account = group_data(passing_engagement, 'account_key')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')

print ""
print "Not passing students: "
non_passing_minutes = sum_grouped_items(non_passing_engagement_by_account, 'total_minutes_visited')
described_data(non_passing_minutes.values())
print ""
print "Passing Students: "
passing_minutes = sum_grouped_items(passing_engagement_by_account, 'total_minutes_visited')
described_data(passing_minutes.values())

print ""
print "Lessons Completed Passing Students: "
passing_lessons = sum_grouped_items(passing_engagement_by_account, 'lessons_completed')
described_data(passing_lessons.values())
print ""
print "Lessons Completed Non Passing Students: "
non_passing_lessons = sum_grouped_items(non_passing_engagement_by_account, 'lessons_completed')
described_data(non_passing_lessons.values())
print ""
print "Passing Students visits: "
visit_students_lessons = sum_grouped_items(passing_engagement_by_account, 'has_visited')
described_data(visit_students_lessons.values())
print ""
print "Non-Passing Students visits: "
non_visit_students_lessons = sum_grouped_items(non_passing_engagement_by_account, 'has_visited')
described_data(non_visit_students_lessons.values())

run_plt(non_visit_students_lessons.values())