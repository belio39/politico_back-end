# politico_back-end
Politico enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency.
# Politico_app    


# Usage

- Create a political party
- Get all political parties
- Get a specific political party
- Edit a specific political party
- Delete a particular party
- Create a political office
- Get all political offices
- Get a specific political office

# Prerequisities
  - Python 3.6 version
 
# Installation
Downlaod / clone the project to your local computer by:

- Download the zip file of this repository.
- Unzip it and navigate into the Politico_app directory.

# Virtual environment
Create a virtual environment
> $ virtualenv venv

Activate the environment

> $ venv/bin/activate 

# Dependencies
Install package requirements to your environment
>$ pip install -r requirements.txt 

# Env
Create a.env file in your Politico_app root directory and add:

- >$ venv/bin/activate
- >$ export FLASK_APP="run.py"
- >$ export SECRET="any-character-or-STRING-YOU-PREFER"
- >$ export APP_SETTINGS="development"

# Testing
To set up testing environment
- >$ pip install nose
- >$ pip install coverage

# Testing API endpoints
<table> 
<tr>
<th>Test</th>
<th>Endpoints</th>
<th>HTTP VERBS</th>
</tr>
<tr>
<td>Post sign up</td>
<td>/api/v1/signup</td>
<td>POST</td>
</tr>
<tr>
<td>Post political party</td>
<td>/api/v1/office</td>
<td>GET</td>
</tr>
<tr>
<td>Get a specific political party</td>
<td>/api/v1/political/<party_id></td>
<td>GET</td>
</tr>
<tr>
<td>Edit a specific political party </td>
<td>/api/v1/politicals/<paty_id>/party</td>
<td>POST</td>
</tr>
<td>Delete a particular party </td>
<td>/api/v1/particulars/<paty_id>/party</td>
<td>POST</td>
</tr>
</table>

# Resources
The API is hosted on [Heroku]

# Authors
> [Dennis rotich Belio](https://github.com/belio39)

# Acknowledgement
Andela Bootcamp - cohort 37
