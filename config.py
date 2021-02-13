from brownie import *
from brownie.utils import color


class Config:
    NULL_ADDRESS = "0x0000000000000000000000000000000000000000"
    GAS_MULTIPLIER = 1.5  # avoid stuck tx's due to median gas variance
    DEPLOYER_ETH = "paralink_deployer_eth"  # brownie account id
    DEPLOYER_BSC = "paralink_deployer_bsc"  # brownie account id

    @staticmethod
    def get(name=network.show_active()):
        cls = None

        if name.startswith("binance"):
            if "mainnet" in name:
                cls = BinanceMainnet()
            elif "testnet" in name:
                cls = BinanceTestnet()
            else:
                raise ValueError(f"Network name '{name}' is not recognized.")
        elif name == "mainnet":
            cls = EthereumMainnet()
        else:
            raise ValueError(
                f"Network name '{color('bright magenta')}{name}{color}' is not recognized."
            )

        print(
            f"Using network config {color('bright magenta')}{type(cls).__name__}{color}, active network: {color('green')}{network.show_active()}{color}."
        )

        return cls


class EthereumMainnet(Config):
    # Deployments
    PARA_TOKEN = "0x3a8d5BC8A8948b68DfC0Ce9C14aC4150e083518c"
    PARA_FARMING = ""
    PARA_STAKING = ""
    TIMELOCK = ""
    GOVERNOR = ""

    UNISWAP_V2_FACTORY = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
    UNISWAP_V2_ROUTER = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

    def get_deployer_account(self):
        return accounts.load(self.DEPLOYER_ETH)


class BinanceMainnet(Config):
    PARA_ORACLE = ""
    PARA_ORACLE_USER = ""

    def get_deployer_account(self):
        return accounts.load(self.DEPLOYER_BSC)


class BinanceTestnet(Config):
    PARA_ORACLE = "0xf1DBf560bB5a2b0150DBaF3Fc351Be969A2CD7b0"
    PARA_ORACLE_USER = "0xe4A49adA9e491174ed86Fc8157fc5735531F5CCB"

    def get_deployer_account(self):
        return accounts.load(self.DEPLOYER_BSC)
