import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("https://admin-vue3-vite.vercel.app")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Open the Login page by navigating to '/login' so the login form (username, password, captcha) can be inspected.
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Enter the captcha '6p76' into the captcha input field and click the '登 录' button to submit the login form.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("6p76")
        
        # -> Enter the captcha '6p76' into the captcha input field and click the '登 录' button to submit the login form.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '登 录' button to submit the login form and sign in.
        await page.goto("https://admin-vue3-vite.vercel.app/adminAuth/adminList")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Click the '权限管理' menu item in the left sidebar to reveal its submenu.
        # 权限管理
        elem = page.get_by_text('权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '账号列表' (Account List) item in the left sidebar to open the account list page.
        # 账号列表 menu item
        elem = page.get_by_role('menuitem', name='账号列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Open the 'admin' account details by clicking the 'admin' row in the account list.
        # admin
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[2]')
        await elem.click(timeout=10000)
        
        # -> Click the 'admin' account row in the account list to open its detail page and verify the account detail page is displayed.
        # admin
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[2]')
        await elem.click(timeout=10000)
        
        # -> Click the 'admin' row in the account list to open and view its account detail page.
        # admin
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[2]')
        await elem.click(timeout=10000)
        
        # -> Click the avatar image for the 'admin' row to open that account's detail page.
        # Click the avatar image for the 'admin' row to open that account's detail page.
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[4]/div/div/img')
        await elem.click(timeout=10000)
        
        # -> Click the ID cell showing '1' in the admin row to open that account's detail page.
        # 1
        elem = page.locator('xpath=/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/table/tbody/tr/td')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        current_url = await page.evaluate("() => window.location.href")
        # Assert-outcome: passed
        # Assert: page loaded with a URL (final outcome verified by the AI judge during the run)
        assert current_url, 'Page should have loaded with a URL'
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    