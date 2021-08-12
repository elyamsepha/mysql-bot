import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get
from contador import Contador
from banco_de_dados import Cadastro
from banco_de_dados import Mostrar
import datetime
import os


caminho = os.getcwd()

client = commands.Bot(command_prefix='sql.')

client.remove_command('help')

@client.command()
async def cadastrar(ctx):
	nome = (f'{ctx.author.name}#{ctx.author.discriminator}')
	id_discord = str(ctx.author.id)
	if Cadastro.verificar_usuario(id_discord) == True:
		await ctx.send(f"{ctx.author.mention} você ja está cadastrado!")
	if Cadastro.verificar_usuario(id_discord) == False:
		data = str(datetime.datetime.now())
		data = str(data[0:19])
		id_usuario = str(Contador.pegar_numero())
		Cadastro.adicionar_usuario(nome, id_discord, id_usuario, data)
		await ctx.send(f"```você se cadastrou com sucesso!\nseu id de reconhecimento é: {id_usuario}```")


@client.command()
async def mostrar(ctx, metodo, info):
	await ctx.send(f"```{Mostrar.info(metodo, info)}```")

@client.command()
async def mostrar_todos(ctx):
	Mostrar.todos()
	await ctx.send(file=discord.File(caminho+r'//todos_cadastrados.txt'))

@client.command()
async def help(ctx):
    embed = discord.Embed(
            title = 'COMANDOS',
            description = (f"```—————— | métodos de reconhecimento | ——————\n---> id\n---> id_discord\n---> nome\n\n———————————— |  COMANDOS | —————————————————\n\n---> sql.cadastrar\n---> sql.mostrar\n\nEXEMPLOS:\n     sql.mostrar id: 1\n————————————————————————————————————————————```"),
            colour = discord.Colour.red()
            )

    embed.set_footer(text='mysql bot')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/875369695379873825/875459591159304192/SQL-Course.png?width=784&height=442')

    await ctx.send(embed=embed)

client.run("TOKEN")