import os
import uuid

import pytest
from playwright.sync_api import Page, expect

BASE_URL = 'http://localhost:8000'


# Reuse existing helpers from other tests where appropriate

def signup_user(page: Page, email: str, password: str):
    page.goto(f'{BASE_URL}/accounts/signup/')
    expect(page.get_by_role('heading', name='Sign Up')).to_be_visible()
    page.get_by_label('Email').fill(email)
    password_fields = page.locator('input[type="password"]')
    password_fields.nth(0).fill(password)
    password_fields.nth(1).fill(password)
    page.get_by_role('button', name='Sign Up').click()
    # If we are redirected to an email confirmation page, attempt login
    if '/accounts/email/' in page.url or '/accounts/confirm-email/' in page.url:
        page.goto(f'{BASE_URL}/accounts/login/')
        page.get_by_label('Email or Username').fill(email)
        page.get_by_label('Password').fill(password)
        page.get_by_role('button', name='Sign In').click()


@pytest.fixture
def test_user():
    email = f'testuser_{uuid.uuid4().hex[:8]}@example.com'
    password = os.environ.get('TEST_USER_PASSWORD', 'TestPassword123!')
    return email, password


def test_navbar_dropdown_click_and_keyboard(page: Page, test_user):
    email, password = test_user
    # create and login a user
    signup_user(page, email, password)
    page.goto(BASE_URL)

    # Wait for username to appear in navbar
    username_button = page.get_by_role('button', name='Open user menu')
    expect(username_button).to_be_visible()

    # Visual alignment check: compare center Y of Home link and username button
    home_link = page.get_by_role('link', name='Home')
    hb = home_link.bounding_box()
    ub = username_button.bounding_box()
    # Both bounding boxes should be available
    assert hb is not None
    assert ub is not None
    home_center_y = hb['y'] + hb['height'] / 2
    user_center_y = ub['y'] + ub['height'] / 2
    # Allow small difference (in pixels)
    tolerance = 6
    diff = abs(home_center_y - user_center_y)
    assert diff <= tolerance, (
        'Navbar items misaligned: '
        f'{home_center_y} vs {user_center_y}'
    )

    # Click to open dropdown
    username_button.click()
    # menu should become visible (links present)
    expect(page.get_by_role('link', name='Profile')).to_be_visible()
    expect(page.get_by_role('link', name='Logout')).to_be_visible()

    # Test keyboard: focus button, press Enter to open
    username_button.focus()
    page.keyboard.press('Enter')
    expect(page.get_by_role('link', name='Profile')).to_be_focused()

    # From Profile, press ArrowDown to go to Logout
    page.keyboard.press('ArrowDown')
    expect(page.get_by_role('link', name='Logout')).to_be_focused()

    # Press Escape to close menu and focus should return to button
    page.keyboard.press('Escape')
    expect(username_button).to_be_focused()

    # Open via ArrowDown on button
    username_button.focus()
    page.keyboard.press('ArrowDown')
    expect(page.get_by_role('link', name='Profile')).to_be_focused()

    # Finally click Logout and expect to land on logout or landing
    page.get_by_role('link', name='Logout').click()
    # After logout, the login link should be visible again
    login_link = page.get_by_role('link', name='Login')
    expect(login_link).to_be_visible()
