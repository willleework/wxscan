//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: '数据识别程序',
    userInfo: {},
    hasUserInfo: false,
    sessionno: '',
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  loginTab: function(){
    var that = this;
    wx.request({
      url: 'http://192.168.117.102:8000/wxgds/login/',
      data: {
        username: 'will',
        password: '123',
      },
      header: {
        "Content-Type": "application/json"
      },
      success:function(res){
        if (res.data.status == 1000) {
          console.log(res.data.session_no)
          that.data.sessionno = res.data.session_no;
          wx.showToast({
            title: '登录成功！',
          })
        } else {
         wx.showToast({
           title: '登录失败！',
         })
        }
      },
    })
  },
  scanTab: function(){
    var that = this;
    wx.scanCode({
      success: (res) => {
        console.log(res)
        wx.request({
          url: 'http://192.168.117.102:8000/wxgds/devInfoQuery/',
          data: {
            dev_id: res.result,
            session_no: that.data.sessionno,
            username:'will',
          },
          header: {
            "Content-Type": "application/json"
          },
          success: function (res) {
            console.log(res.data.status)
            var status = res.data.status
            if (status == '1000') {
              wx.showModal({
                title: '查询结果',
                content: res.data.dev_info,
              })
            }
            else if (status == '2001') {
              wx.showToast({
                title: '用户尚未登录',
                duration: 1000
              })
            } else {
              wx.showToast({
                title: '查询失败',
                duration: 1000,
              })
            }
          }
        })
      }
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
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
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  }
})
