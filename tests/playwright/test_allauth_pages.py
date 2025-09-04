
import os
import uuid

import pytest
from playwright.sync_api import Page, expect

BASE_URL = 'http://localhost:8000'
ALLAUTH_URLS = [
    (f'{BASE_URL}/accounts/login/', 'Sign In', False),
    (f'{BASE_URL}/accounts/signup/', 'Sign Up', False),
    (f'{BASE_URL}/accounts/password/reset/', 'Password Reset', False),
    (f'{BASE_URL}/accounts/email/', 'Manage Email Addresses', True),
    (f'{BASE_URL}/accounts/logout/', 'Sign Out', True),
    (f'{BASE_URL}/accounts/password/change/', 'Change Password', True),
    (f'{BASE_URL}/accounts/password/set/', 'Set Password', True),
    (f'{BASE_URL}/accounts/inactive/', 'Account Inactive', False),
    (f'{BASE_URL}/accounts/social/connections/', 'Social Account Connections', True),
]

# Helper to sign up a user
def signup_user(page: Page, email: str, password: str):
    page.goto(f'{BASE_URL}/accounts/signup/')
    expect(page.get_by_role('heading', name='Sign Up')).to_be_visible()
    page.get_by_label('Email').fill(email)
    password_fields = page.locator('input[type="password"]')
    password_fields.nth(0).fill(password)
    password_fields.nth(1).fill(password)
    page.get_by_role('button', name='Sign Up').click()
    if '/accounts/email/' in page.url or '/accounts/confirm-email/' in page.url:
        login_user(page, email, password)

# Helper to login a user
def login_user(page: Page, email: str, password: str):
    page.goto(f'{BASE_URL}/accounts/login/')
    expect(page.get_by_role('heading', name='Sign In')).to_be_visible()
    page.get_by_label('Email or Username').fill(email)
    password_field = page.locator('input[type="password"]').first
    password_field.fill(password)
    page.get_by_role('button', name='Sign In').click()
    assert '/accounts/login/' not in page.url, 'Login failed, still on login page.'


# Use a pytest fixture to provide a unique user for each test
@pytest.fixture
def test_user():
    email = f'testuser_{uuid.uuid4().hex[:8]}@example.com'
    password = os.environ.get('TEST_USER_PASSWORD', 'TestPassword123!')
    return email, password


@pytest.mark.parametrize(('url', 'heading', 'requires_auth'), ALLAUTH_URLS)
def test_allauth_page_loads(page: Page, url, heading, requires_auth, test_user):
    email, password = test_user
    if requires_auth:
        # Always create and login a fresh user for auth-required pages
        signup_user(page, email, password)
        login_user(page, email, password)
    page.goto(url)
    expect(page).to_have_url(url)
    expect(page.get_by_role('heading', name=heading)).to_be_visible()
    skip_link = page.get_by_role('link', name='Skip to main')
    expect(skip_link).to_be_visible()
    submit_btn = page.locator('form button.btn')
    expect(submit_btn).to_be_visible()

    # The duplicate test_allauth_page_loads function has been removed.


# Additional tests for login page
def test_login_form_fields_and_error(page: Page):
    page.goto(f'{BASE_URL}/accounts/login/')
    expect(page.get_by_label('Email or Username')).to_be_visible()
    expect(page.get_by_label('Password')).to_be_visible()
    # Submit empty form to trigger error
    page.get_by_role('button', name='Sign In').click()
    expect(page.get_by_text('This field is required.', exact=False)).to_be_visible()

def test_signup_form_creates_user_and_login(page: Page, test_user):
    email, password = test_user
    page.goto(f'{BASE_URL}/accounts/signup/')
    expect(page.get_by_role('heading', name='Sign Up')).to_be_visible()
    page.get_by_label('Email').fill(email)
    page.get_by_label('Password').fill(password)
    page.get_by_label('Password (again)').fill(password)
    page.get_by_role('button', name='Sign Up').click()
    # If redirected to email confirmation, login manually
    if '/accounts/email/' in page.url or '/accounts/confirm-email/' in page.url:
        page.goto(f'{BASE_URL}/accounts/login/')
        page.get_by_label('Email or Username').fill(email)
        page.get_by_label('Password').fill(password)
        page.get_by_role('button', name='Sign In').click()
    assert '/accounts/login/' not in page.url, 'Signup or login failed.'

def test_signup_form_fields_and_error(page: Page):
    page.goto(f'{BASE_URL}/accounts/signup/')
    expect(page.get_by_role('heading', name='Sign Up')).to_be_visible()
    # Submit empty form to trigger error
    page.get_by_role('button', name='Sign Up').click()
    expect(page.get_by_text('This field is required.', exact=False)).to_be_visible()

def test_password_reset_flow(page: Page):
    page.goto(f'{BASE_URL}/accounts/password/reset/')
    expect(page.get_by_label('Email')).to_be_visible()
    page.get_by_role('button', name='Reset Password').click()
    expect(page.get_by_text('This field is required.', exact=False)).to_be_visible()

# Accessibility: test skip link focus
def test_skip_link_focus(page: Page):
    page.goto(f'{BASE_URL}/accounts/login/')
    page.keyboard.press('Tab')
    skip_link = page.get_by_role('link', name='Skip to main')
    expect(skip_link).to_be_focused()
