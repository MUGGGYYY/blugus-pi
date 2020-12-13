from datetime import time, datetime, date
from time import sleep
from pathlib import Path

START: time = time(6, 0, 0)
STOP: time = time(18, 0, 0)
PICTURES_PER_DAY: int = 730
IMAGES_DIR = Path() / "images"


def capture_image() -> None:
    """ Captures image from PI Camera """
    file_name = IMAGES_DIR / f"{datetime.now()}.jpg"
    print(f"Capturing image {file_name}")


DATE_STOP = datetime.combine(date.min, STOP)
DATE_START = datetime.combine(date.min, START)
INTERVAL = (DATE_STOP - DATE_START) / PICTURES_PER_DAY

next_capture_date: datetime = datetime.now()


print(f"Start: {START}")
print(f"Stop: {STOP}")
print(f"Interval: {INTERVAL}")


def wait_for_date(the_date: datetime):
    print(f"Next Capture: {the_date}")
    while the_date > datetime.now():
        sleep(0.001)


def is_in_capture_range():
    return START <= datetime.now().time() <= STOP


def wait_for_capture_interval():
    global next_capture_date
    next_capture_date += INTERVAL
    wait_for_date(next_capture_date)


if __name__ == "__main__":
    IMAGES_DIR.mkdir(exist_ok=True)
    assert START < STOP, "Start time must be before stop time"
    while True:
        wait_for_capture_interval()
        if is_in_capture_range():
            capture_image()
