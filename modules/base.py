import streamlit as st
class BaseModule:
    def __init__(self,name,prefix):
        self.name=name; self.prefix=prefix
    def run_and_store(self,key,func,*a,**k):
        r=func(*a,**k); st.session_state.results.setdefault(self.prefix,{})[key]=r; return r
    def render(self): raise NotImplementedError
class ModuleRegistry:
    _m={}
    @classmethod
    def register(cls,m): cls._m[m.name]=m
    @classmethod
    def names(cls): return list(cls._m.keys())
    @classmethod
    def get(cls,n): return cls._m[n]