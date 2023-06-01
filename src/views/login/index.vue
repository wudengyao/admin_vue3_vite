<template>
  <div class="login-container">
    <el-form ref="loginFromRef" class="login-form" :model="loginForm" :rules="loginRules">
      <div class="title-container">
        <h3 class="title">Vue3后台系统</h3>
      </div>

      <el-form-item prop="username" style="display: flex;flex-direction: row">
        <span class="icon-container">
          <UserFilled style="width: 1em;height: 1em"/>
        </span>
        <el-input placeholder="请输入用户名" name="username" type="text" v-model="loginForm.username"/>
      </el-form-item>

      <el-form-item prop="password">
        <span class="icon-container">
          <Lock style="width: 1em;height: 1em"/>
        </span>
        <el-input placeholder="请输入密码" name="password" :type="passwordType" v-model="loginForm.password" />
        <span class="show-pwd">
          <svg-icon
              :icon="passwordType === 'password' ? 'eye' : 'eye-open'"
              @click="onChangePwdType"
          />

        </span>
      </el-form-item>

      <el-form-item class="code-box">
       <span class="icon-container">
          <Tickets style="width: 1em;height: 1em"/>
        </span>
        <el-input
            placeholder="图形验证码"
            v-model="loginForm.captcha_code" class="code-input" maxlength="4">
        </el-input>
        <div class="code-img" @click="getCodeImg">{{loginForm.captcha_code}}</div>
      </el-form-item>


      <el-button type="primary" style="width: 100%; margin-bottom: 30px;" :loading="loading"
                 @click="handleLogin"
                 size="large"
                >登录</el-button>

      <div style="color: red">账户密码随便输</div>

    </el-form>


  </div>
</template>

<script setup>
import {UserFilled,Lock,Tickets} from '@element-plus/icons'

import { ref, onMounted } from 'vue'
import { validatePassword } from './rules'
import { getCode } from '@/api/api'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'



onMounted(() => {
  getCodeImg()
})

//数据源
const loginForm = ref({
  username: 'admin',
  password: '123456',
  captcha_code: '',
  code_key: ''
})
//验证规则
const loginRules = ref({
  username: [
    {
      required: true,
      trigger: 'blur',
      message: '请输入用户名'
    },

  ],
  password: [
    {
      required: true,
      trigger: 'blur',
      validator: validatePassword()
    },

  ],
})

// 处理密码框文本显示状态
const passwordType = ref('password')
const onChangePwdType = () => {
  if (passwordType.value === 'password') {
    passwordType.value = 'text'
  } else {
    passwordType.value = 'password'
  }
}

// 登录动作处理
const loading = ref(false)
const loginFromRef = ref(null)
const store = useStore()
const router = useRouter()

/**
 * 登录
 */
const handleLogin = () => {
  loginFromRef.value.validate(valid => {
    if (!valid) return
    loading.value = true
    store.dispatch('user/login', loginForm.value)
        .then(() => {
          loading.value = false
          // TODO: 登录后操作
          router.push('/')

        })
        .catch(err => {
          getCodeImg()
          loading.value = false
        })

  })


}
/**
 * 获取图形验证码
 */
const getCodeImg = () => {

  loginForm.value.code_key = '43b0a022b1300a92199496ceff9d567f'
  loginForm.value.captcha_code = getCodeOfRandom()

  // getCode({})
  //   .then(data => {
  //     let obj = data.bizobj
  //
  //     loginForm.value.code_key = obj.code_key
  //     loginForm.value.captcha_code = obj.code
  //   })
  //   .catch(err => {
  //   })
}


const getCodeOfRandom = ()=>{
  // 所需随机抽取的样本数组
  let nums=new Array("q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","0","1","2","3","4","5","6","7","8","9");
  // 初始化 拼接字符串
  let str="";
  for(let i=0;i<4;i++){
    //每次生成一个0 - 61 之间的 number 作为随机获取验证码的下标
    let p=Math.floor(Math.random()*1000)%36;
    //拼接验证码  随机抽取大小写字母和数字
    str+=nums[p];
  }
  return str;
}


</script>

<style lang="scss" scoped>
$bg: #5268bc;
$dark_gray: #889aa4;
$light_gray: #eee;
$cursor: #000000;
$txt_color: #333;


.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 35px;
    margin: 0 auto;
    overflow: hidden;
    background: white;
    margin-top: 7%;
    border-radius:4px;


    ::v-deep .el-form-item {
      border: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(0, 0, 0, 0.1);
      border-radius: 5px;
      color: #454545;
    }

    ::v-deep .el-input{
      display: inline-block;
      height: 47px;
      width: 85%;

      input {
        background: transparent;
        -webkit-appearance: none;
        padding: 12px 5px 12px 15px;
        height: 47px;
        caret-color: $cursor;
        color: $txt_color;
      }
      .el-input__wrapper {
        background: transparent;
        -webkit-appearance: none;
        padding: 12px 5px 12px 15px;
        height: 47px;
        caret-color: $cursor;
        color: $txt_color;
      }
      .el-input__wrapper is-focus{
        background: transparent;
        -webkit-appearance: none;
        border-radius: 0px;
        padding: 12px 5px 12px 15px;
        height: 47px;
        caret-color: $cursor;
        color: $txt_color;
    }
    }
  }


  .icon-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $txt_color;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
  .code-box{
    position: relative;

    .code-img {
      position: absolute;
      width:60px;
      right: 0;
      top: 6px;
      font-size:22px;
      background: transparent;

    }
  }
}
</style>