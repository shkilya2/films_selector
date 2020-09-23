import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode
import functions
import keyboard as kb
import pandas
import db

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['genre'])
async def process_command_1(message: types.Message):
    await message.reply("Популярные жанры", reply_markup=kb.inline_kb_1)


@dp.callback_query_handler(text_contains='btn')
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    genre = callback_query.data.split(' ')[-1]
    movie = functions.select_genre(genre)
    msg = text(bold(movie.title), f'Описание: {movie.description}...', f'Год: {movie.year}', f'Страна: {movie.country}', f'Жанр: {movie.genre}', f'Время: {movie.runtime} минуты', f'Режисер: {movie.film_director}', f'Актеры: {movie.cast}', sep='\n')
    await bot.send_photo(callback_query.from_user.id, photo=movie.img_url, parse_mode=ParseMode.MARKDOWN, caption=msg)

@dp.callback_query_handler(text='Скрыть')
async def cancel(call: types.CallbackQuery):
    await call.message.edit_reply_markup()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f'Привет, {message.chat.first_name}!\nИспользуй /help, '
                        'чтобы узнать список доступных команд!')



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/randommovie - кинь 🎲 или используй эту команду и я выберу тебе фильм 😊', '/genre - только выбери жанр и я предложу фильм 🍿', 
               'Просто напиши название фильма и получи описание🎬 Или имена актёров, режиссёров, чтобы узнать фильмографию', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=ContentType.DICE)
@dp.message_handler(commands=['randommovie'])
async def process_start_command(message: types.Message):
    movie = functions.search_random_movie()
    print("RANDOM!!!", movie.title)
    msg = text(bold(movie.title), f'Описание: {movie.description}...', f'Год: {movie.year}', f'Страна: {movie.country}', f'Жанр: {movie.genre}', f'Время: {movie.runtime} минуты', f'Режисер: {movie.film_director}', f'Актеры: {movie.cast}', sep='\n')
    await bot.send_photo(chat_id=message.from_user.id, photo=movie.img_url, parse_mode=ParseMode.MARKDOWN, caption=msg)


@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text:
        db.add_message(
            user_id=message.from_user.id,
            text=message.text,
            time=message.date,
            name=message.chat.first_name)
    try:
        movies, length, titles = functions.find(message.text)
        if length > 0:
            if length > 5:
                k = 5
            else:
                k = length
            for i in range(k):
                movie = movies.iloc[i]
                msg = text(bold(movie.title), f'Описание: {movie.description}...', f'Год: {movie.year}', f'Страна: {movie.country}', f'Жанр: {movie.genre}', f'Время: {movie.runtime} минуты', f'Режисер: {movie.film_director}', f'Актеры: {movie.cast}', sep='\n')
                await bot.send_photo(chat_id=message.from_user.id, photo=movie.img_url, parse_mode=ParseMode.MARKDOWN, caption=msg)
        if length > 5:
            if length > 50:
                length = 50
            await bot.send_message(message.from_user.id, bold('Я также нашел по вашему запросу:'), parse_mode=ParseMode.MARKDOWN)
            for i in range(5, length):
                await bot.send_message(message.from_user.id, titles.iloc[i])
        if length == 0:
            await bot.send_message(message.from_user.id, 'К сожалению, я ничего не нашел по вашему запросу. Проверьте правильность написания 😌😌😌')
    except:
        await bot.send_message(message.from_user.id, 'К сожалению, я ничего не нашел по вашему запросу. Проверьте правильность написания 😌😌😌')
   




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




