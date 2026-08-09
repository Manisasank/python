import json
import os
import calendar
from datetime import datetime


EVENTS_FILE = os.path.join(os.path.dirname(__file__), "calendar_events.json")


def build_month_calendar(year, month, first_weekday=calendar.SUNDAY):
    """Return a formatted monthly calendar string."""
    cal = calendar.TextCalendar(first_weekday)
    return cal.formatmonth(year, month)


def build_year_calendar(year, first_weekday=calendar.SUNDAY):
    """Return a formatted yearly calendar string."""
    cal = calendar.TextCalendar(first_weekday)
    return cal.formatyear(year)


def load_events(file_path=EVENTS_FILE):
    """Load saved events from a JSON file."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def save_events(events, file_path=EVENTS_FILE):
    """Save events to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as handle:
        json.dump(events, handle, indent=2)


def add_event(title, date_text, description="", file_path=EVENTS_FILE):
    """Add a new event and return the updated event list."""
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Date must use YYYY-MM-DD format") from exc

    events = load_events(file_path)
    events.append(
        {
            "title": title,
            "date": date_text,
            "description": description,
        }
    )
    save_events(events, file_path)
    return events


def list_events_for_month(year, month, file_path=EVENTS_FILE):
    """Return events that fall within the given month."""
    events = load_events(file_path)
    return [
        event
        for event in events
        if event.get("date", "") and datetime.strptime(event["date"], "%Y-%m-%d").year == year
        and datetime.strptime(event["date"], "%Y-%m-%d").month == month
    ]


def display_events(events):
    """Format events for terminal display."""
    if not events:
        print("No events scheduled.")
        return

    for event in events:
        print(f"- {event['date']}: {event['title']}")
        if event.get("description"):
            print(f"  {event['description']}")


def main():
    print("\n********** Calendar App **********")
    print("1. View a month")
    print("2. View a year")
    print("3. Add an event")
    print("4. View events for a month")
    print("0. Quit")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice in {"0", "quit", "exit"}:
            print("Goodbye!")
            break

        if choice in {"1", "month", "view month"}:
            try:
                year = int(input("Enter a year: ").strip())
                month = int(input("Enter a month (1-12): ").strip())
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if 1 <= month <= 12:
                print(build_month_calendar(year, month))
            else:
                print("Please enter a month from 1 to 12.")

        elif choice in {"2", "year", "view year"}:
            try:
                year = int(input("Enter a year: ").strip())
            except ValueError:
                print("Please enter a valid year.")
                continue
            print(build_year_calendar(year))

        elif choice in {"3", "add", "event"}:
            title = input("Event title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            date_text = input("Date (YYYY-MM-DD): ").strip()
            description = input("Description (optional): ").strip()
            try:
                add_event(title, date_text, description)
            except ValueError as exc:
                print(exc)
            else:
                print("Event saved.")

        elif choice in {"4", "events", "view events"}:
            try:
                year = int(input("Enter a year: ").strip())
                month = int(input("Enter a month (1-12): ").strip())
            except ValueError:
                print("Please enter valid numbers.")
                continue
            display_events(list_events_for_month(year, month))

        else:
            print("Please choose a valid option.")


if __name__ == "__main__":
    main()
