"""Tests for FuelAgent"""
import pytest
from fuel_agent_kit import FuelAgent, FuelAgentConfig

class TestFuelAgent:
    def test_init_success(self):
        config = FuelAgentConfig(wallet_private_key="test_key", model="openai")
        agent = FuelAgent(config)
        assert agent is not None
    
    def test_init_missing_private_key(self):
        with pytest.raises(ValueError):
            config = FuelAgentConfig(wallet_private_key="", model="openai")
            FuelAgent(config)
