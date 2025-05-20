import streamlit as st

class BaseModule:
    def __init__(self, name, prefix):
        self.name = name
        self.prefix = prefix
    def run_and_store(self, key, func, *args, **kwargs):
        res = func(*args, **kwargs)
        st.session_state.results.setdefault(self.prefix, {})[key] = res
        return res
    def render(self):
        raise NotImplementedError

class ModuleRegistry:
    _modules = {}
    @classmethod
    def register(cls, module):
        cls._modules[module.name] = module
    @classmethod
    def names(cls):
        return list(cls._modules.keys())
    @classmethod
    def get(cls, name):
        return cls._modules[name]
