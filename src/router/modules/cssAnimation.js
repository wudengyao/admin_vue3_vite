/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

export default {
  path: '/cssAnimation',
  component: Layout,
  redirect: '/cssAnimation/shootingStar',
  alwaysShow: true, // will always show the root menu
  name: 'audio',
  meta: {
    title: 'CSS动画',
    icon: 'article-ranking'
  },
  children: [
    {
      path: '/cssAnimation/shootingStar',
      component: () => import('@/views/css-animation/shootingStar.vue'),
      name: 'shootingStar',
      meta: {title: '流星雨', icon: 'star'}
    },
    {
      path: '/cssAnimation/jumpBlock',
      component: () => import('@/views/css-animation/jumpBlock.vue'),
      name: 'jumpBlock',
      meta: {title: '能跳动的icon', icon: 'star'}
    },
    {
      path: '/cssAnimation/downBtn',
      component: () => import('@/views/css-animation/downBtn.vue'),
      name: 'downBtn',
      meta: {title: '奇怪的下载按钮', icon: 'star'}
    },
    {
      path: '/cssAnimation/videoMaskText',
      component: () => import('@/views/css-animation/videoMaskText.vue'),
      name: 'videoMaskText',
      meta: {title: '以视频为背景的文字', icon: 'star'}
    },
    {
      path: '/cssAnimation/hoverShiningBtn',
      component: () => import('@/views/css-animation/hoverShiningBtn.vue'),
      name: 'hoverShiningBtn',
      meta: {title: '发光的hover按钮', icon: 'star'}
    },
    {
      path: '/cssAnimation/filpCard',
      component: () => import('@/views/css-animation/filpCard.vue'),
      name: 'filpCard',
      meta: {title: '翻卡片动画', icon: 'star'}
    },
    {
      path: '/cssAnimation/hoverFillText',
      component: () => import('@/views/css-animation/hoverFillText.vue'),
      name: 'hoverFillText',
      meta: {title: 'hover菜单填充效果', icon: 'star'}
    },
    {
      path: '/cssAnimation/slidePic',
      component: () => import('@/views/css-animation/slidePic.vue'),
      name: 'slidePic',
      meta: {title: '图片无缝滚动切换', icon: 'star'}
    },
    {
      path: '/cssAnimation/bubbleFloat',
      component: () => import('@/views/css-animation/bubbleFloat.vue'),
      name: 'bubbleFloat',
      meta: {title: 'ios动态气泡壁纸', icon: 'star'}
    },
    {
      path: '/cssAnimation/waveloading',
      component: () => import('@/views/css-animation/waveloading.vue'),
      name: 'waveloading',
      meta: {title: '水波纹loading效果', icon: 'star'}
    },
    {
      path: '/cssAnimation/fullscreenMenu',
      component: () => import('@/views/css-animation/fullscreenMenu.vue'),
      name: 'fullscreenMenu',
      meta: {title: '全屏菜单动画', icon: 'star'}
    },
    {
      path: '/cssAnimation/hoverSlideMenu',
      component: () => import('@/views/css-animation/hoverSlideMenu.vue'),
      name: 'hoverSlideMenu',
      meta: {title: 'hover菜单扫描效果', icon: 'star'}
    },
    {
      path: '/cssAnimation/tabs',
      component: () => import('@/views/css-animation/tabs.vue'),
      name: 'tabs',
      meta: {title: '有趣的tab效果', icon: 'star'}
    },
    {
      path: '/cssAnimation/hoverBorderBtn',
      component: () => import('@/views/css-animation/hoverBorderBtn.vue'),
      name: 'hoverBorderBtn',
      meta: {title: '有趣的hover按钮', icon: 'star'}
    },
  ]
}

