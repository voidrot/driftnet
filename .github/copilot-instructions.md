# driftnet Global Instructions

driftnet is a django project that consumes data from EVE Online API, zKillboard API, and other sources to provide a comprehensive set of data to make informed decisions in the EVE Online universe.

## Repository Structure

- `config/`: Contains all the configuration settings for the Django project.
- `apps/`: Contains the core application code and django apps for the driftnet project.
- `apps/static/`: Contains all the static files for the driftnet project.
- `apps/templates/`: Contains all global templates for the driftnet project.
- `app/**/templates/`: Contains all app-specific templates for the driftnet project.
- `apps/**/test.py` and `apps/**/tests/`: Contains all the unit test cases for the driftnet project.
- `e2e/`: Contains all the Playwright tests for the driftnet project.
- `justfile`: Contains all the commands to manage the project using `just`.

## Key Tools
1. [Django](https://www.djangoproject.com/): The web framework used for the project.
2. [Playwright](https://playwright.dev/): Used for end-to-end testing of the frontend.
3. [pytest](https://pytest.org/): The testing framework used for backend tests.
4. [uv](https://docs.astral.sh/uv/): Package and virtual environment manager. You must use uv when adding packages.
5. [django-allauth](https://docs.allauth.org/en/latest/): Used for authentication and social account management.
6. Tailwind CSS and [DaisyUI](https://daisyui.com/): Used for styling the frontend.

## Key Guidelines
1. Follow the DRY (Don't Repeat Yourself) principle when writing code.
2. Assume that the development server is running, do not ask to run `just runserver`

### Backend Guidelines
1. Follow Django and Python best practices for code organization and structure. 
2. Write unit tests for all new backend features and bug fixes.
3. Code must follow secure coding practices (see OWASP Top 10 and security-and-owasp.instructions.md).
4. Optimize for performance and scalability (see performance-optimization.instructions.md).
5. Adhere to DevOps principles (CALMS, DORA metrics) and automate CI/CD pipelines where possible.

### Frontend Guidelines
1. Follow best practices for HTML, CSS, and JavaScript.
2. Global templates should go in `apps/templates/` and app specific templates should go in `apps/{app-name}/templates/`.
3. Write playwright tests for all new frontend features and bug fixes.
4. Ensure that all styling makes use of tailwind and DaisyUI components.
5. Ensure that all javascript lives outside of the HTML templates and is included as static files.
6. Build all frontend code with accessibility in mind (see a11y.instructions.md, WCAG 2.2 AA).
7. Optimize for frontend performance (see performance-optimization.instructions.md).

### Commenting Standards
- Write self-explanatory code. Only comment to explain WHY, not WHAT. See self-explanatory-code-commenting.instructions.md.

### Test Coverage
- Aim for 90%+ coverage on new backend code. All new features and bug fixes must include tests.

### Contribution Guidelines
- Follow standard code style and commit message conventions.
- Submit pull requests with clear descriptions and context for changes.
- All code must pass CI/CD checks and meet test coverage requirements.
- Reviewers should provide constructive feedback and context for requested changes.

### Security Guidelines
- Always follow the principle of least privilege and deny by default.
- Use parameterized queries for all database access.
- Never hardcode secrets; use environment variables or secret managers.
- Validate and sanitize all user input.
- Set appropriate security headers for web applications.
- Keep dependencies up to date and run vulnerability scans regularly.

### Accessibility Guidelines
- Code must conform to WCAG 2.2 Level AA and go beyond minimal conformance where possible.
- All interactive elements must be keyboard navigable and have clear focus states.
- Use semantic HTML and ARIA attributes appropriately.
- Provide skip links and consistent navigation structure.
- Ensure sufficient color contrast and avoid using color as the only means of conveying information.

### Performance Guidelines
- Measure before optimizing; use profiling tools to identify bottlenecks.
- Optimize for the common case and avoid premature optimization.
- Minimize resource usage and prefer simplicity.
- Automate performance testing and set performance budgets.

### DevOps Guidelines
- Foster a collaborative, blameless culture and shared responsibility.
- Automate everything possible (CI/CD, testing, infrastructure).
- Apply lean principles to eliminate waste and maximize flow.
- Measure key metrics (DORA) and use data to drive improvement.
- Promote knowledge sharing and clear documentation.

---

For further details, see the instructions in the `.github/instructions/` directory.
