
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Launch Chrome browser
    browser = p.chromium.launch(headless=False)

    # Open a new page
    page = browser.new_page()

    try:
        # Open Cricbuzz live scores
        print("Opening Cricbuzz...")

        page.goto(
            "https://www.cricbuzz.com/live-cricket-scores",
            wait_until="domcontentloaded",
            timeout=60000
        )

        # Wait for page loading
        page.wait_for_timeout(5000)

        # Get page content
        score = page.locator("body").inner_text()

        # Display score
        print("\nCRICKET LIVE SCORE")
        print("=" * 50)
        print(score[:5000])

        # Save screenshot
        page.screenshot(
            path="score.png",
            full_page=True
        )

        print("\nScreenshot saved successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        browser.close()
        print("Browser closed.")
