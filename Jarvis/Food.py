import discord

class Food:
    foodsList = ['Hamburguer','Pizza','Cinnamon Rolls','Lasagna']
    async def foods(self,client, message): 
        cmd = message.content.split()
        
        if 'add' in message.content:
            add = cmd[cmd.index('add')+1] 
            if add is not None and add not in Food.foodsList:
                Food.foodsList.append(add)
            else:
                embed = discord.Embed(title="Foods",description= "No food to add or food already added!",color=0xa69ea8)
                await message.channel.send(embed=embed)
        else:
            d = ''
            for f in Food.foodsList: d+=f+"\n"
            embed = discord.Embed(title="Foods",description= d,color=0xa69ea8)
            await message.channel.send(embed=embed)

    def get_recipes(self,client,message):
        return
    
    def add_recipes(self,client,message):
        return
        
    def update_recipes(self,client,message):
        return