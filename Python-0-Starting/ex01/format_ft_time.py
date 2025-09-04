from datetime import datetime


Start_Date = datetime(1970, 1, 1)
Now = datetime.now()


time_diff = Now - Start_Date

Seconds_Ellapse = float(time_diff.total_seconds())


scientific = f"{Seconds_Ellapse:.2e}"
formatted = f"{Seconds_Ellapse:,.4f}"

print(
    f"Seconds since January 1, 1970: {formatted} or {scientific} "
    "in scientific notation"
)
formatted_date = Now.strftime("%b %d %Y")
print(formatted_date)
