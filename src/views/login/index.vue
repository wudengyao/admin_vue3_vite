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
        <el-input  placeholder="请输入用户名" name="username" type="text" v-model="loginForm.username" @keyup.enter.native="handleLogin"/>
      </el-form-item>

      <el-form-item prop="password">
        <span class="icon-container">
          <Lock style="width: 1em;height: 1em"/>
        </span>
        <el-input placeholder="请输入密码" name="password" :type="passwordType" v-model="loginForm.password" @keyup.enter.native="handleLogin"/>
        <span class="show-pwd">
          <svg-icon
              :icon="passwordType === 'password' ? 'eye' : 'eye-open'"
              @click="onChangePwdType"
          />

        </span>
      </el-form-item>

      <el-form-item class="code-box" prop="captcha_code">
       <span class="icon-container">
          <Tickets style="width: 1em;height: 1em"/>
        </span>
        <el-input
            placeholder="图形验证码"
            v-model="loginForm.captcha_code" name="captcha_code" class="code-input" maxlength="4" @keyup.enter.native="handleLogin">
        </el-input>
        <div class="code-img" @click="getCodeImg">{{ code_net }}</div>
      </el-form-item>


      <el-button type="primary" style="width: 100%; margin-bottom: 30px;" :loading="loading"
                 @click.native.prevent="handleLogin"
                 size="large">
        <span v-if="!loading">登 录</span>
        <span v-else>登 录 中...</span>
      </el-button>


    </el-form>
    <!--  底部  -->
    <div class="el-login-footer">
      <span>项目搭建博客地址：https://juejin.cn/user/1310273591836957</span>
    </div>

  </div>
</template>

<script setup>
import {UserFilled, Lock, Tickets} from '@element-plus/icons'

import {ref, onMounted} from 'vue'
import {validatePassword, validateCode} from './rules'
import {getCode} from '@/api/api'
import {useStore} from 'vuex'
import {useRouter} from 'vue-router'
import {ElMessage} from "element-plus";

const code_net = ref('')

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
  captcha_code: [
    {
      required: true,
      trigger: 'blur',
      validator: validateCode()
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
    console.log(loginForm.value)
    if(loginForm.value.captcha_code != code_net.value){
      ElMessage.error("验证码错误！")
      return;
    }
    loading.value = true
    store.dispatch('user/login', loginForm.value)
        .then(() => {
          setTimeout(() => {
            loading.value = false
            // TODO: 登录后操作
            router.push('/')
          }, 500)
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
  getCode({})
      .then(data => {
        let obj = data.bizobj

        loginForm.value.code_key = obj.code_key
        code_net.value = obj.code
      })
      .catch(err => {
      })
}


</script>

<style lang="scss" scoped>
$bg: #5268bc;
$dark_gray: #889aa4;
$light_gray: #eee;
$cursor: #000000;
$txt_color: #333;


.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-image: url("../../assets/login-background.jpeg");
  background-size: cover;
  .login-form {
    position: relative;
    width: 420px;
    max-width: 100%;
    padding: 35px;
    margin: 0 auto;
    overflow: hidden;
    background: white;
    margin-top: 3%;
    ::v-deep .el-form-item {
      border: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(0, 0, 0, 0.1);
      border-radius: 5px;
      color: #454545;
    }

    ::v-deep .el-input {
      display: inline-block;
      height: 47px;
      width: 85%;

      input {
        padding: 12px 5px 12px 15px;
        height: 47px;
        caret-color: $cursor;
        color: $txt_color;
      }

      .el-input__wrapper {
        background: none;
        box-shadow: none;
        width: 90%;
        height: 47px;
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

  .code-box {
    position: relative;

    .code-img {
      position: absolute;
      width: 60px;
      right: 0;
      top: 6px;
      font-size: 22px;
      background: transparent;

    }
  }
  .el-login-footer {
    height: 40px;
    line-height: 40px;
    position: fixed;
    bottom: 0;
    width: 100%;
    text-align: center;
    color: #fff;
    font-family: Arial;
    font-size: 12px;
    letter-spacing: 1px;
  }
}
</style>
