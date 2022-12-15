#!/usr/bin/env python3
import re
def read_match(read_path, pattern):
    results = []
    with open(read_path) as syslog:
        for line in syslog.readlines():
            line = line.strip()
            match = re.search(pattern, line)
            if match:
                results.append(list(match.groups()))
    return results

def sorted_errors(results):
    errors = {}
    for result in results:
        if result[1] not in errors.keys() and result[0] == "ERROR":
        	errors[result[1]] = 1
        elif result [1] in errors.keys() and result[0] == "ERROR":
        	errors[result[1]] += 1
    sorted_errors = sorted(errors.items(), key=lambda x:x[1], reverse=True)
    return sorted_errors

def usage_stats(results):
    users = {}
    for result in results:
        if result[2] not in users.keys():
            users[result[2]] = {"INFO": 0, "ERROR": 0}
        elif result[0] == "INFO":
            users[result[2]]["INFO"] += 1
        elif result[0] == "ERROR":
            users[result[2]]["ERROR"] += 1
    return  sorted(users.items())

def write_errors(error_path, errors):
	with open(error_path, "w") as error_log:
		header = "Error,Count\n"
		error_log.write(header)
		for error in errors:
			line = "{},{}\n".format(error[0].strip(), error[1])
			error_log.write(line)

def write_usage(usage_path, usage):
	with open(usage_path, "w") as usage_log:
		header = "Username,INFO,ERROR\n"
		usage_log.write(header)
		for user in usage:
			user = list(user)
			line = "{},{},{}\n".format(user[0], user[1]["INFO"], user[1]["ERROR"])
			usage_log.write(line)

read_path = "syslog.log"
error_path = "error_message.csv"
usage_path = "user_statistics.csv"
pattern = r"(INFO|ERROR)([\s\w\[#\]]*)\(([\w]*)\)$"
write_errors(error_path, list(sorted_errors(read_match(read_path, pattern))))
write_usage(usage_path, usage_stats(read_match(read_path, pattern)))
