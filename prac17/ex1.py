from datetime import date

class UkrainianCalendar:
    def get_holiday_list(self):
        return [
            date(2025, 1, 1),   # Новий рік
            date(2025, 1, 7),   # Різдво
            date(2025, 3, 8),   # Міжнародний жіночий день
            date(2025, 4, 20),  # Великдень (умовно)
            date(2025, 5, 1),   # День праці
            date(2025, 6, 28),  # День Конституції
            date(2025, 8, 24),  # День Незалежності
        ]

    def is_working_day(self, check_date):
        holidays = self.get_holiday_list()
        return check_date.weekday() < 5 and check_date not in holidays
