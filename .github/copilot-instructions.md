# Voidlink Global Instructions

Voidlink is a django project that consumes data from EVE Online API, zKillboard API, and other sources to provide a comprehensive set of data to make informed decisions in the EVE Online universe.

## Repository Structure

- `config/`: Contains all the configuration settings for the Django project.
- `apps/`: Contains the core application code and django apps for the Voidlink project.
- `apps/static/`: Contains all the static files for the Voidlink project.
- `apps/templates/`: Contains all global templates for the Voidlink project.
- `app/**/templates/`: Contains all app-specific templates for the Voidlink project.
- `tests/` and `apps/**/tests/`: Contains all the test cases for the Voidlink project.
- `tests/playwright/`: Contains all the Playwright tests for the Voidlink project.
- `justfile`: Contains all the commands to manage the project using `just`.

## Key Tools
1. [Django](https://www.djangoproject.com/): The web framework used for the project.
2. [Playwright](https://playwright.dev/): Used for end-to-end testing of the frontend.
3. [pytest](https://pytest.org/): The testing framework used for backend tests.
4. [uv](https://docs.astral.sh/uv/): Package and virtual environment manager. You must use uv when adding packages.

## Key Guidelines
1. Follow the DRY (Don't Repeat Yourself) principle when writing code.
2. Assume that the development server is running, do not ask to run `just runserver`

### Backend Guidelines
1. Follow Django and Python best practices for code organization and structure. 
2. Write unit tests for all new backend features and bug fixes.

### Frontend Guidelines
1. Follow best practices for HTML, CSS, and JavaScript.
2. Global templates should go in `apps/templates/` and app specific templates should go in `apps/{app-name}/templates/`.
3. Write playwright tests for all new frontend features and bug fixes.
4. Ensure that all styling makes use of tailwind and DaisyUI components.
5. Ensure that all javascript lives outside of the HTML templates and is included as static files.