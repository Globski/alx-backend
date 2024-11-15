# Alx Backend - i18n

## Description

This project is about adding **internationalisation (i18n)** to a Flask web application. The goal is to allow the application to support multiple languages and handle locale-specific features, such as displaying timestamps in the correct timezone. You will use two key libraries: **Flask-Babel** for localisation and **pytz** for time zone handling. The main goals of this project are to enable the Flask application to support different languages. To ensure that timestamps are displayed according to the user's timezone. Allow dynamic switching of language preferences. This project is divided into several tasks that build upon each other. Each task will guide you through the process of implementing different internationalisation features. At the end of this project, you will have a Flask web application that dynamically changes its language based on user preference. Displays timestamps in the correct timezone. Provides a localised experience for users from different regions.

## Project Structure

| Task # | Description                                                                                                                                                     | Source Code/File                                        |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| 0      | **Basic Flask app**: Setup a basic Flask app in `0-app.py` with a `/` route and `index.html` template that outputs "Welcome to Holberton" and "Hello world".     | `0-app.py`, `templates/0-index.html`                   |
| 1      | **Basic Babel setup**: Install Flask-Babel, configure the app to support languages `["en", "fr"]`, set default locale to `en`, and timezone to `UTC`.           | `1-app.py`, `templates/1-index.html`                   |
| 2      | **Get locale from request**: Create `get_locale` function to select the best language based on request headers.                                                   | `2-app.py`, `templates/2-index.html`                   |
| 3      | **Parametrize templates**: Parametrize templates with `_` or `gettext` for message IDs `home_title` and `home_header`, and set up translation files.             | `3-app.py`, `babel.cfg`, `templates/3-index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po` |
| 4      | **Force locale with URL parameter**: Implement locale switching by passing `locale=fr` or `locale=en` in the URL.                                                | `4-app.py`, `templates/4-index.html`                   |
| 5      | **Mock logging in**: Simulate user login by passing `login_as` URL parameter and display welcome message based on user settings (locale).                       | `5-app.py`, `templates/5-index.html`                   |
| 6      | **Use user locale**: Update `get_locale` to prioritize user’s preferred locale.                                                                               | `6-app.py`, `templates/6-index.html`                   |
| 7      | **Infer appropriate time zone**: Implement `get_timezone` to determine user timezone from URL or user settings, defaulting to `UTC` if unknown.                | `7-app.py`, `templates/7-index.html`                   |
| 8      | **Display the current time**: Based on inferred timezone, display the current time in both English and French.                                                   | `app.py`, `templates/index.html`, `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po` |

## Environment

- **Operating System**: Ubuntu 18.04 LTS
- **Python Version**: 3.7

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- Your code should use the pycodestyle style (version 2.5)
- The first line of all your files should be exactly #!/usr/bin/env python3
- All your *.py files should be executable
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions and methods should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Learning Objectives

By the end of this project, you will learn to:
- Parametrize Flask templates to display different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps according to the user’s timezone.

## Prototype Used in the Project

| Function/Method | Description                                                      | File Location           |
|-----------------|------------------------------------------------------------------|-------------------------|
| `get_locale`    | Determines the best locale for the user based on URL, user settings, and request headers. | `5-app.py`, `6-app.py`  |
| `get_user`      | Simulates user login by fetching user data from a mock database. | `5-app.py`              |
| `get_timezone`  | Determines the user's timezone based on URL or user settings, validates it using `pytz`. | `7-app.py`              |
| `before_request`| Executes before each request to set user locale and timezone.   | `5-app.py`              |

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/alx-backend.git
   cd alx-backend/0x02-i18n
   ```

2. Install the required dependencies **Setup Your Flask Application**: 
  - Install Flask and Flask-Babel:
   ```bash
   pip3 install flask flask_babel==2.0.0 pytz
   ```
 - **Configure Flask-Babel**:
   Flask-Babel helps to manage translations and time zones in your Flask application. You will configure it to support different locales (languages) based on the request.

- **Locale Selection and Translation**:
   You will need to provide translations for different languages. You can use **gettext** (provided by Flask-Babel) to mark strings for translation.

4. To extract translatable strings and initialize translations:
   - Then, use **pybabel** to extract the strings and generate translation files:

   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   pybabel init -i messages.pot -d translations -l en
   pybabel init -i messages.pot -d translations -l fr
   pybabel compile -d translations
   ```

-    Use **pytz** to handle time zone conversions.  

5. Run the application:

   ```bash
   python3 0-app.py
   ```

6. Access the app by navigating to `http://127.0.0.1:5000/`.

7. **Testing**:
   Ensure that the application works as expected, especially checking:
   - Translations are applied correctly.
   - Timezones are displayed according to the user's locale.
   - The application gracefully falls back to the default language if no locale is specified.

**Set up Flask and Flask-Babel**:
   - Install and configure Flask-Babel to handle language translation in the app.

**Support Multiple Languages**:
   - Enable the app to support different languages (e.g., English, Spanish) and display translated text based on the user's preferred language.

**Handle Time Zones with pytz**:
   - Use the **pytz** library to ensure that timestamps are displayed according to the user's local time zone.

**User Preferences**:
   - Allow users to dynamically select their preferred language and time zone, which will adjust the content accordingly.
     
## Additional Notes

- The project utilizes **Flask-Babel** for handling translations and timezones.
- **Pytz** is used for managing timezones, ensuring that the time is displayed correctly according to the user's location.
- To initialize translations, use `pybabel` commands to extract and compile the translation files.

- **Parametrize Flask templates to display different languages**: This means setting up your Flask templates to render text in different languages based on the user's preferences or settings.
- **Infer the correct locale**: You need to determine the locale (language and region) based on user settings, URL parameters, or request headers.
- **Localize timestamps**: Format timestamps based on the user's locale, ensuring that dates and times appear correctly in different regions.

