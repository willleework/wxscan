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
    statusColor: '#999999',
    statusText: '-',
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
          hasUserInfo: true,
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
        //console.log(res.data)
        if (res.errMsg !='scanCode:ok')
        {
          wx.showToast({
            title: '扫码失败',
          })
          return
        }
        //调用后台服务查询
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
              page.setData({ devid: res.data.dev_id });
              page.setData({ devdatainfo: res.data.dev_info});
              page.setData({
                devid: res.data.dev_id,
                devdatainfo: res.data.dev_info,
                statusColor: page.getStatusColor(res.data.dev_status),
                statusText: page.getStatusText(res.data.dev_status),
              })
            }
            else if (status == '2001') {
              wx.showToast({
                title: '用户尚未登录',
                duration: 1000
              })
              wx.navigateTo({
                url: '../login/login'
              })
            }
            else if(status == 3002){
              wx.showModal({
                title: '数据查询失败',
                content: '没有检索到对应设备信息',
              })
            } else {
              wx.showModal({
                title: '数据查询失败',
                content: res.data.info,
              })
            }
          }
        })
      }
    })
  },
  borrowTab: function(){

  },
  returnTab: function(){
    
  },
  getStatusColor: function(status){
    switch(status)
    {
      case '0':
        return '#CC0000'
      case '1':
        return '#66CC99'
      case '2':
        return '#FF9900'
      case '3':
        return '#999999' 
    }
  },
  getStatusText: function(status){
    switch (status) {
      case '0':
        return '未初始化'
      case '1':
        return '正常'
      case '2':
        return '借出'
      case '3':
        return '不可用'
    }
  }
})