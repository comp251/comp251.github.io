#!/usr/bin/env python3

import datetime
import argparse
import re


def parse_date(s):
    try:
        return datetime.datetime.strptime(s, '%m-%d-%Y')
    except ValueError:
        raise argparse.ArgumentTypeError('Invalid date: {}'.format(s))


def format_date(fmt_str, date):
    out = fmt_str
    out = re.sub(r'<MONTH>', str(date.month), out)
    out = re.sub(r'<DAY>', str(date.day), out)
    out = re.sub(r'<YEAR>', str(date.year), out)
    out = re.sub(r'<DAY_NAME>', date.strftime('%A'), out)
    out = re.sub(r'<MONTH_NAME>', date.strftime('%B'), out)
    out = re.sub(r'<BR>', '\n', out)
    return out


def generate(args):
    start_date = args.start
    end_date = args.end
    cur_d = args.start
    week = 0
    start_day = cur_d.weekday()

    offsets = []
    days_sorted = 'MTWRFsS'
    for i in range(7):
        d = (start_day + i) % 7
        if days_sorted[d] in args.days:
            offsets.append(i)

    offset = 0
    week = 0
    cur_d = args.start
    while True:
        cur_d = start_date + \
            datetime.timedelta(weeks=week, days=offsets[offset])
        offset = (offset + 1) % len(offsets)
        if offset == 0:
            week += 1
        if cur_d > end_date:
            break
        print(format_date(args.template, cur_d))


def main():
    parser = argparse.ArgumentParser(
        prog='gen_schedule.py',
        description='generate list of class days')
    parser.add_argument('-s', '--start', type=parse_date, required=True,
                        help='start date of semester MM-DD-YYYY')
    parser.add_argument('-e', '--end', type=parse_date, required=True,
                        help='end date of semester MM-DD-YYYY')
    parser.add_argument('-d', '--days', type=str, required=True,
                        help='string representing days of week (SMTWRFs) for class (e.g., MWF, TR, etc.).')
    parser.add_argument('-t', '--template', type=str,
                        default=("- month_name: <MONTH_NAME><BR>"
                                 "  month: <MONTH><BR>"
                                 "  day_name: <DAY_NAME><BR>"
                                 "  day: <DAY><BR>"
                                 "  topic: <BR>"
                                 "  reading:  <BR>"
                                 "  assignment: <BR>"),
                        help=("template for printing days placeholders: <MONTH>, "
                              "<DAY>, <YEAR>, <MONTH_NAME>, <DAY_NAME>, <BR>"))
    args = parser.parse_args()
    generate(args)


if __name__ == '__main__':
    main()
