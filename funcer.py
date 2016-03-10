# -*- coding: utf-8 -*-
import os
import sys
import re

import yaml

class FuncMaker(object):

    def __init__(self, mp):
        '''确保string中的符号均为半角符号
        '''
        self._func_pre = 'calc_'
        self._mp = mp
        self._split_pattern = re.compile(r'[-+*/()\d]')
        self._param_pattern = re.compile(r'([^-+*/()\d ]+)')
    
    def make(self, string):
        self._str = string
        # get function name & params
        self._split_lr()
        self.func_name = self._func_pre + self._mp[self._func_name_key]
        self.params = self._find_params()

        self.expression = self._make_expression()

        func_str = self.make_func(self.func_name, self.params, self.expression)
        return func_str

    def _split_lr(self, delim='='):
        '''
        _func_name_key: left part in equation
        _expression: right part in equation 
        '''
        self._func_name_key, self._expression = [
                i.strip() for i in self._str.split(delim)]

    def _find_params(self):
        params = []
        for key in re.split(self._split_pattern, self._expression):
            key = key.strip()
            if not key:
                continue

            param = self._mp[key]
            if param in params:
                continue

            params.append(param)

        return params
            
    
    def _make_expression(self):
        return re.sub(
                self._param_pattern, 
                lambda x: self._mp[x.group()],
                self._expression,
                re.X)

    @staticmethod
    def make_func(func_name, params, expression):
        func = ('def %(func_name)s(%(params)s):\n'
                '    return %(expression)s\n'
                ) %{'func_name': func_name,
                    'params': ', '.join(params),
                    'expression': expression}
        
        return func

def main(map_fn, func_fn):
    '''
    '''
    with open(map_fn, 'rb') as map_file, open(func_fn, 'rb') as func_file:
        data_map = yaml.load(map_file)
        fm = FuncMaker(data_map)
        for line in func_file:
            print fm.make(line.decode('utf8'))

if __name__ == '__main__':
    
    model_name = os.path.abspath(sys.argv[1])

    map_fn = '%s.yaml' %model_name
    func_fn = '%s.func' %model_name

    main(map_fn, func_fn)
