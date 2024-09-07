import discord
import asyncio
import random
from datetime import datetime

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
        try:
            if embed_message:
                # Создаем новое embed-сообщение с обновленным содержимым
                new_embed = discord.Embed(
                    title="STANDOFF365",
                    url="https://range.standoff365.com/",
                    description="Здесь вы можете проверить состояние отраслей на киберполигоне\n\n```\nПеречень отраслей\n```\n____",
                    colour=0xf50000,
                    timestamp=datetime.now()
                )

                new_embed.set_author(
                    name="Cyberrange Status",
                    url="https://range.standoff365.com/",
                    icon_url="https://standoff365.com/favicons/icon.svg"
                )

                # Пример изменения статуса: случайное изменение статуса отрасли
                statuses = ["🟢 Работает в штатном порядке |","🟢 Работает в штатном порядке |", "🟡 Наблюдаются некоторые проблемы |", "🔴 Команда уже работает над сбоем | "]
                new_embed.add_field(
                    name="> **Metal&Tech**",
                    value=f"{random.choice(statuses)} [Перейти](https://range.standoff365.com/battle/5/industry/17/)",
                    inline=False
                )
                new_embed.add_field(
                    name="> **HighTechEnergy**",
                    value=f"{random.choice(statuses)} [Перейти](https://range.standoff365.com/battle/5/industry/38/)",
                    inline=False
                )
                new_embed.add_field(
                    name="> **Банковская система**",
                    value=f"{random.choice(statuses)} [Перейти](https://range.standoff365.com/battle/5/industry/19/)",
                    inline=False
                )
                new_embed.add_field(
                    name="> **NetFusionPro**",
                    value=f"{random.choice(statuses)} [Перейти](https://range.standoff365.com/battle/5/industry/18/)",
                    inline=False
                )

                new_embed.set_image(url="https://standoff365.com/content/uploads/battle2_6c5484b198.png")
                new_embed.set_footer(icon_url="https://standoff365.com/favicons/icon.svg")

                # Обновляем сообщение
                await embed_message.edit(embed=new_embed)

            # Ждем 30 секунд перед следующим обновлением
            await asyncio.sleep(30)
        
        except Exception as e:
            # Логирование ошибки, чтобы отслеживать проблемы
            print(f"Ошибка при обновлении embed-сообщения: {e}")
            await asyncio.sleep(10)  # Подождем 10 секунд перед повторной попыткой

@client.event
async def on_ready():
    print(f'Мы вошли как {client.user}')

    # Получаем канал по его ID, где будет отправлено embed-сообщение
    channel = client.get_channel(1280596041422606336)

    # Проверяем, найден ли канал
    if channel is None:
        print(f"Ошибка: Канал с ID {1280596041422606336} не найден. Проверьте ID канала и права доступа.")
        return

    # Создаем первоначальное embed-сообщение
    embed = discord.Embed(
        title="STANDOFF365",
        url="https://range.standoff365.com/",
        description="Здесь вы можете проверить состояние отраслей на киберполигоне\n\n```\nПеречень отраслей\n```\n____",
        colour=0xf50000,
        timestamp=datetime.now()
    )

    embed.set_author(
        name="Cyberrange Status",
        url="https://range.standoff365.com/",
        icon_url="https://standoff365.com/favicons/icon.svg"
    )

    embed.add_field(
        name="> **Metal&Tech**",
        value="✅ Металлургический комбинат [Metal&Tech](https://range.standoff365.com/battle/5/industry/17/) работает в штатном порядке",
        inline=False
    )
    embed.add_field(
        name="> **HighTechEnergy**",
        value="✅ Отрасль электроэнергетики [HighTechEnergy](https://range.standoff365.com/battle/5/industry/38/) работает в штатном порядке",
        inline=False
    )
    embed.add_field(
        name="> **Банковская система**",
        value="✅ [Банковская отрасль ](https://range.standoff365.com/battle/5/industry/19/) работает в штатном порядке",
        inline=False
    )
    embed.add_field(
        name="> **NetFusionPro**",
        value="✅ IT-компания [NetFusionPro](https://range.standoff365.com/battle/5/industry/18/) работает в штатном порядке",
        inline=False
    )

    embed.set_image(url="https://standoff365.com/content/uploads/battle2_6c5484b198.png")
    embed.set_footer(icon_url="https://standoff365.com/favicons/icon.svg")

    # Отправляем embed-сообщение и сохраняем ссылку на него
    global embed_message
    embed_message = await channel.send(embed=embed)

    # Запускаем фоновую задачу для обновления embed-сообщения
    client.loop.create_task(update_embed())

# Запускаем бота
client.run(TOKEN)
