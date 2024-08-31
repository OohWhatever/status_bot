embed = discord.Embed(title="STANDOFF365",
                      url="https://range.standoff365.com/",
                      description="Здесь вы можете проверить состояние отраслей на киберполигоне\n\n```\nПеречень отраслей\n```\n____",
                      colour=0xf50000,
                      timestamp=datetime.now())

embed.set_author(name="Cyberrange Status",
                 url="https://range.standoff365.com/",
                 icon_url="https://standoff365.com/favicons/icon.svg")

embed.add_field(name="> **Metal&Tech**",
                value="✅ Металлургический комбинат [Metal&Tech](https://range.standoff365.com/battle/5/industry/17/) работает в штатном порядке",
                inline=False)
embed.add_field(name="> **HighTechEnergy**",
                value="✅ Отрасль электроэнергетики [HighTechEnergy](https://range.standoff365.com/battle/5/industry/38/) работает в штатном порядке",
                inline=False)
embed.add_field(name="> **Банковская система**",
                value="✅ [Банковская отрасль ](https://range.standoff365.com/battle/5/industry/19/) работает в штатном порядке",
                inline=False)
embed.add_field(name="> **NetFusionPro**",
                value="✅ IT-компания [NetFusionPro](https://range.standoff365.com/battle/5/industry/18/) работает в штатном порядке",
                inline=False)

embed.set_image(url="https://standoff365.com/content/uploads/battle2_6c5484b198.png")

embed.set_footer(icon_url="https://standoff365.com/favicons/icon.svg")

await ctx.send(embed=embed)
