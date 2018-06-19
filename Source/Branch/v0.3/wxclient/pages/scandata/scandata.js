// pages/scandata/scandata.js
//获取应用实例
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    devid: '扫码识别设备ID',
    devdatainfo: '',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
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

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  },
  /**
 * 用户点击扫码
 */
  scanTab: function () {
    var page = this;
    wx.scanCode({
      success: (res) => {
        console.log(res)
        wx.request({
          url: app.globalData.sanadd,
          data: {
            dev_id: res.result,
            session_no: app.globalData.sessionno,
          },
          header: {
            "Content-Type": "application/json"
          },
          success: function (res) {
            console.log(res.data.status)
            var status = res.data.status
            if (status == '1000') {
              /*wx.showModal({
                title: '查询结果',
                content: res.data.dev_info,
              })*/
              page.setData({ devid: res.data.dev_id });
              page.setData({ devdatainfo: res.data.dev_info});
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
})