import discord
import asyncio
import random

# Токен вашего бота (его нужно получить с Discord Developer Portal)
TOKEN = ''

# Создание экземпляра клиента
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Глобальная переменная для хранения ссылки на сообщение
embed_message = None

# Функция для обновления embed-сообщения
async def update_embed():
    global embed_message
    while True:
        if embed_message:
            # Создаем новое embed-сообщение с обновленным содержимым
            new_embed = discord.Embed(
                title="Обновляемое сообщение",
                description=f"Случайное число: {random.randint(1, 100)}",
                color=discord.Color.blue()
            )
            await embed_message.edit(embed=new_embed)

        # Ждем 30 секунд перед следующим обновлением
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f'Мы вошли как {client.user}')

    # Получаем канал по его ID, где будет отправлено embed-сообщение
    channel = client.get_channel(1279509509135536330)

    # Создаем первоначальное embed-сообщение
    embed = discord.Embed(
        title="Обновляемое сообщение",
        description="Это сообщение будет обновляться каждые 30 секунд.",
        color=discord.Color.blue()
    )

    # Отправляем embed-сообщение и сохраняем ссылку на него
    global embed_message
    embed_message = await channel.send(embed=embed)

    # Запускаем фоновую задачу для обновления embed-сообщения
    client.loop.create_task(update_embed())

# Запускаем бота
client.run(TOKEN)