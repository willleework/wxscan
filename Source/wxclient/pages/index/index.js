//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: '数据识别程序',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  loginTab: function(){
    wx.scanCode({
      success: (res) => {
        console.log(res)
        wx.request({
          url: 'http://192.168.117.102:8000/wxgds/devInfoQuery/',
          data: {
            dev_id: res.result,
          },
          header: {
            "Content-Type": "application/json"
          },
          success: function (res) {
            console.log(res.data.status)
            var status = res.data.status
            if (status == '0') {
              wx.showModal({
                title: '查询结果',
                content: res.data.data.dev_info,
              })
            }
            else if (status == '404') {
              wx.showToast({
                title: '未找到数据',
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
