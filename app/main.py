import argparse
import threading
from typing import Optional

import uvicorn
import webview
from loguru import logger

from app import app


DEFAULT_TITLE = "PyWebview App"
DEFAULT_DEV_FRONTEND = "http://localhost:5173"


class Client:
    """Coordinate FastAPI server and webview window."""

    def __init__(self, host: str = "0.0.0.0", port: int = 8000, mode: str = "static", frontend_url: Optional[str] = None):
        self.host = host
        self.port = port
        self.mode = mode
        self.frontend_url = frontend_url or self._default_frontend_url()
        self.app = app

    def _default_frontend_url(self) -> str:
        if self.mode == "dev":
            return DEFAULT_DEV_FRONTEND
        return f"http://localhost:{self.port}"

    def _run_server(self) -> None:
        logger.info("Starting FastAPI on http://{}:{} (ws://{}:{}/ws)", self.host, self.port, self.host, self.port)
        uvicorn.run(self.app, host=self.host, port=self.port)

    def start_server(self) -> None:
        """Only run the FastAPI server."""
        self._run_server()

    def start_webview(self) -> None:
        """Start FastAPI server in a background thread, then open the webview window."""
        threading.Thread(target=self._run_server, daemon=True).start()

        if self.mode == "dev":
            logger.info("Dev mode: start the Vue dev server separately (e.g. `npm run dev -- --host --port 5173`).")
        logger.info("Webview will load frontend [{}] from {}", self.mode, self.frontend_url)

        webview.create_window(DEFAULT_TITLE, url=self.frontend_url, maximized=True, resizable=True)
        webview.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run AmberDay desktop app")
    parser.add_argument("--server", action="store_true", help="Only start backend server")
    parser.add_argument("--host", default="0.0.0.0", help="Backend listen address")
    parser.add_argument("--port", type=int, default=8000, help="Backend listen port")
    parser.add_argument(
        "--mode",
        choices=["static", "dev"],
        default="static",
        help="static: load built assets; dev: point to Vue dev server",
    )
    parser.add_argument(
        "--frontend-url",
        dest="frontend_url",
        help="Override frontend URL (default: static=http://localhost:{port}, dev=http://localhost:5173)",
    )

    args = parser.parse_args()
    client = Client(host=args.host, port=args.port, mode=args.mode, frontend_url=args.frontend_url)

    if args.server:
        client.start_server()
    else:
        client.start_webview()
