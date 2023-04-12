from flask import Flask, render_template, request
from jira import JIRA
import os
import datetime

user = "******"
apikey = "******"
server = "*****"


def today_date():
    e = datetime.datetime.now()
    cloud_date = "%s-%s-%s" % (e.year, e.month, e.day)
    return cloud_date


app = Flask(__name__)


# @app.route('/')
# def main():
#     return render_template('index.html')


@app.route('/', methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
        box1 = request.form['email']
        box2 = request.form['message']
        options = {
            'server': server
        }
        jira = JIRA(options, basic_auth=(user, apikey))

        jira_dict_convert = {
            'project': {'key': "NOC"},  # NOC
            'summary': " TEST NOC form, IPA creds reset issue, user " + str(box1),
            'issuetype': {'name': "Task"},  # Task
            'description': str(box2),
            'customfield_12000': {"id": "36319"},
            # 'Cloud Operations Request Type is required.',
            'customfield_10032': [{"value": "Model N"}],
            # 'Customer is required.',
            'customfield_10602': {"id": "10559"},
            'customfield_12100': today_date(),  # 'Cloud Operations Requested Date is required.'
            # 'customfield_13001': {"value": str(box1)},  # Affected Environments
            'customfield_20659': [{"value": "N/A"}],  # Support Projects
        }
        new_issue = jira.create_issue(fields=jira_dict_convert)
        print(new_issue.permalink())
        return render_template('success.html')

    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
