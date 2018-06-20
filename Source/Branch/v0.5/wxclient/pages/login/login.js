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
    wx.login({
      success: function (res) {
        console.log('code: ' + res.code)
        wx.request({
          url: app.globalData.loginadd,
          data: {
            jscode: res.code,
          },
          header: {
            "Content-Type": "application/json"
          },
          success: function (res) {
            if (res.data.status == 1000) {
              console.log('sessionno:'+res.data.session_no)
              app.globalData.sessionno = res.data.session_no;
              wx.navigateTo({
                url: '../main/main'
              })
            } else {
              wx.showModal({
                title: '登录失败',
                content: res.data.info,
              })
            }
          },
        })
      }});
  },
  registerTab: function(){
    wx.login({
      success: function (res) {
        console.log('code: ' + res.code)
        wx.request({
          url: app.globalData.rigisteradd,
          method: "POST",  
          data: {
            jscode: res.code,
            nickname: app.globalData.userInfo.nickName
          },
          header: {
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
          },
          success: function (res) {
            if (res.data.status == 1000) {
              wx.showModal({
                title: '注册成功',
                content: res.data.info,
              })
            } else {
              wx.showModal({
                title: '注册失败',
                content: res.data.info,
              })
            }
          },
        })
      }
    });
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
