# AGENTS.md

## Project overview

This project is a Django-based application that integrates with EVE Online APIs, zKillboard, and other sources to provide comprehensive data and decision support for the EVE Online universe. It is structured with modular Django apps under `apps/`, configuration in `config/`, and global/static assets in their respective directories. The project emphasizes maintainability, accessibility, and security best practices.

## Build and test commands

- **Build/Install dependencies:**
  - `just install` (uses `uv` for Python dependency management)
- **Run development server:**
  - `just runserver`
- **Run backend tests:**
  - `just test`
- **Run Playwright frontend tests:**
  - `just test-playwright`

## Code style guidelines

- **Python:**
  - Follow PEP8 and project-specific conventions (see `.github/instructions/python.instructions.md`).
  - Use self-explanatory code and comment only for complex logic or business rules.
- **Frontend:**
  - Use Tailwind CSS and DaisyUI for styling.
  - Place all JavaScript in static files, not inline in templates.
- **Commits:**
  - Use Conventional Commits (see `.github/instructions/conventional-commit.instructions.md`).

## Testing instructions

- All new features and bug fixes must include tests.
- Backend: Use `pytest` for unit and integration tests. Place tests in `tests/` or `apps/**/tests/`.
- Frontend: Use Playwright for end-to-end tests. Place tests in `tests/playwright/`.
- Run all tests before submitting changes: `just test` and `just test-playwright`.

## Security considerations

- Follow OWASP and project security guidelines (see `.github/instructions/security-and-owasp.instructions.md`).
- Never hardcode secrets; use environment variables and `.env` for configuration.
- Use parameterized queries for all database access.
- Validate and sanitize all user input.
- Review dependencies for vulnerabilities regularly.
