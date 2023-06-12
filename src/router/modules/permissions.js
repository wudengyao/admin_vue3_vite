/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

export default{
  path: '/adminAuth',
  component: Layout,
  redirect: '/adminAuth/getRoleList',
  alwaysShow: true, // will always show the root menu
  name: 'adminAuth',
  meta: {
    title: '权限管理',
    icon: 'permission'
  },
  children: [
    {
      path: '/adminAuth/getRoleList',
      component: () => import('@/views/permissions-page/roleList.vue'),
      name: 'getRoleList',
      meta: { title: '角色管理',icon:'role'}
    },
    {
      path: '/adminAuth/adminList',
      component: () => import('@/views/permissions-page/accountList.vue'),
      name: 'adminList',
      meta: { title: '账号管理',icon:'personnel'}
    },
    {
      path: '/account/detail',
      name: 'accountDetail',
      component: () => import('@/views/permissions-page/accountDetail.vue'),
      meta: { title: '账号详情',icon:'personnel'},
      hidden: true,//true不显示在侧边栏

    }

  ]
}

