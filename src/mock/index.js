const getCodeOfRandom = () => {
  // 所需随机抽取的样本数组
  let nums = new Array("q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
  // 初始化 拼接字符串
  let str = "";
  for (let i = 0; i < 4; i++) {
    //每次生成一个0 - 61 之间的 number 作为随机获取验证码的下标
    let p = Math.floor(Math.random() * 1000) % 36;
    //拼接验证码  随机抽取大小写字母和数字
    str += nums[p];
  }
  return str;
}

export default [
  {
    url: "/Index/getCaptchaCode",
    method: "post",
    response: () => {
      return {
        status: {
          error_code: 0,
          error_msg: 'success'
        },
        bizobj: {
          code_key: '6012e9ba65b442d2e5e7fec6e8eabcfd',
          code: getCodeOfRandom()
        }
      };
    },
  },
  {
    url: "/Index/login",
    method: "post",
    response: () => {
      return {
        status: {
          error_code: 0,
          error_msg: 'success'
        },
        bizobj: {
          sys_token: 'd33a7fdf547d2a086a96f4d38253cbc9',
          admin_nick_name: '小三爷',
          admin_id: '1'
        }
      };
    },
  },
  {
    url: "/Index/getPermission",
    method: "post",
    response: () => {
      return {
        status: {
          error_code: 0,
          error_msg: 'success'
        },
        bizobj: [
          {
            "id": "1",
            "name": "权限管理",
            "parent_id": "0",
            "type": "1",
            "url": "/adminAuth/getRoleList",
            "secondMenuList": [
              {
                "id": "2",
                "name": "角色管理",
                "parent_id": "1",
                "type": "2",
                "url": "/adminAuth/getRoleList",
                "buttonList": [
                  {
                    "id": "3",
                    "name": "查询",
                    "parent_id": "2",
                    "type": "3",
                    "url": "/adminAuth/getRoleList"
                  },
                  {
                    "id": "3",
                    "name": "查看",
                    "parent_id": "2",
                    "type": "3",
                    "url": "/adminAuth/lookRole"
                  },
                  {
                    "id": "3",
                    "name": "修改",
                    "parent_id": "2",
                    "type": "3",
                    "url": "/adminAuth/saveRole"
                  },
                  {
                    "id": "3",
                    "name": "删除",
                    "parent_id": "2",
                    "type": "3",
                    "url": "/adminAuth/delRole"
                  }
                ]
              },
              {
                "id": "4",
                "name": "账号管理",
                "parent_id": "1",
                "type": "2",
                "url": "/adminAuth/adminList",
                "buttonList": [
                  {
                    "id": "8",
                    "name": "查询",
                    "parent_id": "4",
                    "type": "3",
                    "url": "/adminAuth/adminList"
                  },
                  {
                    "id": "3",
                    "name": "修改",
                    "parent_id": "2",
                    "type": "3",
                    "url": "/adminAuth/modifyAdmin"
                  }


                ]
              }
            ]
          },
          {
            "name": "三方库管理",
            "parent_id": "0",
            "type": "1",
            "url": "/third/editor",
            "secondMenuList": [
              {
                "id": "2",
                "name": "富文本",
                "parent_id": "1",
                "type": "2",
                "url": "/third/editor",
                "buttonList": [
                  {
                    "id": "3",
                    "name": "查询",
                    "parent_id": "2",
                    "type": "3",
                    "url": "/third/editor"
                  }
                ]
              },
              {
                "id": "4",
                "name": "markdown",
                "parent_id": "1",
                "type": "2",
                "url": "/third/markdown",
                "buttonList": [
                  {
                    "id": "8",
                    "name": "查询",
                    "parent_id": "4",
                    "type": "3",
                    "url": "/third/markdown"
                  }

                ]
              }
            ]
          },
          {
            "name": "音频可视化",
            "parent_id": "0",
            "type": "1",
            "url": "/audio/canvas",
            "secondMenuList": [
              {
                "id": "2",
                "name": "canvas+audio",
                "parent_id": "1",
                "type": "2",
                "url": "/audio/canvas"

              },
              {
                "id": "3",
                "name": "wavesurfer",
                "parent_id": "1",
                "type": "2",
                "url": "/audio/wavesurfer"

              }

            ]
          }
        ]
      };
    },
  },
  {
    url: "/adminAuth/adminList",
    method: "post",
    response: () => {
      return {
        status: {
          error_code: 0,
          error_msg: 'success'
        },
        bizobj: [
          {
            "id": "1",
            "account": "admin",
            "date": "2023-03-27 13:58:15",
            "role_name": "主管"
          },
          {
            "id": "2",
            "account": "小三爷",
            "date": "2023-01-27 13:58:15",
            "role_name": "主管"
          },
          {
            "id": "3",
            "account": "张三",
            "date": "2022-02-27 13:58:15",
            "role_name": "普通员工"
          }
        ],
        "page_info": {
          "cur_page": "1",
          "page_size": "10",
          "total_items": "3"
        }
      };
    },
  },
  {
    url: "/adminAuth/getRoleList",
    method: "post",
    response: () => {
      return {
        status: {
          error_code: 0,
          error_msg: 'success'
        },
        bizobj: [
          {
            "id": "1",
            "name": "主管",
            "operator": "2023-04-26 11:10:52"
          },
          {
            "id": "2",
            "name": "普通员工",
            "operator": "2023-04-26 11:10:12"
          }
        ],
        "page_info": {
          "cur_page": "1",
          "page_size": "10",
          "total_items": "2"
        }
      };
    },
  },

];


