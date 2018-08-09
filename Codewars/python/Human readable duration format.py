def format_duration(seconds):
    if seconds == 0:
        return "now"
    years=seconds/60/60/24/365
    seconds-=years*60*60*24*365

    days=seconds/60/60/24
    seconds-=days*60*60*24

    hours=seconds/60/60
    seconds-=hours*60*60

    minutes=seconds/60
    seconds-=minutes*60

    print(years,days,hours,minutes,seconds)
    formatted=[]
    for time,time_name in [(years,"year"),(days,"day"),(hours,"hour"),(minutes,"minute"),(seconds,"second")]:
        temp=""
        if not time is 0:
            temp="{} {}".format(time,time_name)
            if time >= 2:
                temp+="s"
        if temp:
            formatted.append(temp)

    formatted2=", ".join(formatted[:-1])
    if len(formatted)>1:
        return formatted2 + " and " + formatted[-1]
    else:
        return formatted.pop()