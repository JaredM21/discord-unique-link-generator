import discord

token = 'BOT TOKEN' # Put Bot Token Here
client = discord.Client()
print(client)
number_of_links = input('How many links do you want to create? ') 
print(number_of_links)
text_file = open("links.txt", "a")


@client.event 
async def on_ready():
    print(client.guilds[0]) # 0 = Latest Server Joined
    g = client.guilds[0]  # Choose the guild/server you want to use 
    print(g.get_channel(955215848547708948))
    c = g.get_channel(955215848547708948) # Get channel ID
    invites = await discord.abc.GuildChannel.invites(c) # list of all the invites in the server
    print(invites)
    inviteNumber = 0

    while len(invites) < int(number_of_links):
        print('CREATING INVITES')
        for i in range(int(number_of_links)): # Create as many links as needed
            i = await discord.abc.GuildChannel.create_invite(c, max_uses=1, max_age=0, unique=True) # Create the invite link
            inviteNumber += 1
            print("Invite Number " + str(inviteNumber) + ': ' + str(i))
            n = text_file.write(str(i)+',\n')
        break

    text_file.close()
    print('Finished. Exiting soon...')
    exit()

client.run(token)