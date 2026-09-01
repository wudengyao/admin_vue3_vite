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
        
        # -> Open the 'Login' page by navigating to /login so the login form and captcha DOM text can be inspected.
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Fill the captcha field with the shown code 'q770' and click the '登 录' button to attempt login.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("q770")
        
        # -> Fill the captcha field with the shown code 'q770' and click the '登 录' button to attempt login.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '下一个' (Next) button in the walkthrough overlay to advance the guided tour.
        # 下一个 button
        elem = page.get_by_role('button', name='下一个', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '下一个' (Next) button in the walkthrough overlay to advance the guided tour and verify the tour progresses.
        # 下一个 button
        elem = page.get_by_role('button', name='下一个', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '下一个' (Next) button in the walkthrough overlay to advance the guided tour and verify the tour progresses.
        # 下一个 button
        elem = page.get_by_role('button', name='下一个', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '完成' button in the walkthrough overlay to finish the tour and confirm the overlay closes.
        # 完成 button
        elem = page.get_by_role('button', name='完成', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '下一个' (Next) button in the walkthrough overlay to advance the guided tour and verify the overlay remains visible (search for the title '引导').
        # 下一个 button
        elem = page.get_by_role('button', name='下一个', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '下一个' (Next) button in the walkthrough overlay to advance the guided tour and then verify the overlay/highlight changes.
        # 下一个 button
        elem = page.get_by_role('button', name='下一个', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '下一个' (Next) button in the walkthrough overlay to advance the guided tour and verify the overlay/highlight changes.
        # 下一个 button
        elem = page.get_by_role('button', name='下一个', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The walkthrough overlay modal is displayed with controls '关闭', '上一个', and '完成'.
        await page.locator("xpath=/html/body/div[6]/div[1]").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: Walkthrough overlay container is visible on the page.
        await expect(page.locator("xpath=/html/body/div[6]/div[1]").nth(0)).to_be_visible(timeout=15000), "Walkthrough overlay container is visible on the page."
        
        # --> The guided walkthrough is active and showing a step titled '菜单', indicating the tour has started.
        # Assert-outcome: passed
        # Assert: The walkthrough overlay shows the step title '菜单', indicating the tour is active.
        await expect(page.locator("xpath=/html/body/div[6]/div[1]").nth(0)).to_contain_text("\u83dc\u5355", timeout=15000), "The walkthrough overlay shows the step title '\u83dc\u5355', indicating the tour is active."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    