- **Flask-Babel**: This extension provides support for translations, locale-specific formatting, and more.
- **pytz**: A library used to handle time zone conversion and display timestamps correctly.
   - Supports multiple languages
   - Localizes timestamps based on user time zone
   - Automatically detects the user's locale from request headers

## Translations
The application supports English, Spanish, and French. You can add additional languages by using **pybabel** to extract and initialize translation files.

### 1. **Parametrize Flask Templates for Multiple Languages**  
   - Use **Flask-Babel** to enable language-specific translations in your templates.
   - Mark strings for translation using `gettext()` or the `_()` function.
   - Example:  
     ```html
     <h1>{{ _('Welcome to our website!') }}</h1>
     ```
   - Provide translated `.po` files for different languages (e.g., `en.po`, `es.po`).

---

### 2. **Infer Locale from URL, User Settings, or Request Headers**  
   - **URL parameters**: You can pass the language code in the URL, like `/en` or `/es`, to switch the language.
   - **User settings**: Store the user's preferred language in a session or database.
   - **Request headers**: Use the `Accept-Language` header to detect the user's preferred language automatically.
   - Example in Flask:
     ```python
     @babel.init_app(app, locale_selector=get_locale)
     def get_locale():
         return request.args.get('lang', 'en')  # Fallback to 'en'
     ```

---

### 3. **Localize Timestamps**  
   - Use **Flask-Babel** to format timestamps according to the user's locale.
   - Example:
     ```html
     <p>{{ event_time | datetime('short') }}</p>
     ```
   - This will format `event_time` according to the user's locale (e.g., `MM/DD/YYYY` for US or `DD/MM/YYYY` for Europe).


## Tasks

### 0. Basic Flask app

First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).


- File: 0-app.py, templates/0-index.html

---

### 1. Basic Babel setup

Install the Babel Flask extension:

```bash
$ pip3 install flask_babel==2.0.0
```

Then instantiate the Babel object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.


- File: 1-app.py, templates/1-index.html

---

### 2. Get locale from request


Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.


- File: 2-app.py, templates/2-index.html

---

### 3. Parametrize templates


Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing

```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

Then initialize your translations with

```bash
$ pybabel extract -F babel.cfg -o messages.pot .
```

and your two dictionaries with
```bash
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

| msgid         | English               | French              |
|---------------|-----------------------|---------------------|
| home_title    | "Welcome to Holberton" | "Bienvenue chez Holberton" |
| home_header   | "Hello world!"         | "Bonjour monde!"     |

Then compile your dictionaries with

```bash
$ pybabel compile -d translations
```

Reload the home page of your app and make sure that the correct messages show up.



- File: 3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo

---

### 4. Force locale with URL parameter

In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and if its value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading:

<img width="328" alt="54f3be802024dbcf06f4" src="https://github.com/user-attachments/assets/66ef05cb-795d-43c1-9da1-2cb15c5fd376">

- File: 4-app.py, templates/4-index.html

---

### 5. Mock logging in

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.

```python
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```

This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

| msgid          | English                        | French                         |
|----------------|--------------------------------|--------------------------------|
| logged_in_as   | "You are logged in as %(username)s." | "Vous êtes connecté en tant que %(username)s." |
| not_logged_in  | "You are not logged in."       | "Vous n'êtes pas connecté."   |

Visiting `http://127.0.0.1:5000/` in your browser should display this:

<img width="254" alt="f958f4a1529b535027ce" src="https://github.com/user-attachments/assets/0b38a5ef-9911-419b-b4eb-e541d54d30b8">


Visiting `http://127.0.0.1:5000/?login_as=2` in your browser should display this:

<img width="259" alt="277f24308c856a09908c" src="https://github.com/user-attachments/assets/8e5ec94f-726e-493b-b45d-1aba52685f15">

- File: 5-app.py, templates/5-index.html

---

### 6. Use user locale

Change your `get_locale` function to use a user’s preferred locale if it is supported.

The order of priority should be:
- Locale from URL parameters
- Locale from user settings
- Locale from request header
- Default locale

Test by logging in as different users.

<img width="272" alt="9941b480b0b9d87dc5de" src="https://github.com/user-attachments/assets/113ef5ae-8716-4aee-9c46-5a959c585bb8">

- File: 6-app.py, templates/6-index.html

---

### 7. Infer appropriate time zone

Define a `get_timezone` function and use the `babel.timezoneselector` decorator.

The logic should be the same as `get_locale`:

- Find `timezone` parameter in URL parameters
- Find time zone from user settings
- Default to `UTC`

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To do that, use `pytz.timezone` and catch the `pytz.exceptions.UnknownTimeZoneError` exception.

- File: 7-app.py, templates/7-index.html

---

### 8. Display the current time

Based on the inferred time zone, display the current time on the home page in the default format. For example:

`Jan 21, 2020, 5:55:39 AM` or `21 janv. 2020 à 05:56:28`

Use the following translations:

| msgid          | English                         | French                        |
|----------------|---------------------------------|-------------------------------|
| current_time_is| "The current time is %(current_time)s." | "Nous sommes le %(current_time)s." |

Displaying the time in French looks like this:

<img width="299" alt="bba4805d6dca0a46a0f6" src="https://github.com/user-attachments/assets/14f23ae9-acd9-47b6-99ea-7e91d42e3f73">

Displaying the time in English looks like this:

<img width="328" alt="54f3be802024dbcf06f4" src="https://github.com/user-attachments/assets/7a0376e8-28c6-4506-a288-97e0793f3482">

- File: app.py, templates/index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po
