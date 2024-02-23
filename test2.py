import discord

# Discord botunuzun token'ını buraya ekleyin
TOKEN = 'MTIwNTgxOTU3NjI3MzczMTYzNA.G-9p4T.7q9_u2uzObNmPNU_yJwXM_GhUQuDzy3nUiFT2U'

# Discord botunuzun Client'ını oluşturun
    
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Eğer mesaj bir webhook mesajı ise
    if message.webhook_id:
        print(f'Received a webhook message: {message.content}')

# Botu çalıştırın
client.run(TOKEN)