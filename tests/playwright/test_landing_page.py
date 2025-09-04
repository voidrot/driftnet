import pytest
import re
from playwright.sync_api import Page, expect

BASE_URL = 'http://localhost:8000'


@pytest.fixture(autouse=True)
def before_each_after_each(page: Page):
    # Go to the landing page before each test.
    page.goto(f'{BASE_URL}/')


def test_landing_page_loads(page: Page):
    """Test that the landing page loads successfully."""
    expect(page).to_have_title('Voidlink')


def test_main_heading(page: Page):
    """Test the main heading and subtitle are displayed."""
    expect(page.locator('h1:has-text("Voidlink")')).to_be_visible()
    expect(page.get_by_text('Your EVE Online Intelligence Dashboard')).to_be_visible()


def test_skip_link(page: Page):
    """Test the skip to main content link."""
    skip_link = page.get_by_role('link', name='Skip to main features')
    expect(skip_link).to_be_visible()
    expect(skip_link).to_have_attribute('href', '#features')


def test_features_section(page: Page):
    """Test the features section is displayed with correct content."""
    expect(page.get_by_role('heading', name='What Voidlink Can Do')).to_be_visible()

    # Test feature cards
    expect(page.get_by_role('heading', name='EVE API Integration')).to_be_visible()
    expect(
        page.get_by_text(
            'Connect your EVE Online account and view real-time '
            'character, corporation, and alliance data.'
        )
    ).to_be_visible()

    expect(page.get_by_role('heading', name='zKillboard Insights')).to_be_visible()
    expect(
        page.get_by_text(
            'Analyze killmails, ship losses, and PvP stats with data from zKillboard.'
        )
    ).to_be_visible()

    expect(page.get_by_role('heading', name='Decision Support')).to_be_visible()
    expect(
        page.get_by_text(
            'Get actionable intelligence for fleet ops, market moves, '
            'and strategic planning.'
        )
    ).to_be_visible()


def test_how_it_works_section(page: Page):
    """Test the How It Works section."""
    expect(page.get_by_role('heading', name='How It Works')).to_be_visible()

    # Test the mockup code content
    expect(
        page.get_by_text('1. Sign up and link your EVE Online account.')
    ).to_be_visible()
    expect(
        page.get_by_text(
            '2. Explore dashboards for your characters, corporations, and alliances.'
        )
    ).to_be_visible()
    expect(
        page.get_by_text('3. Access killboard analytics and market data.')
    ).to_be_visible()
    expect(
        page.get_by_text("Make informed decisions with Voidlink's intelligence tools.")
    ).to_be_visible()


def test_get_started_section(page: Page):
    """Test the Get Started section and sign up button."""
    expect(page.get_by_role('heading', name='Get Started')).to_be_visible()

    sign_up_button = page.locator('#maincontent a[href="/account/signup/"]')
    expect(sign_up_button).to_be_visible()
    expect(sign_up_button).to_have_attribute('href', '/account/signup/')


def test_navigation_links(page: Page):
    """Test the navigation links in the header."""
    # Test Home link
    home_link = page.get_by_role('link', name='Home')
    expect(home_link).to_be_visible()
    expect(home_link).to_have_attribute('href', '/')

    # Test Login link (when not authenticated)
    login_link = page.locator('nav a[href="/accounts/login/"]')
    expect(login_link).to_be_visible()
    expect(login_link).to_have_attribute('href', '/accounts/login/')

    # Test Sign Up link (when not authenticated) - specifically in navigation
    signup_link = page.locator('nav a[href="/accounts/signup/"]')
    expect(signup_link).to_be_visible()
    expect(signup_link).to_have_attribute('href', '/accounts/signup/')


def test_footer_visibility(page: Page):
    """Test that the footer is visible and contains correct content."""
    footer = page.locator('footer')
    expect(footer).to_be_visible()
    expect(footer).to_contain_text('Voidlink. All rights reserved.')
    expect(footer).to_contain_text('2025')


def test_responsive_design(page: Page):
    """Test that the page is responsive."""
    # Test on different viewport sizes
    page.set_viewport_size({'width': 375, 'height': 667})  # Mobile
    expect(page.locator('h1:has-text("Voidlink")')).to_be_visible()

    page.set_viewport_size({'width': 768, 'height': 1024})  # Tablet
    expect(page.locator('h1:has-text("Voidlink")')).to_be_visible()

    page.set_viewport_size({'width': 1920, 'height': 1080})  # Desktop
    expect(page.locator('h1:has-text("Voidlink")')).to_be_visible()


def test_accessibility(page: Page):
    """Test basic accessibility features."""
    # Test that main content has proper heading hierarchy
    main_headings = page.locator('h1, h2').all()
    assert len(main_headings) > 0

    # Test that images have alt text (if any)
    images = page.locator('img')
    for img in images.all():
        alt_attr = img.get_attribute('alt')
        assert alt_attr is not None
        assert alt_attr.strip() != ''

    # Test that form elements have labels (if any)
    inputs = page.locator('input')
    for input_element in inputs.all():
        input_id = input_element.get_attribute('id')
        if input_id:
            label = page.locator(f'label[for="{input_id}"]')
            assert label.count() > 0


def test_sign_up_button_click(page: Page):
    """Test that the Sign Up button navigates to the signup page."""
    sign_up_button = page.locator('#maincontent a[href="/account/signup/"]')
    sign_up_button.click()
    expect(page).to_have_url(re.compile(r'/account/signup/'))


def test_navigation_link_functionality(page: Page):
    """Test that navigation links work correctly."""
    # Remove Django Debug Toolbar to avoid interference
    page.evaluate('document.getElementById("djDebug")?.remove()')

    # Test Login link
    login_link = page.locator('nav a[href="/accounts/login/"]')
    login_link.click()
    expect(page).to_have_url(re.compile(r'/accounts/login/'))
    page.go_back()  # Go back to landing page

    # Test Sign Up link
    signup_link = page.locator('nav a[href="/accounts/signup/"]')
    signup_link.click()
    expect(page).to_have_url(re.compile(r'/accounts/signup/'))
    page.go_back()  # Go back to landing page

    # Test Home link (should stay on same page)
    home_link = page.get_by_role('link', name='Home')
    home_link.click()
    expect(page).to_have_url(f'{BASE_URL}/')
