# @Author: Pakzat
import asyncio
import aiomysql
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# TG BOT变量
TOKEN = "[Your TG BOT TOKEN]"
# MySQL变量
async def create_pool():
    # 创建连接池
    pool = await aiomysql.create_pool(
        host='[Your MySQL Server Host]',
        port=[Port],
        user='[User Name]',
        password='[Password]',
        db='[Database Name]',
        autocommit=True
    )
    return pool

async def search_keyword_in_tables(pool, keyword):
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SHOW TABLES")
            tables = await cursor.fetchall()

            results = []

            for table in tables:
                table_name = table[0]

                await cursor.execute(f"SHOW COLUMNS FROM {table_name}")
                columns = await cursor.fetchall()

                query = f"SELECT * FROM {table_name} WHERE "
                conditions = []
                for column in columns:
                    column_name = column[0]
                    conditions.append(f"{column_name} LIKE '%{keyword}%'")

                query += " OR ".join(conditions)

                await cursor.execute(query)

                query_results = await cursor.fetchall()

                results.extend(query_results)

            return results

async def start_command(message: types.Message):
    if message.get_args():
        reply_message = '有参数，参数是：' + message.get_args()
        await message.answer(reply_message)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='按钮1', callback_data='button1'),
                     types.InlineKeyboardButton(text='按钮2', callback_data='button2'),
                     types.InlineKeyboardButton(text='按钮3', callback_data='button3'),
                     types.InlineKeyboardButton(text='按钮4', callback_data='button4'),
                     types.InlineKeyboardButton(text='按钮5', callback_data='button5'),
                     types.InlineKeyboardButton(text='按钮6', callback_data='button6'))
        await message.answer('你输入了特定命令/start', reply_markup=keyboard)

async def search_command(message: types.Message):
    if message.get_args():
        keyword = message.get_args()
        await message.answer('正在查询，请稍候...')
        results = await search_keyword_in_tables(pool, keyword)
        if results:
            reply_message = '查询结果：\n'
            for row in results[:100]:
                reply_message += str(row) + '\n'
                if len(reply_message) >= 4000:  # 设置消息长度限制
                    await message.answer(reply_message)
                    reply_message = ''
            if reply_message:
                await message.answer(reply_message)
        else:
            await message.answer('没有找到匹配的结果')
    else:
        await message.answer('请提供关键词参数')

async def button_callback_handler(query: types.CallbackQuery):
    await query.answer()

    if query.data == 'button1':
        await query.message.answer('你点击了按钮1')
    elif query.data == 'button2':
        await query.message.answer('你点击了按钮2')
    elif query.data == 'button3':
        await query.message.answer('你点击了按钮3')
    elif query.data == 'button4':
        await query.message.answer('你点击了按钮4')
    elif query.data == 'button5':
        await query.message.answer('你点击了按钮5')
    elif query.data == 'button6':
        await query.message.answer('你点击了按钮6')



loop = asyncio.get_event_loop()
pool = loop.run_until_complete(create_pool())

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(search_command, commands=['search'])
dp.register_callback_query_handler(button_callback_handler)

try:
    loop.run_until_complete(dp.start_polling())
except KeyboardInterrupt:
    pass
finally:
    loop.run_until_complete(bot.close())
    loop.run_until_complete(dp.storage.close())
    loop.run_until_complete(dp.storage.wait_closed())
    loop.close()
