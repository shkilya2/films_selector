from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


inline_kb_1 = InlineKeyboardMarkup(row_width=2)


inline_btn_1 =InlineKeyboardButton('Комедии 😂', callback_data='btn Комедии')
inline_btn_2 = InlineKeyboardButton('Мультфильмы 🏰', callback_data='btn Мультфильмы')
inline_btn_3 = InlineKeyboardButton('Детективы 🔎', callback_data='btn Детективы')
inline_btn_4 = InlineKeyboardButton('Документальные 📚', callback_data='btn Документальные')
inline_btn_5 = InlineKeyboardButton('Драмы 🎭', callback_data='btn Драмы')
inline_btn_6 = InlineKeyboardButton('Ужасы 🔪', callback_data='btn Ужасы')
inline_btn_7 = InlineKeyboardButton('Фантастика 🪐', callback_data='btn Фантастика')
inline_btn_8 = InlineKeyboardButton('Фэнтези ✨', callback_data='btn Фэнтези')
inline_btn_9 = InlineKeyboardButton('Боевики 💣', callback_data='btn Боевики')
inline_btn_10 = InlineKeyboardButton('Приключения 🪂', callback_data='btn Приключения')
inline_kb_1.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9, inline_btn_10)
inline_kb_1.add(InlineKeyboardButton('Скрыть ✖️', callback_data='Скрыть'))
