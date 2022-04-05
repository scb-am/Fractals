import pdb
from datetime import datetime, timedelta


def checkio(log_text):
    logs = []
    for log in log_text.split("\n"):
        log_date_time, user, host = log.split(";;")
        user = user.lower()
        log_date_time = datetime.strptime(log_date_time, '%Y-%m-%d-%H-%M-%S')
        host = ".".join(host.split("//")[1].split("/")[0].split(".")[-2:])
        host = host.lower()
        logs.append([log_date_time, user, host])

    result = {}
    for log in logs:
        result.setdefault(log[1], {"sessions": {log[2]: []}})
        result[log[1]]["sessions"].setdefault(log[2], [])
        if result[log[1]]["sessions"][log[2]]:
            log_diff = log[0] - result[log[1]]["sessions"][log[2]][-1]["last"]
            if log_diff > timedelta(minutes=30):
                result[log[1]]["sessions"][log[2]].append(
                    {
                        "start": log[0],
                        "last": log[0],
                        "duration": timedelta(seconds=1),
                        "count": 1,
                    }
                )
            else:
                duration = log[0] - result[log[1]]["sessions"][log[2]][-1]["start"] + timedelta(seconds=1)
                result[log[1]]["sessions"][log[2]][-1]["count"] += 1
                result[log[1]]["sessions"][log[2]][-1]["duration"] = duration
                result[log[1]]["sessions"][log[2]][-1]["last"] = log[0]
        else:
            result[log[1]]["sessions"][log[2]].append(
                {
                    "start": log[0],
                    "last": log[0],
                    "duration": timedelta(seconds=1),
                    "count": 1,
                }
            )

    sessions = []
    for user, user_sessions in result.items():
        for host, host_sessions in user_sessions["sessions"].items():
            for host_session in host_sessions:
                sessions.append([user, host, host_session["duration"].seconds, host_session["count"]])

    return "\n".join([";;".join([str(i) for i in x]) for x in sorted(sessions, key=lambda x: [x[0], x[1], x[2], x[3]])])




# from datetime import datetime as datetime, timedelta
#
#
# class WebSession:
#     def __init__(self):
#         self.seconds = 1
#         self.len = 0
#         self.last = None
#
#     def add_log(self, time):
#         self.seconds += (time - self.last).seconds if self.last else 0
#         self.last = time
#         self.len += 1
#
#
# def parse_log(line):
#     from re import match
#     time, name, request = line.lower().split(';;')
#     time = datetime.strptime(time, '%Y-%m-%d-%H-%M-%S')
#     url = match('(https?://)?(\w+\.)*(\w+\.\w+)/?.*', request).groups()[-1]
#     return time, name, url




# def checkio(sessions):
#     data, out = dict(), []
#     for i in sessions.split():
#         pattern = r'(.+?);;(.+?);;https?://(.*\.)?(.+?\..+?)/'
#         time, user, _, site = __import__('re').search(pattern, i.lower()+'/').groups()
#         time = __import__('datetime').datetime.strptime(time, '%Y-%m-%d-%H-%M-%S')
#         data[(user, site)] = data[(user, site)]+[time] if (user, site) in data else [time]
#     for time, (user, site) in [(data[x], x) for x in data]:
#         duration, count = 1, 1
#         for delta in [(y-x).total_seconds() for x, y in zip(time, time[1:])]:
#             out += [(user, site, int(duration), count)] if delta > 30*60 else []
#             (count, duration) = (1, 1) if delta > 30*60 else (count+1, duration+delta)
#         out += [(user, site, int(duration), count)] if duration > 0 else []
#     return '\n'.join(["%s;;%s;;%s;;%s" % x for x in sorted(out)])




# import datetime
#
#
# class Request:
#     def __init__(self, s):
#         data = s.split(";;")
#         self.user = data[1].lower()
#         self.datetime = datetime.datetime.strptime(data[0], "%Y-%m-%d-%H-%M-%S")
#         target = data[2]
#         domain = target.split("/")[2]
#         self.domain = ".".join(domain.split(".")[-2:])
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __str__(self):
#         return str((self.datetime, self.user, self.domain))
#
#
# def checkio(s):
#     data = s.split("\n")
#     sessions = {}
#     dead_sessions = []
#     for d in data:
#         request = Request(d)
#         key = (request.user, request.domain)
#         if key in sessions:
#             session = sessions[key]
#             if (request.datetime - session[-1].datetime).total_seconds() > 30 * 60:
#                 dead_sessions.append(session)
#                 sessions[key] = []
#         else:
#             sessions[key] = []
#         sessions[key].append(request)
#     for key in sessions:
#         dead_sessions.append(sessions[key])
#     sessions_data = []
#     for session in dead_sessions:
#         name = session[0].user
#         domain = session[0].domain
#         count = len(session)
#         duration = (session[-1].datetime - session[0].datetime).total_seconds() + 1
#         sessions_data.append((name, domain, duration, count))
#     sessions_data = sorted(sessions_data)
#     out_string = ""
#     for session in sessions_data:
#         if out_string != "":
#             out_string += "\n"
#         out_string += "{};;{};;{};;{}".format(session[0], session[1], int(session[2]), session[3])
#     return out_string

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(
"""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
==
"""name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"
