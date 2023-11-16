#7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#    Примеры:
#    1234565 seconds = 14:6:56:5
user_input = int(input('Seconds: '))

seconds = user_input

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

remaining_seconds = seconds


formatted_time = f"{days}:{hours}:{minutes}:{remaining_seconds}"

print(f"{user_input} seconds = {formatted_time}")