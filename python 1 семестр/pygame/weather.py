import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TELEGRAM_TOKEN = "APLI_KEY" #Thay API TOKEN CỦA BẠN VÀO
OPENWEATHERMAP_API_KEY = "fe8d8c65cf345889139d8e545f57819a" #CÁI NÀY ĐỂ NGUYÊN CŨNG ĐƯỢC

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Xin chào! Tôi là bot dự báo thời tiết. Để biết dự báo, sử dụng lệnh /weather.")

def weather(update: Update, context: CallbackContext) -> None:
    # Lấy địa điểm từ tin nhắn của người dùng
    location = ' '.join(context.args)

    if not location:
        update.message.reply_text("Vui lòng nhập địa điểm. Ví dụ: /weather Hanoi")
        return

    # Gọi API OpenWeatherMap để lấy thông tin thời tiết
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}'
    response = requests.get(weather_url)
    data = response.json()

    if response.status_code == 200:
        # Xử lý dữ liệu và trả lời tin nhắn với thông tin thời tiết
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15  # Chuyển từ Kelvin sang Celsius
        temperature_formatted = "{:.2f}".format(temperature)
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        
        # Mức mưa
        rain = 0
        if 'rain' in data:
            rain = data['rain'].get('1h', 0)

        # Tạo một chuỗi thông tin thời tiết
        weather_info = (
            f"Thời tiết tại {location}:\n"
            f"Trạng thái: {weather_description}\n"
            f"Nhiệt độ: {temperature_formatted} °C\n"
            f"Độ ẩm: {humidity}%\n"
            f"Tốc độ gió: {wind_speed} m/s\n"
            f"Áp suất: {pressure} hPa\n"
            f"Mức mưa (1h): {rain} mm"
        )

        update.message.reply_text(weather_info)
    else:
        update.message.reply_text("Không thể lấy thông tin thời tiết. Vui lòng thử lại sau.")

def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    # Đăng ký các lệnh
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("weather", weather))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()