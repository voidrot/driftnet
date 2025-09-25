import pytest
from playwright.sync_api import Page, expect

@pytest.mark.playwright
def test_terms_page_content(page: Page, live_server):
    page.goto(live_server + '/terms')
    expect(page.get_by_role('heading', name='Terms of Service', exact=True)).to_be_visible()
    expect(page.get_by_text('Last updated:')).to_be_visible()
    expect(page.get_by_text('1. Acceptance of Terms')).to_be_visible()
    expect(page.get_by_text('2. Using the Service')).to_be_visible()
    expect(page.get_by_text('3. Accounts and Registration')).to_be_visible()
    expect(page.get_by_text('4. Content')).to_be_visible()
    expect(page.get_by_text('5. Prohibited Conduct')).to_be_visible()
    expect(page.get_by_text('6. Fees and Payments')).to_be_visible()
    expect(page.get_by_text('7. Termination')).to_be_visible()
    expect(page.get_by_text('8. Disclaimers')).to_be_visible()
    expect(page.get_by_text('9. Limitation of Liability')).to_be_visible()
    expect(page.get_by_text('10. Governing Law')).to_be_visible()
    expect(page.get_by_text('11. Changes to Terms')).to_be_visible()
    expect(page.get_by_text('12. Contact')).to_be_visible()
    expect(page.get_by_text('If you have questions about these Terms, contact us at support@voidlink.example.')).to_be_visible()
