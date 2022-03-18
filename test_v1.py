import datetime


def numOfDays(date1, date2):

    return (date2-date1).days


date1 = datetime.datetime(
    int(input('enter_a_first_year:')),
    int(input('enter_a_first_month:')),
    int(input('enter_a_first_day:'))
    )

date2 = datetime.datetime(
    int(input('enter_a_last_year:')),
    int(input('enter_a_last_month:')),
    int(input('enter_a_last_day:'))
    )

print(numOfDays(date1, date2), "days_betwen_date")

x1 = numOfDays(date1, date2)
x2 = x1 * 0.082

print((x2), "days_otpusk_for_date")
