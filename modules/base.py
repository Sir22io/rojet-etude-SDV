import streamlit as st

class BaseModule:
    """Classe de base pour tous les modules Streamlit."""
    name: str
    key_prefix: str

    def __init__(self, name: str, key_prefix: str):
        self.name = name
        self.key_prefix = key_prefix

    def run_and_store(self, key: str, func, *args, **kwargs):
        result = func(*args, **kwargs)
        st.session_state.results.setdefault(self.key_prefix, {})[key] = result
        return result

    def render(self):
        raise NotImplementedError

class ModuleRegistry:
    _modules = {}

    @classmethod
    def register(cls, module: BaseModule):
        cls._modules[module.name] = module

    @classmethod
    def get(cls, name: str) -> BaseModule:
        return cls._modules[name]

    @classmethod
    def names(cls):
        return list(cls._modules.keys())
