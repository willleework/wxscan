// pages/login/login.js
//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: '点击头像使用微信账号登录',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  loginTab: function () {
    var that = this;
    wx.request({
      url: 'http://192.168.117.103:8000/wxgds/login/',
      data: {
        username: 'will',
        password: '123',
      },
      header: {
        "Content-Type": "application/json"
      },
      success: function (res) {
        if (res.data.status == 1000) {
          console.log(res.data.session_no)
          app.globalData.sessionno = res.data.session_no;
          /*wx.showToast({
            title: '登录成功！',
          })*/
          wx.navigateTo({
            url: '../main/main'
          })
        } else {
          wx.showToast({
            title: '登录失败！',
          })
        }
      },
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function (e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  }
})
