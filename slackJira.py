import requests
import sys
import getopt
import json

#send message

def send_slack_message(message):
	payload ='{"text":"%s"}' % message
	response = requests.post('https://hooks.slack.com/services/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',
		data = payload)
	print(response.text)
	create_issue(message)

def create_issue(message):
	headers={
	"Accept": "application/json",
	"Content-Type": "application/json"
	}
	value = {
		"fields": {
		"project":{
		"key":"IN"
		},
		"summary":message,
		"description" : "Issue created from slack",
		"issuetype":{
		"name":"Task"
		}
		}
		}
	payload = json.dumps(value)
	response = requests.post('https://slackjira-integration.atlassian.net/rest/api/2/issue',
		headers = headers,
		data = payload,
		auth=("naman.chhajed008@gmail.com", "0i7JhG0oCtcwZLqZrIQF8CA3"))
	data = response.json()
	print(data)

def main(argv):
	message =" "

	try: opts, args = getopt.getopt(argv, "hm:",["message="])

	except getopt.GetoptError:
		print('slackJira.py -m <message>')
		sys.exit(2)

	if len(opts)==0:
		print('provide a valid message')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('slackJira.py -m <message>')
			sys.exit()
		elif opt in ("-m","--message"):
			message= arg

	send_slack_message(message)

if __name__ == "__main__":
	main(sys.argv[1:])