[![Build Status](https://travis-ci.org/belio39/politico_back-end.svg?branch=develop)](https://travis-ci.org/belio39/politico_back-end)


[![Maintainability](https://api.codeclimate.com/v1/badges/1cb17183af1da03af9b6/maintainability)](https://codeclimate.com/github/belio39/politico_back-end/maintainability)


# politico_back-end
Politico enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency.

# Usage

- Home page
- Create an account
- Login into your account
- Post a question
- Fetch all questions
- Fetch a single question
- Edit a specific question
- Delete a specific question
- Post an answer to a question

# Prerequisities
  - Python 3.6 version
 
# Installation
Downlaod / clone the project to your local computer by:

- Download the zip file of this repository.
- Unzip it and navigate into the Politico_back_end directory.

# Virtual environment
Create a virtual environment
> $ virtualenv venv

Activate the environment

> $ venv/bin/activate 

# Dependencies
Install package requirements to your environment
>$ pip install -r requirements.txt 

# Env
Create a.env file in your Politico_back_end root directory and add:

- >$ venv/bin/activate
- >$ export FLASK_APP="run.py"
- >$ export SECRET="any-character-or-STRING-YOU-PREFER"
- >$ export APP_SETTINGS="development"

# Testing
To set up testing environment
- >$ pip install pytest
- >$ pip install coverage

# Testing API endpoints
<table> 
<tr>
<th>Test</th>
<th>Endpoints</th>
<th>HTTP VERBS</th>
</tr>
<tr>
<td>Create a political party</td>
<td>/api/v1/party</td>
<td>POST</td>
</tr>
<tr>
<td>Get all political parties</td>
<td>/api/v1/party</td>
<td>GET</td>
</tr>
<tr>
<td>Get a specific political party</td>
<td>/api/v1/<party_id></td>
<td>GET</td>
</tr>
<tr>
<td>Edit a specific political party</td>
<td>/api/v1/<party_id>/party</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a particular party</td>
<td>/api/v1/party</td>
<td>DELETE</td>
</tr>
<tr>
<td>Create a political office</td>
<td>/api/v1/office</td>
<td>POST</td>
</tr>
<tr>
<td>Get all political offices</td>
<td>/api/v1/office</td>
<td>GET</td>
</tr>
<tr>
<td>Get a specific political office</td>
<td>/api/v1/office</td>
<td>GET</td>
</tr>
</table>

# Resources
The API is hosted on [Heroku](https://politico.app.herokuapp.com/)

# Authors
> [Dennis rotich Belio](https://github.com/belio39)

# Acknowledgement
Andela Bootcamp - cohort 37
