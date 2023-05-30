
import moment from "moment";
import store from '@/store'
import {
  VERSION,
  MODEL_TEST_VERSION,
  SERVER_TYPE,
  TEST_URL,
  MO_URL,
  YFB_URL,
  PRO_URL,
  DEV_URL
} from '@/constant'



// 将字符串的字符全部转换为小写字符
export function lowerCase(str) {
  let arr = str.split("");
  let newStr = "";
  //通过for循环遍历数组
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 'A' && arr[i] <= 'Z')
      newStr += arr[i].toLowerCase();
    else
      newStr += arr[i];
  }
  return newStr;
}




//数据导出（要求接口是get方法啊）
export function exportDataFormatUrl(request_url, request_params, is_new) {

  let server_url = switchServerUrl()

  let url = server_url + request_url;


  if (SERVER_TYPE == 3) {
    url = url + '/version/' + VERSION
  } else {
    url = url + '/version/' + MODEL_TEST_VERSION
  }


  let params = JSON.parse(JSON.stringify(request_params));
  if (store.getters.token) {
    params.sys_token = store.getters.token
  }
  let data = "?";
  for (let key in params) {
    data = data + "&" + key + "=" + params[key];
  }

  url = url + data

  console.log(url)

  if (is_new) {
    //打开新窗口
    window.open(url);
  } else {
    //在本窗口打开
    window.location.href = url;
  }

}



// 获取当前服务器的请求url
export function switchServerUrl() {
  let server_url = ""
  switch (SERVER_TYPE) {
    case 0:
      server_url = TEST_URL
      break
    case 1:
      server_url = MO_URL
      break
    case 2:
      server_url = YFB_URL
      break
    case 3:
      server_url = PRO_URL
      break
    case 4:
      server_url = DEV_URL
      break

  }
  return server_url;

}

/**
 * 格式换权限菜单返回数据
 * @param data
 */
export  function formatPermissionList(data){
  let list = data;
  let role_arr=[]//菜单权限
  let button_arr=[]//button权限
  for(let i in list){
    var i_item = list[i].secondMenuList
    for(let j in i_item){
      var j_item = i_item[j]
      if(j_item.url){
        if(j == 0){
          role_arr.push({
            url:'/'+list[i].url.split('/')[1]
          })
        }
        role_arr.push({
          url:j_item.url
        })
        //button权限赋值存起来
        var k_item = j_item.buttonList
        for(let k in k_item){
          if(k_item[k].url){
            button_arr.push(lowerCase(k_item[k].url));
          }
        }
      }
    }
  }
  return {role_arr:role_arr,button_arr:button_arr}
}
