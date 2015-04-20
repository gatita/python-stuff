#!/usr/bin/env python

import re, sys

DONOR_LIST = {}

def initial_input():
    choice_select = {
    'Send a Thank You': send_thankyou,
    'Create a Report': create_report
    }

    choice = raw_input('Send a Thank You? or Create a Report?\n')
    if choice == 'exit':
        sys.exit()
    choice_select[choice]()


def send_thankyou():
    name = raw_input('Provide full name of donor. Enter "Main Menu" at any point to start over. Enter "List" to view the list of donors.\n')
    if name == 'Main Menu':
        initial_input()

    if name == 'List':
        for name in DONOR_LIST.keys():
            print name
        name = raw_input('Choose a donor name.\n')
        if name == 'Main Menu':
            initial_input()

    if name not in DONOR_LIST:
        DONOR_LIST[name] = []

    pattern = re.compile('\d+(\.\d+)?')
    donation = raw_input('Donation amount?\n')

    if donation == 'Main Menu':
        initial_input()

    while pattern.match(donation) == None:
        print "Please provide a number for donation amount.\n"
        donation = raw_input('Donation amount?\n')
        if donation == 'Main Menu':
            initial_input()

    DONOR_LIST[name].append(int(donation))

    my_donor = {'name': name, 'donation': donation}

    email = "Dear {name},\n Thank you for your generous donation of {donation}!".format(**my_donor)
    print email

    initial_input()


def create_report():
    report = {}
    for key in DONOR_LIST.keys():
        report[key] = [sum(DONOR_LIST[key]), len(DONOR_LIST[key]), sum(DONOR_LIST[key]) / len(DONOR_LIST[key])]

    # sorted_report = sorted(report)

    for key, value in sorted(report.iteritems()):
        total, count, avg = value
        print "{:<10} {:<10} {:<10} {:<10}".format(key, total, count, avg)

    initial_input()


initial_input()