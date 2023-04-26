import datetime
import os
import random

import sqlalchemy
from discord.ext.commands import has_permissions

from Parser import Parser
from apps import get_cat
import asyncio
import discord
from discord.ext import commands
from data import db_session
from data.user import User


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.test_1_f = False
        self.amount_of_questions = 0
        self.answer = None
        self.res = 0

    @commands.command(name='randint')
    async def my_randint(self, ctx, min_int, max_int):
        num = random.randint(int(min_int), int(max_int))
        await ctx.send(num)

    @commands.command(name='set_timer')
    async def timer(self, ctx, *time):
        # $set_timer in 0 minutes 3 seconds
        minutes = int(time[1])
        seconds = int(time[3])
        await asyncio.sleep(60 * minutes + seconds)
        await ctx.send('Time X has come')

    @commands.command(name='help_')
    async def help_(self, ctx):
        await ctx.send('''
        $randint min max
        $set_timer time
        $ban nickname
        $result
        $all_result
        $test
        $youtube link mp3(optional)
        ''')

    @commands.command(name='ban')
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member):
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name == str(member.name)).first()
        if int(user.result_score) < 0:
            await member.ban(reason='IDIOT')
            await ctx.send(f'Участник под ником <@{member.id}> был забанен')
            await asyncio.sleep(int(user.result_score) * 10)
            await member.unban()
            await ctx.send(f'*У {member.mention} закончился бан*')
            link = await ctx.channel.create_invite(max_age=300)
            await member.send(f'У тебя закончился бан на сервере "{ctx.guild.name}"! {link}')
            user.result_score = 0
            db_sess.add(user)
            db_sess.commit()
        else:
            await ctx.author.ban(reason='IDIOT')
            await ctx.send(f'Участник под ником <@{ctx.id}> был забанен')

    @commands.command(name='result')
    async def result_get(self, ctx):
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name == str(ctx.author)).first()
        await ctx.send(user.result_score)

    @commands.command(name='test')
    async def test(self, ctx):
        self.test_1_f = True
        problem = f'{random.randint(-10000, 10000)} {random.choice(["+", "-", "*"])} {random.randint(-10000, 10000)}'
        self.answer = int(eval(problem))
        self.amount_of_questions += 1
        await ctx.send(problem)

    @commands.command(name='youtube')
    async def youtube(self, ctx, link, mp3=False):
        parser = Parser()
        q = parser(link, 'vfv.mp4', mp3)
        await ctx.send(file=discord.File(q))
        os.remove(os.getcwd() + 'vfv.mp4')

    @commands.command(name='all_result')
    async def all_result(self, ctx):
        db_sess = db_session.create_session()
        user = db_sess.query(User)
        top = []
        for i in user:
            top.append((i.name, i.result_score))
        top.sort(key=lambda x: int(x[1]))
        for i in top:
            await ctx.send(f'{i[0]}:::   {i[1]}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content[0] != '$':
            if message.author == self.bot.user:
                return None
            if self.test_1_f is True:
                if int(message.content) == int(self.answer):
                    self.res += 1
                else:
                    self.res += -50
                if self.amount_of_questions == 10:
                    self.test_1_f = False
                    self.amount_of_questions = 0
                    self.answer = 0

                self.amount_of_questions += 1
                problem = f'{random.randint(-10000, 10000)} {random.choice(["+", "-", "*"])} {random.randint(-10000, 10000)}'
                self.answer = int(eval(problem))
                await message.channel.send(problem)

            try:
                user = User()
                user.name = str(message.author)
                user.tags = ''
                user.last_messages = str(message.content)
                user.result_score = self.res
                user.created_date = datetime.datetime.now()
                db_sess = db_session.create_session()
                db_sess.add(user)
                db_sess.commit()
            except sqlalchemy.exc.IntegrityError:
                db_sess = db_session.create_session()
                user = db_sess.query(User).filter(User.name == str(message.author)).first()
                u = user.last_messages
                r = user.result_score
                user.result_score = r + self.res
                user.created_date = datetime.datetime.now()
                user.last_messages = str(u) + "%-%" + str(message.content)
                db_sess.add(user)
                db_sess.commit()
            self.res = 0

            if "кот" in message.content.lower():
                await message.channel.send(get_cat())


