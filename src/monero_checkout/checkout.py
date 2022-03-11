"""
    Python tool to handler payments on Monero
    Author: Mikaio
    Author's Github: https://github.com/Mika-IO
"""


class PaymentCheckout:
    def __init__(
        self,
        user,
        password,
        rpc_host="127.0.0.1",
        rpc_port=18088,
        protocol="http",
        path="/json_rpc",
    ):
        self.user = user
        self.password = password
        self.rpc_host = rpc_host
        self.rpc_port = rpc_port
        self.protocol = protocol
        self.path = path

    def generate_payment(self):
        """
        Mocked return for now
        """
        return {
            "payment_id": "",
            "total_amount": "",
            "qr_code": "",
            "wallet_adress": "",
        }

    def check_payment_staus(self):
        """
        Mocked return for now
        """
        return {
            "payment_id": "",
            "status": "",  # possible values: not_payed, payed
        }

    def connect_wallet(self):
        from monero.wallet import Wallet
        from monero.backends.jsonrpc import JSONRPCWallet

        rpc_wallet = JSONRPCWallet(
            protocol=self.protocol,
            host=self.rpc_host,
            port=self.rpc_port,
            path=self.protocol,
            user=self.user,
            password=self.password,
            timeout=30,
            verify_ssl_certs=True,
            proxy_url=None,
        )
        wallet = Wallet(rpc_wallet)

        return wallet
