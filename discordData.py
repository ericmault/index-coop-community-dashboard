import discord
import pandas as pd
import json
from datetime import datetime
from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    columns = []
    dic = {}

    for guild in client.guilds:
        # for member in guild.members:
            # print(member)
            # print(member.roles)
            # print('-----')
        for role in guild.roles:
            mmm = []
            columns.append(role.name)

            # print("---"+str(role)+"---")
            
            for member in role.members:

                # df[role.name].append(member.name)
                mmm.append(member.name)
                # dic[role.name] = member.name
                # print(member.name)
            columns.append(mmm)
            dic[role.name] = mmm

    print(dic)
    print('--')
    df = pd.DataFrame.from_dict(dic, orient='index')
    print(df)
    
    dft = df.T
    print(dft)
    
    dft.to_csv('role_audit.csv',index=False)
client.run(DISCORD_TOKEN)


