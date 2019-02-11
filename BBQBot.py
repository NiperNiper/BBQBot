import discord

client = discord.Client()

@client.event
async def on_ready():
    print("login")

    print(client.user.name)

    print(client.user.id)

    print("------------------")

    await client.change_presence(game=discord.Game(name='BBQ 봇 대기중', type=0))


@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요")

client.run('NTQ0NDE2NjgwNjYzODQyODI1.D0KzEA.SupiC3dkUv_ECPQu5LxpsUPAkLw')


