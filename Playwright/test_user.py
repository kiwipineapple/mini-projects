import os
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError

os.chdir(Path(__file__).parent)

# Tipp: Use pytest for clear structure
def check_osapiens_web():
    with sync_playwright() as p:
        try:
            browser = p.firefox.launch(headless=False)

            page = browser.new_page()

            page.goto("https://careers.osapiens.com/")
            # Tipp: Use Setup function to open browser before each test case

            # Prints the number of open jobs
            page.wait_for_selector("a.hide-sm-block.text-bold")
            jobs = page.locator("a.hide-sm-block.text-bold")
            count = jobs.count()
            print(f'Number of open jobs: {count}')
            
            # Checks and fails the test if none of the job titles contains “Quality”
            found = False
            for i in range(count):
                title_text = jobs.nth(i).inner_text()
                if "Quality" in title_text:
                    found = True
                    break

            assert found, "No job title contains 'Quality'"


        except TimeoutError:
            print("Page elemens took too long time to be loaded")

        except Exception as e:
            print(f"Some Error occured: {e}")

        finally:
            browser.close()

if __name__ == "__main__":
    check_osapiens_web()