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
        
        # -> Open the login page by navigating to /login so the username/password/captcha fields and the 'code-img' text are visible.
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Enter password '123456', type the captcha '6ksn' into the captcha field, and click the '登 录' button to submit the login form.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Enter password '123456', type the captcha '6ksn' into the captcha field, and click the '登 录' button to submit the login form.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("6ksn")
        
        # -> Enter password '123456', type the captcha '6ksn' into the captcha field, and click the '登 录' button to submit the login form.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Open the role list page and open a role's 'Assign Permissions' (分配权限) dialog so the permission tree can be inspected.
        await page.goto("https://admin-vue3-vite.vercel.app/adminAuth/getRoleList")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Scroll down the Role List page and locate the '分配权限' (Assign Permissions) control for a role so the permission-assignment dialog can be opened.
        await page.mouse.wheel(0, 300)
        
        # -> Click the '权限管理' menu item in the left sidebar to open its submenu.
        # 权限管理
        elem = page.get_by_text('权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '角色列表' (Role List) menu item in the left sidebar to open the role list page.
        # 角色列表 menu item
        elem = page.get_by_role('menuitem', name='角色列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '配置权限' button (label text) in the first role row to open the Assign Permissions dialog.
        # 配置权限 button
        elem = page.get_by_text('1', exact=True).locator("xpath=ancestor-or-self::*[.//button][1]").get_by_role('button', name='配置权限', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The Assign Permissions dialog is visible with the title '配置权限'.
        await page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: Verifies the Assign Permissions dialog is present and visible.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div").nth(0)).to_be_visible(timeout=15000), "Verifies the Assign Permissions dialog is present and visible."
        
        # --> The permission tree is displayed in the dialog and contains the item '权限管理'.
        # Assert-outcome: passed
        # Assert: Verifies a permission tree item labeled '权限管理' is visible in the dialog.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div[1]/div[1]/span").nth(0)).to_have_text("\u6743\u9650\u7ba1\u7406", timeout=15000), "Verifies a permission tree item labeled '\u6743\u9650\u7ba1\u7406' is visible in the dialog."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    