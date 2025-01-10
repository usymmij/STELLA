import wandb

class Logger:
    def __init__(self, settings, name):

        self.wandb = wandb.init(
            project=name,
            config=settings
            #config={
            #    "learning_rate": lr,
            #    "epochs": epochs,
            #},
        )
def log_session(self, log_dict):
    self.wandb.log(log_dict)

