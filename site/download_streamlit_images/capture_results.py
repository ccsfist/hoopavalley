import os
import time
from playwright.sync_api import sync_playwright

# Dashboard URLs from your MkDocs exercise result pages
DASHBOARDS = {
    "HVTstorm_results.png": "https://twowaydisplay.streamlit.app/?game=disasterlistplaceholder&view=all&present=1&embed=true",
    "HVTalert_results.png": "https://twowaydisplay.streamlit.app/?game=Flood&view=all&present=1&embed=true",
    "HVTsafe_results.png": "https://twowaydisplay.streamlit.app/?game=Safe&view=all&present=1&embed=true",
    "HVTcoordinate_results.png": "https://twowaydisplay.streamlit.app/?game=Coordinate&view=all&present=1&embed=true",
}

OUTPUT_DIR = "streamlit_screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def wait_for_streamlit_ready(page, timeout_ms=90000):
    deadline = time.time() + (timeout_ms / 1000.0)
    app_frame = None

    while time.time() < deadline:
        # 1. Wake the app if Streamlit Community Cloud put it to sleep
        for frame in page.frames:
            try:
                wake_btn = frame.locator('button:has-text("Yes, get this app back up!")')
                if wake_btn.count() > 0 and wake_btn.first.is_visible():
                    print("  App is asleep — clicking wake-up button...")
                    wake_btn.first.click()
                    time.sleep(5)
            except Exception:
                pass

        # 2. Look for the Streamlit container in both the main page and nested iframes
        for frame in page.frames:
            try:
                container = frame.locator('[data-testid="stAppViewContainer"], .stApp')
                if container.count() > 0 and container.first.is_visible():
                    app_frame = frame
                    break
            except Exception:
                pass

        if app_frame is not None:
            break
        time.sleep(1)

    if app_frame is None:
        raise TimeoutError("Timed out waiting for Streamlit app container in main page or iframes.")

    # 3. Wait for Streamlit's "Running..." status and loading skeletons to finish
    try:
        app_frame.locator('[data-testid="stStatusWidget"]').wait_for(
            state="detached", timeout=30000
        )
    except Exception:
        pass

    try:
        app_frame.locator('[data-testid="stSkeleton"]').first.wait_for(
            state="detached", timeout=20000
        )
    except Exception:
        pass

    # 4. Extra buffer for charts and tables to finish rendering
    time.sleep(4)


def capture_dashboards():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            device_scale_factor=2,
        )
        page = context.new_page()

        for filename, url in DASHBOARDS.items():
            print(f"Loading {filename}...")
            output_path = os.path.join(OUTPUT_DIR, filename)
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                wait_for_streamlit_ready(page, timeout_ms=90000)
                page.screenshot(path=output_path, full_page=False)
                print(f"Saved -> {output_path}")
            except Exception as exc:
                debug_path = os.path.join(OUTPUT_DIR, f"debug_{filename}")
                page.screenshot(path=debug_path, full_page=False)
                print(f"Error capturing {filename}: {exc}")
                print(f"Saved debug screenshot -> {debug_path}")

        browser.close()


if __name__ == "__main__":
    capture_dashboards()
