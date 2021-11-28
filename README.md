# Slackify Me App in Python Django

![cicd cloud run workflow](https://github.com/MatthewCYLau/slackify-me-django/actions/workflows/cicd-cloud-run.yml/badge.svg)

A Python Django app which turns our plain text messages into emojis

App URL [here](https://slackify-me-django-3i2mtbjusq-ew.a.run.app)

## Installation

Make sure you already have Python and pip installed

```bash
python --version # should print Python version
pip --version # should print pip version
```

Install virtualenv:

```bash
pip install virtualenv
virtualenv --version # should print virtualenv version
```

Create virtual environment:

```bash
virtualenv venv # create a virtual environment called venv
source venv/bin/activate # activate virtual environemnt
```

Install dependencies

```bash
pip install -r requirements.txt
```

To deactivate virtual environment, run `deactivate`

## Usage

In the project root directory, run this command:

```bash
python manage.py runserver # app starts at http://localhost:8000/
```

## Deploy to Cloud Run

In the project root directory, run this command:

```bash
docker build -t gcr.io/<your_gcp_project_id>/slackify-me-django:latest .
docker run -p 8000:8000 gcr.io/<your_gcp_project_id>/slackify-me-django:latest
docker push gcr.io/<your_gcp_project_id>/slackify-me-django:latest
gcloud run deploy --image=gcr.io/<your_gcp_project_id>/slackify-me-django:latest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
