from string import Template

import yaml


class Config:
    def __init__(self, path: str | None = None):
        if not path:
            path = "./config.yaml"

        with open(path) as file:
            config = yaml.safe_load(file)

            self.bot_token = config["bot_token"]
            self.welcome_channel_id = config["welcome_channel_id"]
            self.welcome_message = Template(config["welcome_message"])
