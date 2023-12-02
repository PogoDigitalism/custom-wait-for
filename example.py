import asyncio
import discord
from discord.ext import commands

class TicketContinueView(discord.ui.View):
    def __init__(self, Cog): # Requires you to pass the instance (in this case a Cog) of where you instanced the view and thus want the custom wait_for to be.
        self.Cog = Cog
        super().__init__(timeout=None)

    @discord.ui.button(style=discord.ButtonStyle.blurple, label='continue')
    async def Continue(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.Cog._interaction_future.set_result(True)


class TicketHandler(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    async def wait_for_interaction(self, timeout: int = None):
        self._interaction_future = asyncio.Future(loop=asyncio.get_event_loop())

        try:
            return await asyncio.wait_for(self._interaction_future, timeout=timeout)
        except asyncio.TimeoutError:
            return None
        finally:
            self._interaction_future = None


    @commands.command()
    async def test(self, ctx: commands.Context) -> None:
      TicketContinueView = TicketContinueView(Cog=self)
      await ctx.channel.send('Continue?', view=TicketContinueView)
        
      result = await wait_for_interaction(timeout=60)
      if result is None:
        await ctx.channel.send('No interaction happened, closing.', delete_after=10)
        return

      # continue test()
