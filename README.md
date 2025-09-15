# Voidlink

> Decision support and data aggregation for EVE Online pilots, corporations, and alliances.

---

## Overview

Voidlink is a modular Django application that integrates with EVE Online APIs, zKillboard, and other sources to provide actionable intelligence and decision support for players, corporations, and alliances in the EVE Online universe. It offers a unified dashboard, asset tracking, character management, and more, with a focus on accessibility, security, and maintainability.

> [!TIP]
> Voidlink is designed for extensibility—add new data sources or features with minimal effort.

---

## Features

- **EVE Online SSO Integration**: Secure login and character management via EVE SSO.
- **Comprehensive Data Aggregation**: Combines data from EVE Online, zKillboard, and other APIs.
- **Modular Django Apps**: Each feature is a separate app for maintainability and scalability.
- **Asset & Wallet Tracking**: Monitor assets, wallet balances, and transactions.
- **Corporation & Alliance Management**: Tools for managing groups, contacts, and contracts.
- **Faction Warfare & Incursion Support**: Real-time data for PvP and PvE activities.
- **Accessibility & Security**: Built with WCAG 2.2 AA and OWASP best practices in mind.
- **Modern Frontend**: Tailwind CSS and DaisyUI for a responsive, accessible UI.
- **Automated Testing**: Pytest for backend, Playwright for frontend.

---

## Quickstart

```sh
# Install dependencies (uses uv)
just install

# Run the development server
just runserver

# Run backend tests
just test

# Run Playwright frontend tests
just test-playwright
```

---

## Project Structure

```
voidlink/
├── apps/                # Modular Django apps (character, corporation, wallet, etc.)
├── config/              # Django configuration and settings
├── assets/              # Static assets (CSS, JS)
├── tests/               # Backend and Playwright tests
├── justfile             # Project management commands
├── compose.yml          # Container orchestration (Docker Compose)
├── pyproject.toml       # Python project metadata
└── README.md            # Project documentation
```

---

## Development & Testing

- **Backend**: Python (Django), Pytest
- **Frontend**: Tailwind CSS, DaisyUI, Playwright
- **Containerization**: Docker Compose (see `compose.yml`)
- **Security**: Follows OWASP guidelines, no hardcoded secrets
- **Accessibility**: WCAG 2.2 AA compliance

> [!IMPORTANT]
> All new features and bug fixes must include tests. See `AGENTS.md` for detailed guidelines.

---

## Configuration

- Copy `env.template` to `.env` and fill in required environment variables.
- See `config/settings/` for Django settings.
- Use `justfile` for common project commands.

---

## Useful Resources

- [EVE Online API Documentation](https://developers.eveonline.com/)
- [zKillboard API](https://zkillboard.com/api/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [DaisyUI](https://daisyui.com/)

---

## Support & Community

- For issues, feature requests, or questions, please open a GitHub issue.

