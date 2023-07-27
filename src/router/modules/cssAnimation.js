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
  ]
}

