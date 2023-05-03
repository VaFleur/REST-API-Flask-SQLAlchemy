from application import app
from logger import logger


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    logger.info(f"Start app host={host}, port={port}")
    app.run(host=host, port=port)
    logger.info(f"Stop app host={host}, port={port}")


if __name__ == "__main__":
    run_server()
