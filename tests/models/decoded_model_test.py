import datetime

import pytest

from ethtx.models.decoded_model import (
    AddressInfo,
    DecodedTransactionMetadata,
    Argument,
    DecodedEvent,
    DecodedCall,
    DecodedTransfer,
    DecodedBalance,
    Proxy,
)

FAKE_TIME = datetime.datetime(2020, 12, 25, 17, 5, 55)


@pytest.fixture
def patch_datetime_now(monkeypatch):
    class MyDatetime:
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, "datetime", MyDatetime)


class TestDecodedModels:
    @classmethod
    def setup_class(cls):
        cls.ai = AddressInfo(address="address", name="name")
        cls.a = Argument(name="name", type="type", value=1)

    def test_address_info(self):
        ai = AddressInfo(address="address", name="name")

        assert ai.address == "address"
        assert ai.name == "name"
        assert ai.badge is None

    def test_decoded_transaction_metadata(self):
        dtm = DecodedTransactionMetadata(
            chain_id="mainnet",
            tx_hash="0x12345",
            block_number=1,
            block_hash="0x12345",
            timestamp=FAKE_TIME,
            gas_price=1,
            sender=self.ai,
            receiver=self.ai,
            tx_index=1,
            tx_value=2,
            gas_limit=3,
            gas_used=4,
            success=True,
        )

        assert dtm.chain_id == "mainnet"
        assert dtm.tx_hash == "0x12345"
        assert dtm.block_number == 1
        assert dtm.block_hash == "0x12345"
        assert dtm.timestamp == FAKE_TIME
        assert dtm.gas_price == 1
        assert dtm.sender == self.ai
        assert dtm.receiver == self.ai
        assert dtm.tx_index == 1
        assert dtm.tx_value == 2
        assert dtm.gas_limit == 3
        assert dtm.gas_used == 4
        assert dtm.eth_price is None
        assert dtm.success

    def test_argument(self):
        a = Argument(name="name", type="type", value=1)

        assert a.name == "name"
        assert a.type == "type"
        assert a.value == 1

    def test_decoded_event(self):
        de = DecodedEvent(
            chain_id="mainnet",
            tx_hash="0x12345",
            timestamp=FAKE_TIME,
            contract=self.ai,
            index=1,
            event_signature="0x0bc2390103cdcea68787f9f22f8be92ccf20f5eae0bb850fbb70af78e366e4dd",
            event_name="WalletAddressesSet",
            parameters=[self.a, self.a],
        )

        assert de.chain_id == "mainnet"
        assert de.tx_hash == "0x12345"
        assert de.timestamp == FAKE_TIME
        assert de.contract == self.ai
        assert de.index == 1
        assert de.call_id is None
        assert (
            de.event_signature
            == "0x0bc2390103cdcea68787f9f22f8be92ccf20f5eae0bb850fbb70af78e366e4dd"
        )
        assert de.event_name == "WalletAddressesSet"
        assert de.parameters == [self.a, self.a]
        assert not de.guessed

    def test_decoded_call(self):
        dc = DecodedCall(
            chain_id="mainnet",
            tx_hash="0x12345",
            timestamp=FAKE_TIME,
            call_type="call",
            from_address=self.ai,
            to_address=self.ai,
            value=15,
            function_signature="0x521f8bed",
            function_name="getAllOperator",
            arguments=[self.a],
            outputs=[],
            gas_used=15,
            status=True,
            indent=1,
        )

        assert dc.chain_id == "mainnet"
        assert dc.tx_hash == "0x12345"
        assert dc.timestamp == FAKE_TIME
        assert dc.call_id is None
        assert dc.call_type == "call"
        assert dc.from_address == self.ai
        assert dc.to_address == self.ai
        assert dc.value == 15
        assert dc.function_signature == "0x521f8bed"
        assert dc.function_name == "getAllOperator"
        assert dc.arguments == [self.a]
        assert dc.outputs == []
        assert dc.gas_used == 15
        assert dc.error is None
        assert dc.status
        assert dc.indent == 1
        assert dc.subcalls == []
        assert not dc.guessed

    def test_decoded_transfer(self):
        dt = DecodedTransfer(
            from_address=self.ai, to_address=self.ai, token_symbol="ts", value=0.15
        )

        assert dt.from_address == self.ai
        assert dt.to_address == self.ai
        assert dt.token_address is None
        assert dt.token_symbol == "ts"
        assert dt.token_standard is None
        assert dt.value == 0.15

    def test_decoded_balance(self):
        db = DecodedBalance(holder=self.ai, tokens=[{}])

        assert db.holder == self.ai
        assert db.tokens == [{}]

    def test_proxy(self):
        p = Proxy(address="address", name="name", type="type")

        assert p.address == "address"
        assert p.name == "name"
        assert p.type == "type"
        assert p.semantics is None
        assert p.token is None
