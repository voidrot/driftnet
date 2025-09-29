import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect


@pytest.mark.playwright
def test_homepage_flow(page: Page, live_server):
    page.goto(live_server + '/')
    # Use exact match for the main heading to avoid strict mode violation
    expect(page.get_by_role('heading', name='driftnet', exact=True)).to_be_visible()
    expect(page.get_by_text('Your EVE Online Intelligence Dashboard')).to_be_visible()
    expect(page.get_by_role('link', name='Sign Up')).to_be_visible()
    expect(page.get_by_text('EVE API Integration')).to_be_visible()
    expect(page.get_by_text('zKillboard Insights')).to_be_visible()
    expect(page.get_by_text('Decision Support')).to_be_visible()
    expect(page.get_by_text('Get Started')).to_be_visible()
    expect(page.get_by_text('How It Works')).to_be_visible()
    expect(page.get_by_text('What driftnet Can Do')).to_be_visible()


@pytest.mark.playwright
def test_landing_page_features(page: Page, live_server):
    page.goto(live_server + '/')
    expect(
        page.get_by_text(
            'Connect your EVE Online account and view real-time character, corporation, and alliance data.'
        )
    ).to_be_visible()
    expect(
        page.get_by_text(
            'Analyze killmails, ship losses, and PvP stats with data from zKillboard.'
        )
    ).to_be_visible()
    expect(
        page.get_by_text(
            'Get actionable intelligence for fleet ops, market moves, and strategic planning.'
        )
    ).to_be_visible()
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
        page.get_by_text(
            "4. Make informed decisions with driftnet's intelligence tools."
        )
    ).to_be_visible()
