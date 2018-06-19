# -*- coding: utf-8 -*-
from wxgds.utils.domanimodels.modelbase import ConvertToJson

'''
用户信息类
'''
class UserBase(ConvertToJson):

    @property
    def user_name(self):
        return self._user_name
    @user_name.setter
    def user_name(self, value):
        self._user_name = value;

    @property
    def pass_word(self):
        return self._pass_word
    @pass_word.setter
    def pass_word(self, value):
        self._pass_word = value

    @property
    def login_time(self):
        return self._login_time
    @login_time.setter
    def login_time(self, value):
        self._login_time = value

    @property
    def user_mac(self):
        return self._user_mac
    @user_mac.setter
    def user_mac(self, value):
        self._user_mac = value

    @property
    def user_ip(self):
        return self._user_ip
    @user_ip.setter
    def user_ip(self, value):
        self._user_ip = value