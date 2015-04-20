#!/usr/bin/env python

import re
# name: [total donated, number of donations, avg donation amt]
DONOR_LIST = {}

def initial_input():
    choice_select = {
    'Send a Thank You': send_thankyou,
    'Create a Report': create_report
    }

    choice = raw_input('Send a Thank You? or Create a Report?\n')
    choice_select[choice]()

def send_thankyou():
    name = raw_input('Provide full name of donor.\n')
    if name == 'list':
        for name in DONOR_LIST.keys():
            print name
        name = raw_input('Choose a donor name.\n')

    if name not in DONOR_LIST:
        DONOR_LIST[name] = []

    pattern = re.compile('\d+(\.\d+)?')
    donation = raw_input('Donation amount?\n')

    while pattern.match(donation) == None:
        print "Please provide a number for donation amount.\n"
        donation = raw_input('Donation amount?\n')

    DONOR_LIST[name].append(int(donation))

    my_donor = {'name': name, 'donation': donation}

    email = "Dear {name},\n Thank you for your generous donation of {donation}!".format(**my_donor)
    print email

    initial_input()


def create_report():
    report = {}
    for key in DONOR_LIST.keys():
        report[key] = [sum(DONOR_LIST[key]), len(DONOR_LIST[key]), sum(DONOR_LIST[key]) / len(DONOR_LIST[key])]

    for key, value in report.iteritems():
        total, count, avg = value
        print "{:<10} {:<10} {:<10} {:<10}".format(key, total, count, avg)

    initial_input()


initial_input()