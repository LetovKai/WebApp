from aiogram import Bot, Dispatcher, executor, types
import cfg
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(cfg.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup=types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть страницу', web_app=WebAppInfo(url='https://www.apple.com')))
    await message.answer('Aloha, man!', reply_markup=markup)

executor.start_polling(dp)