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
        
        # -> Open the login page (navigate to '/login') and wait for the login form to appear
        await page.goto("https://admin-vue3-vite.vercel.app/login")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Submit the login form by clicking the '登 录' button, after filling password and the shown captcha text.
        # 请输入密码 password field
        elem = page.get_by_placeholder('请输入密码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("123456")
        
        # -> Submit the login form by clicking the '登 录' button, after filling password and the shown captcha text.
        # 图形验证码 text field
        elem = page.get_by_placeholder('图形验证码', exact=True)
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("30dt")
        
        # -> Submit the login form by clicking the '登 录' button, after filling password and the shown captcha text.
        # 登 录 button
        elem = page.get_by_role('button', name='登 录', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '权限管理' sidebar item to open the permissions/roles UI.
        # 权限管理
        elem = page.get_by_text('权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '角色列表' menu item to open the role list page.
        # 角色列表
        elem = page.get_by_text('角色列表', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '配置权限' button for the '主管' role to open the permission editor.
        # 配置权限 button
        elem = page.get_by_text('1', exact=True).locator("xpath=ancestor-or-self::*[.//button][1]").get_by_role('button', name='配置权限', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '权限管理' permission checkbox in the 配置权限 dialog, then click the '确定' button to save the updated permissions.
        # 权限管理
        elem = page.get_by_role('treeitem', name='权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '权限管理' permission checkbox in the 配置权限 dialog, then click the '确定' button to save the updated permissions.
        # 确定 button
        elem = page.get_by_role('button', name='确定', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '配置权限' button for the '主管' role to open the permission editor.
        # 配置权限 button
        elem = page.get_by_text('1', exact=True).locator("xpath=ancestor-or-self::*[.//button][1]").get_by_role('button', name='配置权限', exact=True)
        await elem.click(timeout=10000)
        
        # -> In the open '配置权限' dialog, toggle the '权限管理' checkbox then click the '确定' button to save the role's permissions.
        # 权限管理
        elem = page.get_by_role('treeitem', name='权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> In the open '配置权限' dialog, toggle the '权限管理' checkbox then click the '确定' button to save the role's permissions.
        # 确定 button
        elem = page.get_by_role('button', name='确定', exact=True)
        await elem.click(timeout=10000)
        
        # -> Open the '配置权限' dialog for the '主管' role by clicking the '配置权限' button in that role's table row.
        # 配置权限 button
        elem = page.get_by_text('1', exact=True).locator("xpath=ancestor-or-self::*[.//button][1]").get_by_role('button', name='配置权限', exact=True)
        await elem.click(timeout=10000)
        
        # -> Toggle the '权限管理' checkbox in the open 配置权限 dialog and click the '确定' button to save the updated permissions.
        # 权限管理
        elem = page.get_by_role('treeitem', name='权限管理', exact=True)
        await elem.click(timeout=10000)
        
        # -> Toggle the '权限管理' checkbox in the open 配置权限 dialog and click the '确定' button to save the updated permissions.
        # 确定 button
        elem = page.get_by_role('button', name='确定', exact=True)
        await elem.click(timeout=10000)
        
        # -> Click the '配置权限' button for the '主管' role to reopen the permission editor and inspect the permission checkbox state.
        # 配置权限 button
        elem = page.get_by_text('1', exact=True).locator("xpath=ancestor-or-self::*[.//button][1]").get_by_role('button', name='配置权限', exact=True)
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> No visible success confirmation appeared after saving the role's permissions.
        # Assert-outcome: failed
        # Assert: Expected the permissions dialog to display a success message containing '操作成功'.
        await expect(page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/div[3]").nth(0)).to_contain_text("\u64cd\u4f5c\u6210\u529f", timeout=15000), "Expected the permissions dialog to display a success message containing '\u64cd\u4f5c\u6210\u529f'."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    