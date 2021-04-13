# Nyumba X

Nyumba X (pronounced Nyumba Kumi) is a web application built on Django as a neighbourhood watch application where users can stay up to date with events in their neighbourhood and also get to browse other neighbourhoods.

## Getting Started

- clone this repo

```
$ git clone https://github.com/BwanaQ/nyumba-kumi.git
```

### Prerequisites

- Python 3 latest version
- Pip3 installer
- virtualenv command

### Installing

1. cd into the nyumba-kumi folder

```
$ cd nyumba-kumi
```

2. Add a python 3 environment

```
$ virtualenv env
```

3. Enter the virtual environment

```
$ source env/bin/activate
```

4. Install dependancies from requirements.txt

```
(env)$ pip install -r requirements.txt
```

5. rename .env copy to .env then run this command

```
(env) $ source .env
```

6. Run server

```
(env) $ python manage.py runserver
```

## Deployment

to deploy to heroku simply create a project and attach your git hub repository

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - Frontend for the monolithic app

## Authors

- **Tom Hunja**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Thanks to [Toptal](https://www.toptal.com/developers/gitignore/api/django) for a beautiful .gitignore file

- Inspiration - My Technical Mentor Kelvin Onkundi and The Olympians Team MC38
