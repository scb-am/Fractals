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
