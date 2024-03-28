import Nametime as Nametime
from datetime import datetime, timedelta


async def dateCount(start_date, end_date):
    try:
        full_date = []
        start_date = start_date.split("_")
        end_date = end_date.split("_")

        for i in range(len(start_date)):
            start_date[i] = int(start_date[i])

        for j in range(len(end_date)):
            end_date[j] = int(end_date[j])

        if start_date and end_date:

            if (
                start_date[0] > 31
                or start_date[0] <= 0
                or end_date[0] > 31
                or end_date[0] <= 0
                or start_date[1] > 12
                or start_date[1] <= 0
                or end_date[1] > 12
                or end_date[1] <= 0
            ):
                return "invalid date input"

            elif start_date[1] in [1, 3, 5, 7, 8, 10, 12] and start_date[0] > 31:
                return "invalid date input"

            elif start_date[1] in [4, 6, 9, 11] and start_date[0] > 30:
                return "invalid date input"

            elif end_date[1] in [1, 3, 5, 7, 8, 10, 12] and end_date[0] > 31:
                return "invalid date input"

            elif end_date[1] in [4, 6, 9, 11] and end_date[0] > 30:
                return "invalid date input"

            elif start_date[2] % 4 == 0 and start_date[0] > 29:
                return "invalid date input"

            elif start_date[2] % 4 != 0 and start_date[0] > 28:
                return "invalid date input"

            elif end_date[2] % 4 == 0 and end_date[0] > 29:
                return "invalid date input"

            elif end_date[2] % 4 != 0 and end_date[0] > 28:
                return "invalid date input"

            else:
                if end_date[2] - start_date[2] < 0:
                    return "invalid date input"
                elif (
                    end_date[2] - start_date[2] == 0 and end_date[1] - start_date[1] < 0
                ):
                    return "invalid date input"
                elif (
                    end_date[1] - start_date[1] == 0 and end_date[0] - start_date[0] < 0
                ):
                    return "invalid date input"

                else:
                    start_date = datetime(start_date[2], start_date[1], start_date[0])
                    end_date = datetime(end_date[2], end_date[1], end_date[0])

                    current_date = start_date
                    date_list = []
                    modified_date = []

                    while current_date <= end_date:
                        date_list.append(current_date.strftime("%Y-%m-%d"))
                        current_date += timedelta(days=1)
                        
                    for dates in date_list:
                        month = dates[5:7]
                        month = Nametime.nameMonth(month)
                        year = dates[0:4]
                        day = dates[8:]

                        modified_date.append(f'{day}_{month}_{year}')
                    
                    return modified_date

        else:
            return

    except Exception as e:
        print(f"error : {e}")
        return "error"
