import random
from giphypop import gif, search_list, random_gif
from errbot import BotPlugin, botcmd

class Giphy(BotPlugin):
    """An Err plugin skeleton"""
    min_err_version = '1.6.0'  # Optional, but recommended
    max_err_version = '2.0.0'  # Optional, but recommended

    def get_configuration_template(self):
        """Defines the configuration structure this plugin supports"""
        return { 'API_KEY': 'dc6zaTOxFJmzC', }

    @botcmd(split_args_with=None)
    def gif(self, mess, args):
        """Return a random gif based on search query"""
        img_list = search_list(term=' '.join(args), api_key=self.config['API_KEY'])
        if img_list:
            count = len(img_list)
            if count == 0:
                return "No results"

        random_index = random.randrange(count)
        img = img_list[random_index]
        return img['original']['url']

    @botcmd(split_args_with=None)
    def gif_random(self, mess, args):
        """Return a random gif"""
        img = random_gif(api_key=self.config['API_KEY'])
        return img['original']['url']

    @botcmd(split_args_with=None)
    def gif_id(self, mess, args):
        """Return a specific gif by unique ID"""
        img = gif(gif_id=args[0], api_key=self.config['API_KEY'])
        return img['original']['url']

