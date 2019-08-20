from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, _, _ = date.split('-')
        return (datetime.strptime(date, '%Y-%m-%d') - datetime.strptime(f"{year}-01-01", '%Y-%m-%d')).days + 1
